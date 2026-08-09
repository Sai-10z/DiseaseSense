# 🧬 DiseaseSense – AI-Powered Clinical Symptom Analysis System

DiseaseSense is a machine learning-powered clinical web application that analyzes user-reported symptoms and predicts potential diseases through an intelligent diagnostic pipeline. Built with **Python**, **Django**, and **Scikit-Learn**, the application combines predictive analytics with an intuitive single-page interface to help users better understand their symptoms before consulting a healthcare professional.

Unlike conventional disease prediction projects that simply output a predicted class, DiseaseSense transforms machine learning predictions into actionable healthcare guidance by integrating:

- 🧠 AI-powered Disease Prediction
- 📊 Top 3 Differential Diagnoses (DDx)
- 🚦 Clinical Urgency Assessment
- 🩺 Specialist Recommendation
- 📍 Nearby Doctor Search
- 📋 Appointment Preparation Checklist
- ❓ Personalized Consultation Questions

The prediction engine was trained on **132 clinical symptoms** spanning **41 disease classes**. After evaluating multiple supervised learning algorithms, **Logistic Regression** was selected as the production model due to its interpretability, computational efficiency, and fast real-time inference.

> **⚠️ Disclaimer:** DiseaseSense is an educational project designed to demonstrate Machine Learning and Full-Stack Development concepts. It is **not** intended to replace professional medical advice, diagnosis, or treatment.
---

# 🚀 Tech Stack

