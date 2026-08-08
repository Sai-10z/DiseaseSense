# 🧬 DiseaseSense – ML Based Disease Prediction System

A Django-based clinical web application that predicts potential medical conditions from user-reported symptoms using machine learning. The system provides an end-to-end healthcare guidance pipeline, including multi-model evaluation, differential diagnosis (DDx), clinical urgency triage, specialist routing, tailored doctor interview preparation, and real-time prediction through a modern single-page interface.

Logistic Regression was selected as the primary production model for its high interpretability, low risk of overfitting, and rapid inference capability.

---

# 🚀 Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Joblib](https://img.shields.io/badge/Joblib-4B8BBE?logo=python&logoColor=white)](https://joblib.readthedocs.io/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

---

# 🏗 Workflow & Prediction Pipeline

```bash
👤 User Inputs Symptoms (Filterable Search Slots)
          ↓
🌐 Django Web Interface (Single-Page Seamless Navigation)
          ↓
⚡ Django Backend Processing & Vectorization (`views.py`)
          ↓
🧠 Serialized Logistic Regression Model (`model.joblib`)
          ↓
📊 Differential Diagnosis (DDx) & Probability Scoring
          ↓
📋 Clinical Care Package Output:
   ├── 🎯 Primary Disease Match & Animated Confidence Donut
   ├── 🚦 Triage & Urgency Severity Level
   ├── 🩺 Recommended Specialist & Google Maps Search Link
   ├── 📑 Top 3 Differential Diagnoses (Rank Color-Coded)
   ├── ❓ Tailored Doctor Questions & Visit Preparation Checklist
   └── 🚨 Emergency Services Hotline Badge (112 / 108)
```

---

# ✨ Core Features - 1

## 🧠 Machine Learning Module
- Data preprocessing and cleaning  
- Exploratory Data Analysis (EDA)  
- Correlation heatmap generation  
- Multi-model training and evaluation  
- Model performance comparison  
- Trained model serialization using Pickle  

## 🌐 Web Application Module
- Django-based interactive interface  
- Symptom-based disease prediction  
- Real-time prediction output  
- Backend integration with trained ML model  
- Simple and user-friendly workflow  

## 📊 Data Analysis & Visualization
- Prognosis distribution graphs  
- Symptom correlation heatmaps  
- Model accuracy comparison charts  
- Dataset exploration and preprocessing analysis  

---

# Core features 2 

## 🧠 Machine Learning & Backend Module
- **Optimized Feature Vectorization**: Converts selected symptoms into binary vectors corresponding to `Training.csv` feature schema.
- **Model Serialization (`model.joblib`)**: Fast, lightweight model loading using Joblib instead of standard pickle.
- **Differential Diagnosis Engine (DDx)**: Generates top 3 ranked candidate predictions with probability scores, guaranteeing non-zero candidates display at a 1% minimum.
- **Urgency Triage Engine**: Automatically maps predicted diseases to clinical severity levels (**High / Red**, **Moderate / Orange**, **Low / Green**).
- **Specialist Router**: Maps 41 disease classes to medical specialties (e.g., Dermatologist, Cardiologist, Pulmonologist).
- **Clinical Question Generator**: Algorithmically generates 3 tailored questions for the patient to ask during their upcoming physician consultation.

## 🌐 Web Application & UI/UX Design
- **Single-Page Application Architecture**: Smooth sectional scrolling (Hero → Symptoms → Results → Consultation Guidance).
- **Interactive Searchable Dropdowns**: Filterable symptom search with live slot progress counters (`0/3`, `1/3`, `2/3`, `3/3`).
- **Animated SVG Confidence Donut**: Custom SVG Donut Chart with scroll-triggered progress ring and centered percentage display.
- **Color-Coded Differential Diagnosis**: Rank #1 (`#7c3aed` Purple), Rank #2 (`#1d6fd8` Blue), Rank #3 (`#475569` Slate).
- **Action Buttons & Local Search**: Direct Google Maps specialist locator ("Find Nearby Specialist") with blue pulse indicator.
- **Emergency Services Badge**: High-visibility `Emergency Services: 112 / 108` pill badge with soft red halo pulse in Section 4.
- **Brand Assets**: Custom brand Logo (`Logo.webp`) positioned in the top right corner and WebP favicon integration (`Favicon.webp`).


---

# 🧪 Machine Learning Models & Results

| Model | Accuracy (%) |
|--------|--------------|
| Logistic Regression | 100.0 |
| K-Nearest Neighbors (KNN) | 100.0 |
| Naïve Bayes | 100.0 |
| Decision Tree | 97.62 |
| Random Forest | 97.62 |
| Gradient Boosting | 97.62 |

