import logging
from flask import Flask, request, jsonify, send_from_directory
import yfinance as yf
from flask_cors import CORS
from agent import StockState, fetch_stock_data, generate_plot

app = Flask(__name__)
CORS(app)

# Enable debugging logs
logging.basicConfig(level=logging.DEBUG)


def fetch_stock_data(ticker, period):
    """Fetch stock data using yfinance and return a JSON-serializable dictionary."""
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period=period)

        if history.empty:
            logging.error(f"No stock data found for {ticker} with period {period}")
            return None

        # Convert DataFrame to JSON-serializable dictionary
        data = history[['Open', 'High', 'Low', 'Close', 'Volume']].to_dict(orient='records')
        return data

    except Exception as e:
        logging.error(f"Error fetching stock data for {ticker}: {str(e)}")
        return None


@app.route('/fetch-stock', methods=['POST'])
def fetch_stock():
    """Handle stock fetching API request."""
    try:
        request_data = request.get_json()
        logging.debug(f"Received request data: {request_data}")

        ticker = request_data.get("ticker", "").upper()
        period = request_data.get("period", "1mo")

        if not ticker:
            return jsonify({"error": "Missing ticker"}), 400

        result = fetch_stock_data(ticker, period)

        if result is None:
            return jsonify({"error": "No data found or API error"}), 500

        return jsonify({"ticker": ticker, "data": result})

    except Exception as e:
        logging.error(f"Server error: {str(e)}")
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500


@app.route('/confirm-plot', methods=['POST'])
def confirm_plot():
    """Handle plot generation API request."""
    try:
        request_data = request.get_json()
        ticker = request_data.get("ticker", "").upper()
        period = request_data.get("period", "1mo")

        if not ticker:
            return jsonify({"error": "Missing ticker"}), 400

        # Initialize the state
        state = StockState(ticker=ticker, period=period, user_confirmation=True)

        # Execute the LangGraph workflow
        from agent import app as workflow_app
        final_state = workflow_app.invoke(state)

        if final_state and final_state.plot_filename:
            # Construct the correct URL
            plot_url = f"/static/{os.path.basename(final_state.plot_filename)}"
            print(f"Generated plot URL: {plot_url}")  # Debugging log
            return jsonify({"plotUrl": plot_url})
        else:
            logging.error(f"Failed to generate plot for {ticker}")
            return jsonify({"error": "Failed to generate plot"}), 500

    except Exception as e:
        logging.error(f"Error generating plot: {str(e)}")
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

@app.route('/static/<filename>')
def serve_static(filename):
    """Serve static files (e.g., generated plots)."""
    return send_from_directory('static', filename)


if __name__ == '__main__':
    app.run(debug=True)