| Category | Technologies |
|----------|--------------|
| **Programming Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **Machine Learning** | ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikitlearn&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) ![Joblib](https://img.shields.io/badge/Joblib-FFCC00?style=flat) |
| **Backend** | ![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) |
| **Data Visualization** | Matplotlib, Seaborn |
| **Development Tools** | Jupyter Notebook, VS Code |
| **Dataset** | Training.csv (132 Symptoms • 41 Diseases) |
| **Model Storage** | Joblib (`model.joblib`) |

---

# 🏗️ Workflow & Prediction Pipeline

```text
👤 User Selects Symptoms
        │
        ▼
🔎 Interactive Searchable Symptom Input
        │
        ▼
⚡ Django Backend (Request Processing & Feature Vectorization)
        │
        ▼
🧠 Logistic Regression Prediction Model (`model.joblib`)
        │
        ▼
📊 Probability Estimation (`predict_proba`)
        │
        ▼
📋 Clinical Intelligence Engine
        ├── 🎯 Primary Disease Prediction
        ├── 📊 Top 3 Differential Diagnoses (DDx)
        ├── 🚦 Clinical Urgency Assessment
        ├── 🩺 Specialist Recommendation
        ├── 📍 Nearby Doctor Search
        ├── ❓ Personalized Consultation Questions
        └── 📑 Appointment Preparation Checklist
        │
        ▼
🌐 Interactive Results Dashboard
```
---

# ✨ Core Features

## 🧠 Machine Learning & Clinical Intelligence

- **Multi-Model Evaluation** – Trained and evaluated multiple classification algorithms, including Logistic Regression, K-Nearest Neighbors, Naïve Bayes, Decision Tree, Random Forest, and Gradient Boosting.
- **Production-Ready Prediction Engine** – Deploys a serialized **Logistic Regression** model (`model.joblib`) for fast, lightweight, real-time inference.
- **Optimized Feature Vectorization** – Converts user-selected symptoms into a **132-dimensional binary feature vector** aligned with the training dataset.
- **Differential Diagnosis (DDx)** – Returns the **Top 3 most probable diseases** ranked by prediction confidence instead of a single diagnosis.
- **Clinical Urgency Assessment** – Automatically categorizes predictions into **High**, **Moderate**, or **Low** severity levels.
- **Specialist Recommendation Engine** – Maps predicted diseases to the most appropriate medical specialists, including Dermatologists, Cardiologists, Neurologists, Pulmonologists, and more.
- **Consultation Question Generator** – Generates personalized questions to help patients prepare for medical appointments.

---

## 🌐 Interactive Web Application

- **Single-Page Application (SPA)** with smooth navigation between Hero, Symptom Input, Results, and Consultation Guidance sections.
- **Searchable Symptom Selection** supporting up to **three symptoms** with live progress indicators.
- **Real-Time Disease Prediction** powered by asynchronous Django backend requests.
- **Dynamic Form Validation** with user-friendly error handling and submission feedback.
- **Responsive Design** optimized for desktop, tablet, and mobile devices.

---

## 📊 Clinical Visualization & User Experience

- **Animated SVG Confidence Donut Chart** displaying prediction confidence using smooth scroll-triggered animations.
- **Rank-Based Differential Diagnosis Cards** with distinct color coding for Top 3 predictions.
- **Clinical Severity Badges** using intuitive visual indicators for urgency assessment.
- **Modern Healthcare UI** featuring glassmorphism, responsive layouts, custom animations, and structured visual hierarchy.

---

## 🩺 Healthcare Assistance Features

- **Nearby Specialist Locator** with direct Google Maps integration.
- **Appointment Preparation Checklist** helping users organize symptoms, medications, and medical history before visiting a physician.
- **Emergency Support Banner** displaying emergency contact numbers (**112 / 108**) for high-risk conditions.
- **Educational Medical Disclaimer** encouraging professional medical consultation and responsible use.

---

# 🧪 Machine Learning Models & Evaluation

DiseaseSense was developed using a supervised multi-class classification approach to predict diseases from symptom-based feature vectors. Multiple machine learning algorithms were trained, evaluated, and compared before selecting the final production model.

## 📊 Model Performance Comparison

| Model | Accuracy (%) |
|--------------------------|-------------:|
| Logistic Regression | **100.00** |
| K-Nearest Neighbors (KNN) | **100.00** |
| Naïve Bayes | **100.00** |
| Decision Tree | 97.62 |
| Random Forest | 97.62 |
| Gradient Boosting | 97.62 |

---

## 🏆 Production Model Selection

Although several algorithms achieved excellent validation accuracy, **Logistic Regression** was selected as the production model based on its overall engineering advantages rather than accuracy alone.

### Why Logistic Regression?

- High mathematical interpretability
- Fast real-time inference
- Low memory footprint
- Strong generalization for binary symptom vectors
- Low computational overhead
- Easy deployment using Joblib serialization
- Well-suited for healthcare decision support applications where explainability is important

---

# ⚙️ Development Workflow

The development of **DiseaseSense** followed a structured workflow, beginning with data exploration and model development before progressing to backend integration, frontend implementation, and user experience enhancements.

## 📌 Phase 1 – Data Analysis & Model Development

- Explored and analyzed the clinical symptom dataset (`Training.csv`)
- Performed data preprocessing and feature engineering
- Conducted Exploratory Data Analysis (EDA)
- Trained and evaluated multiple classification algorithms
- Compared model performance using accuracy metrics
- Selected **Logistic Regression** as the production model
- Serialized the trained model using **Joblib** (`model.joblib`)

## 📌 Phase 2 – Backend Development

- Built the application using the **Django** framework
- Implemented request routing and view logic
- Developed the prediction pipeline for symptom vectorization
- Integrated the trained ML model with the backend
- Implemented probability scoring using `predict_proba()`
- Developed the Differential Diagnosis (DDx) engine
- Added clinical urgency classification
- Implemented specialist recommendation logic
- Configured static asset management for deployment

## 📌 Phase 3 – Frontend Development

- Designed a modern single-page user interface
- Developed searchable symptom selection components
- Added dynamic form validation and error handling
- Built an animated SVG confidence donut chart
- Designed color-coded Differential Diagnosis cards
- Integrated Google Maps specialist search
- Added responsive layouts for desktop and mobile devices

## 📌 Phase 4 – Testing & Refinement

- Verified prediction accuracy across multiple test cases
- Tested frontend responsiveness on different screen sizes
- Optimized user interactions and interface animations
- Improved accessibility and navigation flow
- Refined UI consistency and visual hierarchy
- Validated end-to-end prediction workflow

---

# 📂 Repository Structure

```text
DiseaseSense/
│
├── Disease_Prediction_Model_Training.ipynb   # ML training, EDA & model evaluation
├── requirements.txt                          # Project dependencies
├── README.md                                 # Project documentation
│
├── static/                                   # Global static assets
│   ├── Logo.webp
│   └── Favicon.webp
│
└── app/
    ├── manage.py                             # Django management script
    ├── model.joblib                          # Trained Logistic Regression model
    ├── Training.csv                          # Clinical symptom dataset
    ├── retrain_model.py                      # Model retraining utility
    ├── db.sqlite3                            # Development database
    │
    ├── backend/
    │   ├── settings.py                       # Django configuration
    │   ├── urls.py                           # Application routes
    │   ├── views.py                          # Prediction pipeline & business logic
    │   ├── wsgi.py                           # WSGI entry point
    │   └── asgi.py                           # ASGI entry point
    │
    ├── templates/
    │   └── index.html                        # Single-page application interface
    │
    └── static/
        ├── Logo.webp
        └── Favicon.webp
```
---

# 📸 Project Snapshots

The following screenshots highlight the complete DiseaseSense workflow—from symptom selection and AI-powered disease prediction to personalized clinical guidance and specialist recommendations.

| **Home & Symptom Selection** | **Disease Prediction Results** |
|:----------------------------:|:------------------------------:|
| <img src="screenshots/home.webp" alt="Home & Symptom Selection" width="100%"> | <img src="screenshots/symptoms.webp" alt="Disease Prediction Results" width="100%"> |
| Search and select up to **three symptoms** using interactive, filterable dropdowns with real-time validation and live progress indicators. | View the **predicted disease**, animated confidence score, **Top 3 Differential Diagnoses (DDx)**, and clinical urgency assessment. |

---

| **Clinical Guidance** | **Specialist Recommendation** |
|:---------------------:|:-----------------------------:|
| <img src="screenshots/result.webp" alt="Clinical Guidance" width="100%"> | <img src="screenshots/consult.webp" alt="Specialist Recommendation" width="100%"> |
| Receive a personalized consultation checklist along with dynamically generated questions to help prepare for your medical appointment. | Discover the recommended medical specialist, access Google Maps for nearby doctors, and view emergency guidance for high-risk conditions. |

---
# 🧠 Skills Demonstrated

### 🤖 Machine Learning

- Supervised Machine Learning
- Multi-Class Classification
- Model Training & Evaluation
- Feature Engineering & Vectorization
- Probability Estimation using `predict_proba()`
- Model Selection & Performance Comparison
- Model Serialization with Joblib

---

### 📊 Data Analysis

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Correlation Analysis
- Data Visualization
- Clinical Dataset Interpretation

---

### 🌐 Full-Stack Web Development

- Django Web Framework
- RESTful Backend Development
- Asynchronous AJAX Requests
- JSON Data Exchange
- Static Asset Management
- Responsive Single-Page Application (SPA)

---

### 🎨 Frontend Development

- HTML5, CSS3 & Vanilla JavaScript
- Responsive UI Design
- DOM Manipulation
- SVG-Based Data Visualization
- CSS Animations & Micro-Interactions
- User Experience (UX) Design

---

### 🏥 System Design & Software Engineering

- End-to-End ML System Integration
- Clinical Decision Support Workflow
- Differential Diagnosis (DDx) Design
- Urgency & Severity Classification
- Specialist Recommendation System
- Error Handling & Input Validation
- Modular Application Architecture

---

### 💡 Professional Skills

- Problem Solving
- Analytical Thinking
- Software Debugging
- Technical Documentation
- Model Deployment
- Full Project Lifecycle Development

---

# 🚀 Future Enhancements

- User authentication and patient profiles
- Medical history tracking
- PDF report generation
- AI-powered symptom explanation using LLMs
- Voice-based symptom input
- Cloud deployment using AWS
- Docker containerization
- CI/CD pipeline integration
- Doctor appointment booking
- Electronic Health Record (EHR) integration

---

# ⚠️ Project Disclaimer

> **Educational Purpose Only**
>
> DiseaseSense is an AI-assisted educational and research project developed to demonstrate the application of **Machine Learning**, **Data Analysis**, and **Full-Stack Web Development** in healthcare. The predictions, clinical guidance, and recommendations generated by the system are intended solely for learning and demonstration purposes.

### Important Notice

- This application **does not provide medical advice, diagnosis, or treatment**.
- Disease predictions are generated using a machine learning model trained on a predefined symptom dataset and **should not be considered clinically accurate or definitive**.
- Users should always consult a **licensed healthcare professional** for medical evaluation, diagnosis, and treatment.
- In case of a medical emergency, immediately contact your local emergency services or visit the nearest healthcare facility.

---

### Academic Use

DiseaseSense was developed as an academic project to explore:

- Machine Learning for Healthcare
- Clinical Decision Support Systems
- Django-based Full-Stack Development
- Human-Centered UI/UX Design
- Data Visualization & Predictive Analytics

This project is intended to showcase technical implementation and software engineering practices rather than serve as a certified medical application.

---

# 🙏 Acknowledgements

This project was developed as part of my Machine Learning journey to explore how predictive analytics can be combined with modern web technologies to build interactive healthcare applications.

Special thanks to the open-source Python ecosystem, including:

- Python
- Django
- Scikit-Learn
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

Their tools and documentation made the development of this project possible.

---