### ✅ Final Model Selection

Although multiple algorithms achieved top-tier evaluation scores during model training, **Logistic Regression** was selected as the final production model due to:

- High mathematical interpretability for healthcare applications  
- Computational efficiency and low memory overhead  
- Robust generalization across multi-class symptom features  
- Seamless integration with Joblib serialization  

---

# ⚙️ Development Workflow

## 📌 Phase 1 – Model Development

- Dataset preprocessing and cleaning  
- Feature analysis and visualization  
- Exploratory data analysis (EDA)  
- Training multiple ML algorithms  
- Performance evaluation and comparison  
- Final model selection  

## 📌 Phase 2 – Web Application Integration

- Model serialization using Pickle (`.pkl`)  
- Django backend integration  
- Symptom input form development  
- Real-time prediction handling  
- Result rendering on frontend  

---

# Development workflow 2

## 📌 Phase 1 – Model Training & Notebook Pipeline
- Dataset ingestion and preprocessing (`Training.csv`)  
- Feature matrix definition (132 clinical symptoms across 41 disease classes)  
- Multi-model evaluation and confusion matrix visualization (`Disease_Prediction_Model_Training.ipynb`)  
- Model export (`model.joblib`)  

## 📌 Phase 2 – Django Backend Architecture
- Custom views for single-page rendering (`views.py`)  
- Asynchronous prediction endpoint (`POST /predict/`) returning structured JSON payload  
- Static file serving configuration (`settings.py` & `urls.py`)  
- Robust error handling and silent fallback handling  

## 📌 Phase 3 – Web Application & UI Refinement
- Custom CSS Design System featuring responsive layouts and glassmorphic navigation  
- Dynamic JavaScript state management and DOM manipulation  
- Interactive charts and rank-based differential diagnosis UI  
- Verification of cross-browser compatibility and keyboard accessibility  

---

# 📂 Repository Structure

```text
DiseaseSense/
│
├── Disease_Prediction_Model_Training.ipynb # Jupyter notebook for model training & EDA
├── requirements.txt                         # Python dependencies
├── pyvenv.cfg                               # Virtual environment configuration
├── README.md                                # Project documentation
│
├── static/                                  # Root static brand assets
│   ├── Favicon.webp
│   └── Logo.webp
│
└── app/                                     # Django Application Root
    ├── manage.py                            # Django management script
    ├── model.joblib                         # Trained Logistic Regression model
    ├── Training.csv                         # Dataset used for features & training
    ├── db.sqlite3                           # SQLite database
    ├── requirements.txt                     # Application requirements
    ├── retrain_model.py                     # Script to retrain model if needed
    │
    ├── static/                              # App static assets
    │   ├── Favicon.webp
    │   └── Logo.webp
    │
    ├── templates/
    │   └── index.html                       # Single-page frontend template & UI script
    │
    └── backend/                             # Django backend configuration & logic
        ├── __init__.py
        ├── settings.py                      # App settings & static paths
        ├── urls.py                          # URL routes & static asset serving
        ├── views.py                         # Prediction logic, DDx, and triage routing
        ├── wsgi.py                          # WSGI deployment entry point
        └── asgi.py                          # ASGI entry point
```

---

# 📸 Project Snapshots

| Screenshot | Description |
|------------|-------------|
| ![Home Page](Snapshots/home.jpg) | Symptom input interface |
| ![Prediction Result](Snapshots/result.jpg) | Predicted disease output |

---

# 🧠 Skills Demonstrated

- Machine Learning model development  
- Data preprocessing & cleaning  
- Exploratory Data Analysis (EDA)  
- Classification algorithms implementation  
- Model evaluation & comparison  
- Django web application integration  
- Backend prediction systems  
- Data visualization techniques  
- Real-time ML inference workflow  

---

# skills demo - 2

# 🧠 Key Skills & Concepts Demonstrated

- Machine Learning classification & model evaluation  
- Data preprocessing, vectorization, and feature engineering  
- Model serialization using Joblib (`.joblib`)  
- Full-stack web application development with Django  
- RESTful AJAX communication & JSON payload structure  
- Differential diagnosis (DDx) & clinical triage system design  
- Responsive UI design, custom CSS animations, and SVG visualization  
- Real-time ML inference & production error handling  

---

# 🔐 Project Note & Disclaimer

> **Educational Disclaimer**: DiseaseSense is an AI-assisted educational tool designed to provide general medical information and symptom evaluation. It does not replace professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for official medical guidance. In case of emergency, contact local emergency services immediately (e.g., 112 / 108).

---
