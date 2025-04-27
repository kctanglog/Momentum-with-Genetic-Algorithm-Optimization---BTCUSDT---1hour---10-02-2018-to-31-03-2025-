# 🎯 **Momentum_Backtester - Genetic Algorithm Optimization**  
**BTCUSDT - 1 Hour Interval (10-02-2018 to 31-03-2025**)

---

## 📖 **Project Overview**  
This project demonstrates a **Momentum-Based Trading Strategy**, optimized using **Brute Force** and **Genetic Algorithm (GA)** methods.  
Designed for **professional traders** and **quantitative analysts**, this tool helps fine-tune momentum parameters to maximize profitability through robust backtesting and visualization.

---

## 🚀 **Workflow**  

1. **📊 Fetch Historical Data**  
   Retrieve BTCUSDT candlestick data (OHLCV) from Binance API for the specified time range and interval.  

2. **📈 Backtest the Strategy**  
   Simulate and analyze momentum-based strategies, including:  
   - **Optimization**: Use **Brute Force** or **Genetic Algorithm** techniques to identify the optimal momentum parameter.  
   - **Visualization**: Compare cumulative returns and strategy performance through performance plots, heatmaps, and GA progress charts.  

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
  - Heatmaps for Brute Force optimization results.  
  - **GA Progress Visualization**: Track performance improvements across generations.  

---

## 📂 **File Structure**  

> **`Momentum_Backtester_GA.py`**  
> The main Python class for backtesting and optimization.  

> **`Momentum_Backtester_CodeRunner_GA.ipynb`**  
> Jupyter Notebook for executing backtests and optimizations.  

> **`Data/`**  
> Directory for storing historical data fetched from Binance API.  

---

## 📊 **Results**  

### **Brute Force Optimization**  
- **🏆 Best Momentum:** `747`  
- **📊 Best Performance:** `1,248,957.56`  
- **📈 Out-Performance:** `1,157,473.84`  

### **Genetic Algorithm Optimization**  
- **🏆 Optimal Momentum Found:** `793`  
- **📊 Performance:** `1,062,386.03`  

---

### **Key Insights**  
The **Genetic Algorithm** delivers results close to Brute Force, proving its **efficiency** for optimizing high-dimensional trading strategies with far less computational expense.

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
