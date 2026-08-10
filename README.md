<<<<<<< HEAD
# 🧬 DiseaseSense – Machine Learning Symptom Analysis System

DiseaseSense is a machine learning web application built with **Python**, **Django**, and **Scikit-Learn** that predicts potential diseases based on user-selected symptoms.
It combines a trained machine learning model with simple clinical guidance to help users better understand their symptoms before consulting a healthcare professional.

### ✨ Highlights

- Disease prediction
- Top 3 predicted conditions
- Confidence Score
- Urgency assessment
- Specialist recommendation
- Nearby specialist search
- Appointment preparation checklist
- Suggested questions for the doctor

The prediction model was trained on a dataset containing **132 symptoms** across **41 disease classes**. After comparing multiple machine learning algorithms, **Logistic Regression** was selected for its speed, interpretability, and consistent performance.
=======
# 🧬 DiseaseSense – ML Based Disease Prediction System

A Django-based clinical web application that predicts potential medical conditions from user-reported symptoms using machine learning. The system provides an end-to-end healthcare guidance pipeline, including multi-model evaluation, differential diagnosis (DDx), clinical urgency triage, specialist routing, tailored doctor interview preparation, and real-time prediction through a modern single-page interface.

Logistic Regression was selected as the primary production model for its high interpretability, low risk of overfitting, and rapid inference capability.
>>>>>>> f2c4774 (Initial commit: DiseaseSense ML Prediction App with Django SPA interface, DDx, and clinical guidance)

---

# 🚀 Tech Stack

<<<<<<< HEAD
| Category | Technologies |
|----------|--------------|
| **Programming Language** | Python |
| **Backend** | Django |
| **Machine Learning** | Scikit-Learn, Pandas, NumPy |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Data Visualization** | Matplotlib, Seaborn |
| **Model Serialization** | Joblib |
| **Development Tools** | Jupyter Notebook, VS Code, Git |
| **Dataset** | `Training.csv` (132 Symptoms • 41 Disease Classes) |
=======
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

```text
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
>>>>>>> f2c4774 (Initial commit: DiseaseSense ML Prediction App with Django SPA interface, DDx, and clinical guidance)

---

# ✨ Core Features

<<<<<<< HEAD
DiseaseSense combines machine learning predictions with simple clinical guidance to help users better understand their symptoms.

| Feature | Description |
|---------|-------------|
| Disease Prediction | Predicts possible diseases from selected symptoms. |
| Top 3 Predictions | Displays the three most probable conditions. |
| Confidence Score | Shows the model's confidence for the primary prediction. |
| Urgency Indicator | Categorizes conditions as High, Moderate, or Low urgency. |
| Specialist Recommendation | Suggests the most relevant medical specialist. |
| Nearby Specialist Search | Opens Google Maps to find nearby specialists. |
| Appointment Checklist | Helps users prepare before visiting a doctor. |
| Consultation Questions | Suggests useful questions to ask during the consultation. |

---

# 📸 Project Screenshots

The screenshots below demonstrate the complete DiseaseSense workflow, from the initial landing page and symptom selection to machine learning results and personalized care guidance.

| **Home / Landing Page** | **Symptom Analysis** |
| :---: | :---: |
| ![DiseaseSense Home](screenshots/home.png) | ![DiseaseSense Symptom Analysis](screenshots/symptoms.png) |
| The landing page introduces DiseaseSense and allows users to begin a symptom assessment. | Users can select up to three symptoms through interactive searchable fields before running the analysis. |

| **Analysis Results** | **Care Guidance & Specialist Recommendation** |
| :---: | :---: |
| ![DiseaseSense Analysis Results](screenshots/results.png) | ![DiseaseSense Care Guidance](screenshots/consult.png) |
| Displays the predicted condition, model confidence, reported symptoms, and Top 3 model predictions. | Provides specialist recommendations, appointment preparation guidance, consultation questions, and emergency-care guidance. |

---

# 🏗️ Workflow & Prediction Pipeline

The following workflow shows how user input moves through the prediction pipeline before the final results are displayed.

```text
👤 User Selects Symptoms
        │
        ▼
🔍 Symptom Validation & Processing
        │
        ▼
⚙️ Feature Vectorization
(132-Symptom Feature Space)
        │
        ▼
🧠 Logistic Regression Model
(model.joblib)
        │
        ▼
📊 Probability Estimation
(predict_proba)
        │
        ▼
🎯 Prediction Ranking
 ├── Primary Prediction
 └── Top 3 Model Predictions
        │
        ▼
🩺 Clinical Guidance
 ├── Urgency Assessment
 ├── Specialist Recommendation
 ├── Nearby Specialist Search
 ├── Appointment Checklist
 └── Consultation Questions
        │
        ▼
