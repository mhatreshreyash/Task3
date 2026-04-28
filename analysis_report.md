# 📊 Sales Data Analysis Report

## 📌 Project Overview

This project analyzes a sales dataset using Python and pandas to extract meaningful insights such as total sales, best-selling products, and revenue trends.

---

##  Tools & Technologies

* Python
* pandas
* VS Code

---

##  Dataset Description

The dataset contains the following columns:

* **Product** – Name of the product
* **Quantity** – Number of units sold
* **Price** – Price per unit

---

##  Data Cleaning

* Missing values in **Product** were replaced with `"Unknown"`
* Missing values in **Quantity** and **Price** were replaced with `0`
* A new column **Total_Sales** was created:

  ```
  Total_Sales = Quantity × Price
  ```

---

## 📈 Key Metrics

### 1. Total Sales

The total revenue generated from all transactions.

### 2. Best-Selling Product

Product with the highest total quantity sold.

### 3. Top Revenue Product

Product that generated the highest revenue.

### 4. Average Sales

Average revenue per transaction.

---

## 📊 Results Summary

| Metric               | Value       |
| -------------------- | ----------- |
| Total Sales          | ₹12365048.00|
| Best-Selling Product | Laptop      |
| Top Revenue Product  | Laptop      |
| Average Sales        | ₹123650.48  |

---

## 🔍 Insights

* The best-selling product indicates high demand.
* The top revenue product may differ due to pricing differences.
* Missing values were handled to ensure accurate calculations.

---

## 📌 Conclusion

This analysis provides a clear overview of sales performance and helps identify key products driving revenue. It can be further enhanced using visualization tools like charts and dashboards.

---

## 🚀 Future Improvements

* Add data visualization (bar charts, pie charts)
* Perform time-based analysis (monthly/yearly trends)
* Build an interactive dashboard using Streamlit or Power BI

---
