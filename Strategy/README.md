# Momentum_Backtester - Genetic Algorithm Optimization

**BTCUSDT - 1 Hour Interval (10-02-2018 to 31-03-2025)**

---

## 📖 Overview  
This project implements a **Momentum Strategy** for cryptocurrency trading, optimized using both **Brute Force** and **Genetic Algorithm (GA)** methods. The backtester is designed to evaluate momentum-based strategies and optimize their parameters for maximum profitability.

---

## 🚀 Workflow  
1. **Fetch Historical Data**  
   Pull candlestick data (OHLCV) from Binance API for the specified trading pair, interval, and date range.

2. **Backtesting**  
   Use the `Momentum_Backtester` class to backtest strategies based on the momentum parameter.

3. **Optimization**  
   - **Brute Force**: Evaluate all possible momentum values within a defined range.
   - **Genetic Algorithm**: Use GA to efficiently find the optimal momentum parameter.

4. **Visualization**  
   Generate performance graphs, heatmaps, and GA optimization progress visualizations.

---

## 🛠 Features  
- **Historical Data Fetching:** Utilize the Binance API to fetch and preprocess raw data.
- **Momentum Strategy Execution:** Vectorized backtesting of trading strategies based on momentum.
- **Parameter Optimization:**  
  - Brute Force: Exhaustive testing of momentum values.  
  - Genetic Algorithm: Efficient optimization using evolutionary techniques.
- **Visualizations:**  
  - Strategy performance comparison (cumulative returns vs. cumulative strategy).  
  - Heatmaps for brute force optimization results.  
  - GA optimization progress visualization (generation vs. performance).  

---

## 📂 File Structure  
- **`Momentum_Backtester_GA.py`**  
  The main Python class for backtesting and optimization.  

- **`Momentum_Backtester_CodeRunner_GA.ipynb`**  
  Jupyter Notebook for running backtests, visualizations, and optimizations.  

- **`Data/`**  
  Directory for storing historical data fetched from Binance API.

---

## 📊 Results  

### Brute Force Optimization  
- **Best Momentum:** `747`  
- **Best Performance:** `1,248,957.56`  
- **Out-Performance:** `1,157,473.84`  

---

### Genetic Algorithm Optimization  
- **Optimal Momentum Found:** `793`  
- **Performance:** `1,062,386.03`  

---

### Comment  
The **Genetic Algorithm** provides results very close to Brute Force, demonstrating its effectiveness in optimizing momentum strategies.

---

## 🛠 Requirements  
- Python 3.8+
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `requests`
  - `time`

Install dependencies using:
```bash
pip install -r requirements.txt
