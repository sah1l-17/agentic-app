# Stock Data Fetcher and Plot Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![React](https://img.shields.io/badge/React-17.0%2B-blue)
![YFinance](https://img.shields.io/badge/YFinance-0.2%2B-orange)

A web application that fetches stock data using the **Yahoo Finance API** (`yfinance`) and generates interactive plots using **Matplotlib**. The backend is built with **Flask**, and the frontend is built with **React**.

---

## Features

- **Fetch Stock Data**: Retrieve stock data (open, high, low, close, volume) for a given ticker and time period.
- **Generate Plots**: Generate and display interactive plots of stock prices over time.
- **User Confirmation**: Confirm ticker and plot generation through a user-friendly interface.
- **Responsive Design**: Built with a modern and responsive UI using React.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: React (JavaScript)
- **Data Fetching**: `yfinance` (Yahoo Finance API)
- **Plotting**: Matplotlib
- **Workflow Management**: LangGraph (for backend workflow)

---

## Installation

### Prerequisites

- Python 3.8+
- Node.js (for React frontend)
- Git

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/sah1l-17/agentic-app.git
   cd agentic-app/backend
Install Python dependencies:

   ```bash
pip install -r requirements.txt
Run the Flask backend:
   ```

   ```bash
python backend.py
```
The backend will start at http://127.0.0.1:5000.

Frontend Setup
Navigate to the frontend directory:

```bash
cd ../frontend
```
Install Node.js dependencies:

```bash
npm install
```
Run the React frontend:

```bash
npm start
```
The frontend will start at http://localhost:3000.

Usage
Open the application in your browser (http://localhost:3000).

Enter a stock ticker (e.g., AAPL, TSLA) and select a time period (e.g., 1mo, 1y).

Click Fetch Data to retrieve stock data.

Confirm the ticker and generate a plot of the stock prices.

Folder Structure
```bash
stock-data-fetcher/
├── backend/
│   ├── static/                  # Generated plot images
│   ├── agent.py                 # LangGraph workflow and state management
│   ├── backend.py               # Flask backend server
│   └── requirements.txt         # Python dependencies
├── frontend/
│   ├── public/                  # Static assets
│   ├── src/                     # React components
│   ├── package.json             # Node.js dependencies
│   └── README.md                # Frontend documentation
└── README.md                    # Project documentation
```
Contributing
Contributions are welcome! Follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Yahoo Finance for providing stock data.

Matplotlib for plotting.

Flask for backend development.

React for frontend development.

Contact
For questions or feedback, feel free to reach out:

Sahil Ansari

Email: sahil069917@gmail.com

GitHub: sah1l-17
