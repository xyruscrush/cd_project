# 🚀 AI-Based GitHub Code Analyzer

> An intelligent system that analyzes GitHub repositories using Machine Learning to evaluate code quality, activity, importance, and security risks — all visualized through a modern dashboard.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Demo](#-demo)
* [Features](#-features)
* [System Architecture](#-system-architecture)
* [Tech Stack](#-tech-stack)
* [Machine Learning Model](#-machine-learning-model)
* [Dataset](#-dataset)
* [How It Works](#-how-it-works)
* [Project Structure](#-project-structure)
* [Installation & Setup](#-installation--setup)
* [Usage Guide](#-usage-guide)
* [Output Explanation](#-output-explanation)
* [Screenshots](#-screenshots)
* [Challenges & Solutions](#-challenges--solutions)
* [Limitations](#-limitations)
* [Future Improvements](#-future-improvements)
* [Contributing](#-contributing)
* [Author](#-author)
* [License](#-license)

---

## 🧠 Overview

The **AI-Based GitHub Code Analyzer** is a full-stack application that integrates:

* Static Code Analysis
* Machine Learning
* Web-based Visualization

It automatically analyzes Python code from any GitHub repository and predicts multiple quality metrics such as:

* Code Usage
* Activity Level
* Importance
* Sensitivity (security risks)

This helps developers understand their codebase better and identify potential issues quickly.

---

## 🎥 Demo

> Paste a GitHub repo URL → Click Analyze → Get insights instantly

Example:

```
https://github.com/pallets/flask
```

---

## ✨ Features

### 🔍 Code Analysis

* Parses Python files using AST
* Extracts structural and behavioral features

### 🤖 Machine Learning Predictions

* Multi-output classification model
* Predicts 4 different code metrics

### 📊 Visualization Dashboard

* Clean UI with responsive design
* Bar charts for all metrics
* Summary insights

### ⚡ Real-Time Processing

* Clones repo dynamically
* Analyzes files instantly

---

## 🏗️ System Architecture

```
Frontend (HTML/CSS/JS)
        ↓
Flask Backend API
        ↓
Feature Extraction (AST Parsing)
        ↓
ML Model (Random Forest - Multi Output)
        ↓
Predictions → Visualization (Charts)
```

---

## 🧰 Tech Stack

### 🔹 Backend

* Python
* Flask
* GitPython
* AST (Abstract Syntax Tree)

### 🔹 Machine Learning

* Scikit-learn
* Pandas
* Joblib

### 🔹 Frontend

* HTML
* CSS
* JavaScript
* Chart.js

---

## 🤖 Machine Learning Model

### Model Type

* **Random Forest Classifier**
* Multi-output classification

### Input Features

* Lines of Code (LOC)
* Number of Parameters
* Cyclomatic Complexity
* Commit Count (approx)
* Code Churn
* Days Since Last Edit
* Author Count
* Sensitive Keyword Presence

### Output Labels

| Metric      | Description                   |
| ----------- | ----------------------------- |
| Usage       | How frequently code is used   |
| Activity    | How recently code is modified |
| Importance  | Criticality of code           |
| Sensitivity | Security risk level           |

Each label ranges from **0 (Low) → 3 (High)**

---

## 📊 Dataset

* Generated synthetic dataset (5000 samples)
* Feature-based rule generation
* Balanced representation of code scenarios

---

## ⚙️ How It Works

1. User enters GitHub repository URL
2. Backend clones the repository
3. Python files are scanned
4. Features are extracted using AST
5. ML model predicts scores
6. Results are sent to frontend
7. Dashboard displays results

---

## 📁 Project Structure

```
project/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   └── app.py
│
├── ml_model/
│   ├── code_analysis_dataset.csv
│   ├── code_analysis_model.pkl
│   ├── generate_dataset.py
│   ├── train_model.py
│   └── test_model.py
│
└── venv/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install flask flask-cors pandas scikit-learn joblib gitpython
```

---

### 4️⃣ Run Backend

```bash
cd backend
python app.py
```

---

### 5️⃣ Run Frontend

```bash
cd frontend
python3 -m http.server 5500
```

Open browser:

```
http://localhost:5500
```

---

## 🚀 Usage Guide

1. Enter a GitHub repository URL
2. Click **Analyze**
3. Wait for processing
4. View:

   * File-wise predictions
   * Summary stats
   * Bar charts

---

## 📈 Output Explanation

### 📊 Charts

* Distribution of:

  * Usage
  * Activity
  * Importance
  * Sensitivity

### 📁 File Cards

Each file shows:

* Usage Score
* Activity Score
* Importance Score
* Sensitivity Score

### 📌 Summary

* Total files analyzed
* High-risk files
* Sensitive files

---

## 📸 Screenshots

> Add screenshots here

```
/screenshots/ui.png
/screenshots/charts.png
```

---

## ⚠️ Challenges & Solutions

### Challenges

* GitHub URL parsing issues
* Model loading errors
* Backend-frontend communication
* UI design improvements

### Solutions

* URL cleaning logic
* Dynamic model path detection
* Error handling
* UI redesign

---

## 🚧 Limitations

* Supports only Python files
* Uses synthetic dataset
* Approximate commit/activity data

---

## 🔮 Future Improvements

* Multi-language support (C++, Java)
* Real GitHub API integration
* Deep learning models
* Code-level highlighting
* Cloud deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork repo
2. Create feature branch
3. Commit changes
4. Open Pull Request

---

## 👨‍💻 Author

**Your Name**

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🚀 Share it

---
