# 🎯 **Momentum_Backtester - Genetic Algorithm Optimization**  
**BTCUSDT - 1 Hour Interval (10-02-2018 to 31-03-2025)**

---

## 🪙 **Project Overview**  
This project showcases a **Momentum-Based Trading Strategy**, optimized using **Brute Force** and **Genetic Algorithm (GA)** techniques.  
It is designed for **professional traders** and **quantitative finance enthusiasts** to assess and fine-tune trading parameters for maximum profitability.

---

## 🚀 **Workflow**  

1. **📊 Fetch Historical Data**  
   Pull BTCUSDT candlestick data (OHLCV) from Binance API for the specified time range and interval.  

2. **📈 Backtest the Strategy**  
   Simulate the performance of momentum strategies using the `Momentum_Backtester` class.

3. **🧬 Optimize Parameters**  
   - **Brute Force**: Screen all possible momentum values within a given range.  
   - **Genetic Algorithm**: Use evolution-based optimization to find the **optimal momentum value** efficiently.

4. **📉 Visualize Results**  
   Generate visualizations of strategy performance, heatmaps, and GA optimization progress.  

---

## ✨ **Features**  

- **🔗 Historical Data Retrieval**:  
  Fetch and preprocess data from Binance API.  

- **⚙️ Vectorized Backtesting**:  
  Backtest momentum-based strategies for rapid performance evaluation.

- **📊 Parameter Optimization**:  
  - **Brute Force**: Test each momentum value exhaustively.  
  - **Genetic Algorithm**: Use evolutionary techniques to find the best momentum parameter.  

- **📈 Visualizations**:  
  - Performance comparison: **Cumulative Returns vs. Strategy Performance**.  
  - Heatmaps for brute force optimization results.  
  - **GA Progress Visualization**: Plot performance across generations.  

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

### **Brute Force Optimization**  
- **🏆 Best Momentum:** `747`  
- **💰 Best Performance:** `1,248,957.56`  
- **📈 Out-Performance:** `1,157,473.84`  

### **Genetic Algorithm Optimization**  
- **🏆 Optimal Momentum Found:** `793`  
- **💰 Performance:** `1,062,386.03`  

---

### **Key Insights**  
The **Genetic Algorithm** delivers results close to Brute Force, demonstrating its **efficiency** for optimizing high-dimensional trading strategies with less computational effort.

---

## 🛠 **Requirements**  

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
