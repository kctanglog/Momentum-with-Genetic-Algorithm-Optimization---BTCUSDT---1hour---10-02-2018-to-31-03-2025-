# Momentum with Genetic Algorithm Optimization  
**BTCUSDT - 1 Hour Interval (10-02-2018 to 31-03-2025)**

---

## 📖 Overview  
This project implements a **Momentum Strategy** for cryptocurrency trading, optimized using a **Genetic Algorithm (GA)**. The process includes fetching historical data from Binance, backtesting the strategy, and analyzing the results.

---

## 🚀 Workflow  
1. **Pull Data from Binance API**  
   Fetch historical BTCUSDT data for the specified time period.

2. **Backtest the Strategy**  
   Use the `Momentum_Backtester_CodeRunner_GA.ipynb` notebook to run the backtests.  
   - **Main Code**: `Momentum_Backtester_GA.py`  
   - **Optimization**: Genetic Algorithm for parameter tuning.

---

## 📂 File Structure  
- **`Momentum_Backtester_GA.py`**  
  The main Python script containing the momentum strategy logic and GA optimization implementation.

- **`Momentum_Backtester_CodeRunner_GA.ipynb`**  
  Jupyter Notebook used for running and visualizing backtest results.

---

## 📊 Results  
The backtesting results, including performance metrics and visualizations, are generated and stored within the notebook. The Genetic Algorithm optimizes key parameters to maximize profitability.

---

## 🛠 Requirements  
- Python 3.8+
- Libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `binance` API wrapper
  - `scipy`

Install dependencies using:
```bash
pip install -r requirements.txt