🌐 Results Interface
```

---

# 🧪 Machine Learning Models & Evaluation

DiseaseSense uses supervised multi-class classification to predict diseases from symptom-based feature vectors.

Multiple machine learning models were trained and compared before selecting the final model for the application.

## 📊 Model Performance Comparison

| Model                         |    Accuracy |
| ----------------------------- | ----------: |
| **Logistic Regression**       | **100.00%** |
| **K-Nearest Neighbors (KNN)** | **100.00%** |
| **Naïve Bayes**               | **100.00%** |
| Decision Tree                 |      97.62% |
| Random Forest                 |      97.62% |
| Gradient Boosting             |      97.62% |

> **Important:** These results were obtained using the project's dataset and evaluation methodology. They do **not** represent real-world clinical diagnostic accuracy and should not be interpreted as medical reliability.

## 🏆 Selected Model

Although Logistic Regression, KNN, and Naïve Bayes achieved the highest accuracy, **Logistic Regression** was chosen for deployment because it offers:

- Fast inference
- Good interpretability
- Low computational overhead
- Efficient model storage with Joblib
- Native probability estimation using `predict_proba()`

The trained model is saved as `model.joblib` and loaded by the Django application for real-time predictions.

---

## 🛠️ Implementation Highlights

The project includes the following key components:

- Performed data preprocessing and exploratory data analysis (EDA).
- Trained and compared multiple machine learning models.
- Deployed the Logistic Regression model using Joblib.
- Built the prediction pipeline for real-time inference.
- Used `predict_proba()` to rank the Top 3 predicted conditions.
- Integrated the model with a Django backend.
- Designed a responsive single-page interface.
- Added specialist recommendations and consultation support.
- Integrated Google Maps for nearby specialists.
- Included medical disclaimers and emergency information.
=======
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
>>>>>>> f2c4774 (Initial commit: DiseaseSense ML Prediction App with Django SPA interface, DDx, and clinical guidance)

---

# 📂 Repository Structure

```text
DiseaseSense/
│
<<<<<<< HEAD
├── Disease_Prediction_Model_Training.ipynb   Model training and evaluation
├── README.md                                 # Project documentation
├── requirements.txt                          # Python dependencies
├── screenshots/                              # Application screenshots
│   ├── home.png
│   ├── symptoms.png
│   ├── results.png
│   └── consult.png
│
└── app/
    ├── manage.py                             # Django management script
    ├── Training.csv                          # Training dataset
    ├── model.joblib                          # Serialized ML model
    ├── retrain_model.py                      # Model retraining utility
    │
    ├── backend/
    │   ├── settings.py                       # Django configuration
    │   ├── urls.py                           # URL routing
    │   ├── views.py                          # Prediction logic
    │   ├── wsgi.py                           # WSGI entry point
    │   └── asgi.py                           # ASGI entry point
    │
    ├── templates/
    │   └── index.html                        # Main application interface
    │
    └── static/
        ├── Logo.webp                         # Application logo
        └── Favicon.webp                      # Browser favicon
=======
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
>>>>>>> f2c4774 (Initial commit: DiseaseSense ML Prediction App with Django SPA interface, DDx, and clinical guidance)
```

---

<<<<<<< HEAD
# 🚀 Getting Started

Follow the steps below to set up and run DiseaseSense locally.

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/DiseaseSense.git
cd DiseaseSense
```

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Navigate to the Django Application

```bash
cd app
```

## 5️⃣ Start the Development Server

```bash
python manage.py runserver
```

## 6️⃣ Open the Application

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

The application should now be running locally.

---

# 🔮 Future Enhancements

Some features planned for future versions of DiseaseSense include:

- Explainable AI (XAI) to show how symptoms influence predictions
- Symptom tracking to monitor changes over time
- AI-powered health assistant for follow-up queries
- Downloadable clinical summary reports
- Multi-language support
- Enhanced prediction models using ensemble learning
- Integration with healthcare APIs for improved specialist information

---

# ⚙️ Current Limitations

DiseaseSense is an educational project and has the following limitations:

- The model is trained on a single symptom dataset and has **not** been clinically validated.
- Users can currently select a maximum of **three symptoms**, which does not reflect real clinical assessments.
- High accuracy on the project dataset does **not** guarantee similar performance in real-world medical scenarios.
- The application does not consider patient history, age, medications, laboratory results, or other clinical factors.
- Urgency levels and specialist recommendations are based on predefined application logic rather than medical validation.
- Nearby specialist search depends on external map services.

---

# ⚠️ Disclaimer

DiseaseSense is an educational Machine Learning project developed for learning and demonstration purposes. The predictions and guidance provided by this application are **not** intended to replace professional medical advice, diagnosis, or treatment.
Always consult a qualified healthcare professional for medical concerns. In case of a medical emergency, contact your local emergency services immediately.

---
=======
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
>>>>>>> f2c4774 (Initial commit: DiseaseSense ML Prediction App with Django SPA interface, DDx, and clinical guidance)
