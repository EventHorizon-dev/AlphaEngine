# AlphaEngine | Portfolio Optimizer

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AlphaEngine** is an interactive web application built with **Flask** and **Python**. It computes the optimal asset allocation for an investment portfolio by minimizing risk using Modern Portfolio Theory (MPT), and generates an interactive donut chart with **Plotly**.

---

## Key Features

* **Real-Time Market Data:** Fetches live financial data using the Yahoo Finance API (`yfinance`).
* **Mathematical Optimization:** Uses the SLSQP algorithm (`scipy.optimize`) to calculate the optimal asset weights for minimum portfolio variance.
* **Modern Web Dashboard:** A clean, responsive interface featuring dynamic input fields built with JavaScript.
* **Interactive Visualizations:** Renders a sleek, responsive donut chart using Plotly.

---

## Tech Stack

* **Backend:** Python, Flask
* **Math & Data Science:** NumPy, SciPy, Pandas
* **Financial Data:** yfinance
* **Visualization:** Plotly
* **Frontend:** HTML5, CSS3, JavaScript

---

## Installation and Setup

Follow these steps to run the project locally on your machine:

1. **Clone the repository:**
   git clone https://github.com/EventHorizon-dev/AlphaEngine.git
   cd AlphaEngine

2. **Install the required dependencies:**
   pip install -r requirements.txt

3. **Run the Flask application:**
   python moteur.py

4. **Open your browser and navigate to:**
   http://127.0.0.1:5000

---

## Project Structure

AlphaEngine/
│
├── moteur.py               # Main Flask application logic
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── templates/
    └── index.html          # Frontend dashboard interface

---

## Author

Developed with passion by **EventHorizon-dev**. Feel free to check out my other projects on GitHub!