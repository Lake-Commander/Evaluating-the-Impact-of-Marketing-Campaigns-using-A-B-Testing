# 📊 Evaluating-the-Impact-of-Marketing-Campaigns-using-A-B-Testing

Welcome to the **Marketing Campaign A/B Test Analysis** project! This repository contains a professional analysis of marketing campaign data using Python, hypothesis testing, and a dynamic **Streamlit dashboard** for visualization.

---

## 🧠 Project Overview

This project evaluates the performance of a marketing campaign by comparing two user groups:

* **Ad Group** (users shown advertisements)
* **PSA Group** (users shown a public service announcement or nothing)

The primary goals are:

1. ✅ Determine whether ads lead to higher conversion rates.
2. 💰 Estimate the revenue generated from ad conversions.
3. 📐 Use A/B testing (Chi-square test) to assess statistical significance.
4. 💡 Provide actionable business insights.

---

## 📁 Files in This Repository

| File                                   | Description                                                         |
| -------------------------------------- | ------------------------------------------------------------------- |
| `marketing_AB.csv`                     | Dataset containing user interactions and ad exposure details        |
| `AB_testing.ipynb` | Jupyter Notebook with complete data analysis and hypothesis testing |
| `AB_test_dashboard.py`                 | Streamlit app to interactively visualize results                    |
| `README.md`                            | This file - explanation and usage guide                             |

---

## 🧪 Technologies Used

* **Python** (Pandas, Matplotlib, Seaborn, Scipy)
* **Jupyter Notebook** for analysis
* **Streamlit** for the dashboard

---

## 🚀 How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/Lake-Commander/Evaluating-the-Impact-of-Marketing-Campaigns-using-A-B-Testing.git
cd Evaluating-the-Impact-of-Marketing-Campaigns-using-A-B-Testing
```

### 2. Install Required Packages

Use pip to install the needed libraries:

```bash
pip install -r requirements.txt
```

If no `requirements.txt` exists, install manually:

```bash
pip install pandas seaborn matplotlib scipy streamlit
```

### 3. Run the Jupyter Notebook (Optional)

```bash
jupyter notebook AB_testing.ipynb
```

Explore the full analysis step by step.

### 4. Run the Streamlit Dashboard

```bash
streamlit run AB_test_dashboard.py
```

This will launch a web-based dashboard at `http://localhost:8501`.

---

## 🎯 Insights You Can Gain

* Which group converted more users?
* When are ads most effective (time/day)?
* How much revenue did the campaign generate?
* Are the results statistically significant?
* What should marketers do next?

---

## 📈 Sample Dashboard Preview

View dashboard here

https://evaluating-the-impact-of-marketing-campaigns-using-a-b-testing.streamlit.app/

---

## 🤝 Contributing

Contributions are welcome! If you’d like to:

* Improve dashboard visuals
* Add new statistical tests
* Translate to another language

Please fork the repo and submit a pull request.

---

## 📬 Contact

Feel free to connect if you have questions:

* [Mail](mailto:elakhe.ephraim.9@egmail.com)
* [GitHub](https://github.com/Lake-Commander)

---

## 📝 License

This project is licensed under the MIT License.

---

**Built for educational purposes and marketing analytics practice.**
