---

# 🫀 Ischemic Heart Disease Analysis & Dashboard – Nigeria
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

![Dashboard Screenshot](/analysis/IHD_dashboard.jpeg)
---

## 📊 Overview

This project presents a **comprehensive data-driven analysis** of **Ischemic Heart Disease (IHD)** in Nigeria, focusing on trends, demographics, healthcare infrastructure, and expenditure.

It includes:

* A **Streamlit-powered interactive dashboard** for real-time exploration 📈
* A **classification model** to predict heart disease risk using machine learning 🔍

> Built with Python, Pandas, Plotly, and scikit-learn.

---

## 🚀 Features

### 📉 Exploratory Data Analysis

* 📆 **Yearly Trends** in IHD deaths (by gender & age group)
* ⚰️ **Top Causes of Death** comparison to IHD
* 🏥 **Doctor-to-Patient Ratio** tracking over time
* 💰 **Health Expenditure per Capita** visualization

### 🧠 Classification Modeling

* Logistic Regression, Random Forest, and Decision Tree models evaluated
* Key metrics: **Accuracy, Precision, Recall, F1 Score, Log Loss**
* Decision Tree emerged as the best performer with **\~82% accuracy**

### 🖥️ Interactive Dashboard (Streamlit)

* Real-time bar, pie, and line charts
* Responsive layout for seamless exploration
* Clean, minimal design with actionable insights

---

## 🖼️ Dashboard Preview

> *Add your dashboard screenshot above to showcase it visually*

---

## 🗂️ Project Structure

```
Ischemic-heart-disease-/
├── analysis/
│   ├── dashboard.py             # Streamlit app source
│   ├── IHD_analysis.ipynb       # Jupyter notebook (EDA + ML models)
│   ├── cleaned_data/            # Cleaned datasets
│   └── rough_data/              # Raw or semi-clean datasets
│   └── IHD_dashboard.jpeg
├── requirements.txt             # Project dependencies
├── README.md                    # This file
└── LICENSE
```

---

## ⚙️ Getting Started

### ✅ Prerequisites

* Python 3.8+
* pip (Python package manager)

### 💻 Installation

```bash
git clone https://github.com/your-username/Ischemic-heart-disease-.git
cd Ischemic-heart-disease-
pip install -r requirements.txt
```

### 🚀 Run the Dashboard

```bash
streamlit run /analysis/dashboard.py
```

The app will launch in your browser.

---

## 📂 Datasets

| File                   | Description                               |
| ---------------------- | ----------------------------------------- |
| `cleaned_data_df1.csv` | IHD deaths by year, age group, and gender |
| `cleaned_data_df2.csv` | Top 10 causes of death in Nigeria         |
| `cleaned_data_df3.csv` | Doctor-to-patient ratio per year          |
| `cleaned_data_df4.csv` | Health expenditure per capita (USD)       |

---

## 🔍 Model Performance Summary

| Model               | Accuracy     | F1 Score   | Precision     | Recall | Log Loss |
| ------------------- | ------------ | ---------- | ------------- | ------ | -------- |
| Logistic Regression | 73.33%       | 72.41%     | 70.00%        | 75.00% | N/A      |
| Random Forest       | 71.67%       | 70.17%     | 68.97%        | 71.43% | N/A      |
| Decision Tree       | **81.67%** ✅ | **78.43%** | **83.33%** 🔥 | 74.07% | **6.61** |

> 💡 **Decision Tree** was the most effective model overall, offering strong precision and interpretability.

---

## 🛠️ Customization

* Modify `dashboard.py` to customize charts or filters.
* Swap in new datasets under the `analysis/cleaned_data/` directory — just make sure the column names stay consistent!

---

## 🤝 Contributing

Got suggestions or improvements? Contributions are warmly welcome!

* Fork the repo
* Open an issue
* Submit a pull request 🚀

---

## 📄 License

Distributed under the **MIT License**.
See [LICENSE](LICENSE) for full details.

---

## 📬 Contact

For questions, ideas, or collaboration opportunities:
📧 \[[fehintolusamuel@gmail.com](mailto:ehintolusamuel@gmail.com)]

---

> *Developed by \[Fehintolu Samuel], 2025. Powered by data, driven by impact.*
