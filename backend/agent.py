import matplotlib
matplotlib.use('Agg')  # Backend for headless plotting
import matplotlib.pyplot as plt
from langgraph.graph import Graph
import yfinance as yf
import os


class StockState:
    def __init__(self, ticker: str, period: str = "1mo", user_confirmation: bool = False):
        self.ticker = ticker
        self.period = period
        self.stock_price = None
        self.metrics = None
        self.plot_filename = None
        self.user_confirmation = user_confirmation


def fetch_stock_data(state: StockState) -> StockState:
    """Fetch stock data and update the state."""
    try:
        stock = yf.Ticker(state.ticker)
        data = stock.history(period=state.period)
        if data.empty:
            raise ValueError(f"No data found for ticker: {state.ticker}")

        state.stock_price = data['Close'].iloc[-1]
        state.metrics = {
            'open': float(data['Open'].iloc[-1]),
            'high': float(data['High'].iloc[-1]),
            'low': float(data['Low'].iloc[-1]),
        }
        return state
    except Exception as e:
        raise ValueError(f"Error fetching stock data: {e}")


def generate_plot(state: StockState) -> StockState:
    """Generate a plot and save it as an image."""
    if state.user_confirmation:
        try:
            stock = yf.Ticker(state.ticker)
            data = stock.history(period=state.period)

            if data.empty:
                raise ValueError(f"No data found for ticker: {state.ticker}")

            plt.figure(figsize=(10, 5))
            plt.plot(data.index, data['Close'], label=f'{state.ticker} Close Price', color='blue')
            plt.title(f'{state.ticker} Stock Price Over {state.period}')
            plt.xlabel('Date')
            plt.ylabel('Price (USD)')
            plt.legend()

            # Ensure the static directory exists
            os.makedirs('static', exist_ok=True)

            # Save the plot in the static directory
            plot_filename = f"static/{state.ticker.lower()}_plot.png"
            plt.savefig(plot_filename)
            plt.close()

            # Update the state with the correct filename
            state.plot_filename = plot_filename
            print(f"Plot generated successfully: {plot_filename}")
            print(f"State after plot generation: {state.__dict__}")  # Debugging log
        except Exception as e:
            print(f"Error generating plot: {e}")
            state.plot_filename = None
    return state

# Define the workflow using LangGraph
workflow = Graph()
workflow.add_node("fetch_stock_data", fetch_stock_data)
workflow.add_node("generate_plot", generate_plot)
workflow.add_edge("fetch_stock_data", "generate_plot")
workflow.set_entry_point("fetch_stock_data")

app = workflow.compile()
