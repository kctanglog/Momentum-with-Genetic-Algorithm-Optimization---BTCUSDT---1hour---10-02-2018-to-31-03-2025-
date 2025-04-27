# 🧬📈 **Momentum Backtester - Genetic Algorithm (GA) Optimization**  
**Data**
BTCUSDT - 1 Hour Interval (10-02-2018 to 31-03-2025)

---

## 📖 **Project Overview**  
This project demonstrates a **Momentum-Based Trading Strategy**, optimized using **Brute Force** and **Genetic Algorithm (GA)** methods.  
It helps fine-tune momentum parameters to maximize profitability through robust backtesting and visualization.

---

## 🚀 **Workflow**  

1. **📊 Fetch Historical Data**  
   Retrieve BTCUSDT candlestick data (OHLCV) from Binance API for the specified time range and interval.  

2. **📈 Backtest the Strategy**  
   Simulate and analyze momentum-based strategies, including:  
   - **Optimization**: Use **Brute Force** or **Genetic Algorithm** techniques to identify the optimal momentum parameter.  
   - **Visualization**: Compare cumulative returns and strategy performance through performance plots, **heatmaps**, and **Genetic Algorithm (GA) progress charts**.  

---

## ✨ **Features**  

- **🔗 Historical Data Retrieval**:  
  Fetch and preprocess data from Binance API.  

- **⚙️ Vectorized Backtesting**:  
  Efficiently simulate trading strategies in a vectorized manner.  

- **📊 Momentum Optimization**:  
  - **Brute Force**: Test all possible momentum values exhaustively.  
  - **Genetic Algorithm**: Leverage evolution-based optimization for high-dimensional parameter tuning.  

- **📉 Visualizations**:  
  - Strategy performance comparison: **Cumulative Returns vs. Strategy Performance**.  
  - **Heatmaps**: Visualize optimization results for Brute Force searches.  
  - **Genetic Algorithm (GA) progress charts**: Track performance improvements across generations.  

---

## 📂 **File Structure**  

- **`Momentum_Backtester_GA.py`**  
  The main Python class for backtesting and optimization.  

- **`Momentum_Backtester_CodeRunner_GA.ipynb`**  
  Jupyter Notebook for executing backtests and optimizations.  

- **`Data/`**  
  Directory for storing historical data fetched from Binance API.  

---

## 📊 **Results**  

### **Initial Capital: 10,000**  

### **Brute Force Optimization**  
- **🏆 Best Momentum:** `747`  
- **📊 Best Performance:** `1,248,957.56`  
- **📈 Out-Performance:** `1,157,473.84`  

### **Genetic Algorithm Optimization**  
- **🏆 Optimal Momentum Found:** `793`  
- **📊 Performance:** `1,062,386.03`  

---

### **Key Insights**  

The **Genetic Algorithm (GA)** demonstrates the following advantages:  

1. **Efficiency**:  
   Unlike Brute Force, which exhaustively tests every momentum value, GA uses an evolution-based approach to **quickly converge** on the optimal parameter, significantly reducing computational time and expense.  

2. **Scalability**:  
   GA is highly effective for **high-dimensional optimization problems**, making it suitable for strategies involving multiple parameters or large data sets.  

3. **Robustness**:  
   The algorithm avoids getting stuck in **local optima** by using random mutations and crossover operations, ensuring a more global search for the best parameters.

4. **Practicality**:  
   The results produced by GA are **comparable to Brute Force**, proving its reliability for real-world trading applications.  

---

## 🛠 **Requirements**  

- **Python**: 3.12.7  
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
