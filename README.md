# 🧬 DiseaseSense – Machine Learning Symptom Analysis System

DiseaseSense is an end-to-end machine learning web application built with **Python, Django, and Scikit-Learn** that analyzes user-selected symptoms and generates ranked disease predictions.

The system combines a supervised machine learning model with a rule-based clinical guidance layer to transform symptom inputs into structured results, including:

- 🧠 **Disease Prediction**
- 📊 **Top 3 Model Predictions**
- 🎯 **Prediction Confidence**
- 🚦 **Clinical Urgency Guidance**
- 🩺 **Specialist Recommendation**
- 📍 **Nearby Specialist Search**
- 📋 **Appointment Preparation Guidance**
- ❓ **Consultation Questions**

The prediction engine was trained using **132 clinical symptoms across 41 disease classes**. Multiple supervised learning algorithms were evaluated, with **Logistic Regression** selected as the deployed application model because of its interpretability, computational efficiency, and fast inference.

DiseaseSense demonstrates the complete workflow of an applied ML system — from **data preprocessing and model training to prediction, backend integration, and user-facing clinical guidance**.

> **⚠️ Disclaimer:** DiseaseSense is an educational project developed to demonstrate Machine Learning and Full-Stack Web Development concepts. It is **not intended to provide medical diagnosis, treatment, or professional medical advice**.

---

# 🚀 Tech Stack

| Category | Technologies |
|---|---|
| **Programming Language** | Python |
| **Machine Learning** | Scikit-Learn, Pandas, NumPy, Joblib |
| **Backend** | Django |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Data Analysis & Visualization** | Pandas, Matplotlib, Seaborn |
| **Model Training** | Jupyter Notebook |
| **Model Serialization** | Joblib |
| **Development Tools** | VS Code, Git |
| **Dataset** | `Training.csv` — 132 Symptoms • 41 Disease Classes |

---

# ✨ Core Features

DiseaseSense combines machine learning prediction with application-level clinical guidance to provide a complete symptom analysis workflow.

| Feature | Description |
|---|---|
| 🧠 **Machine Learning Disease Prediction** | Predicts a potential condition from user-selected symptoms using a trained Logistic Regression classifier. |
| 📊 **Top 3 Model Predictions** | Uses model probability estimates to rank the three highest-scoring predicted conditions. |
| 🎯 **Prediction Confidence** | Visualizes the model's confidence for the primary prediction using an interactive confidence indicator. |
| 🚦 **Clinical Urgency Guidance** | Classifies predicted conditions into **High, Moderate, or Low** urgency categories using application-level logic. |
| 🩺 **Specialist Recommendation** | Maps the predicted condition to a relevant medical specialist for further evaluation. |
| 📍 **Nearby Specialist Search** | Provides Google Maps integration to help users locate nearby specialists. |
| 📋 **Appointment Preparation Checklist** | Provides practical information users can prepare before consulting a healthcare professional. |
| ❓ **Consultation Questions** | Generates condition-specific questions that users can discuss with their healthcare professional. |
| 🔍 **Interactive Symptom Selection** | Provides searchable symptom selectors with validation and support for selecting up to three symptoms. |
| 📱 **Responsive User Interface** | Provides a responsive interface covering the complete workflow from symptom selection to care guidance. |
| ⚠️ **Medical Safety Guidance** | Displays appropriate disclaimers and emergency-care guidance rather than presenting predictions as medical diagnoses. |

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

DiseaseSense follows an end-to-end prediction workflow that connects user symptom input with the trained machine learning model and application-level clinical guidance.

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
🩺 Application Guidance Layer
 ├── 🚦 Urgency Assessment
 ├── 🩺 Specialist Recommendation
 ├── 📍 Nearby Specialist Search
 ├── 📋 Appointment Checklist
 └── ❓ Consultation Questions
        │
        ▼
🌐 Interactive Results Interface
```

---

# 🧪 Machine Learning Models & Evaluation

DiseaseSense uses a supervised multi-class classification approach to predict potential diseases from symptom-based feature vectors.

Multiple classification algorithms were trained and evaluated on the project dataset before selecting the model used by the web application.

## 📊 Model Performance Comparison

| Model | Accuracy |
|---|---:|
| **Logistic Regression** | **100.00%** |
| **K-Nearest Neighbors (KNN)** | **100.00%** |
| **Naïve Bayes** | **100.00%** |
| Decision Tree | 97.62% |
| Random Forest | 97.62% |
| Gradient Boosting | 97.62% |

> **⚠️ Important:** These accuracy results were obtained using the project's dataset and evaluation methodology. The dataset is a benchmark-style symptom/disease dataset and these results **do not represent real-world clinical diagnostic accuracy**. The reported performance should not be interpreted as evidence that the model can reliably diagnose diseases in clinical settings.

## 🏆 Selected Model

Although Logistic Regression, KNN, and Naïve Bayes achieved the highest accuracy on the evaluation dataset, **Logistic Regression was selected as the application model**.

The selection was based on:

- **High predictive performance** on the evaluation dataset
- **Interpretability** compared with more complex models
- **Fast inference** for real-time web requests
- **Low computational overhead**
- **Efficient model storage and loading** using Joblib
- **Native probability estimation** through `predict_proba()`

The trained Logistic Regression model is serialized as: model.joblib

---

# 🛠️ What I Built

DiseaseSense was developed as an end-to-end Machine Learning and Full-Stack Web Development project.

The implementation includes:

- 📊 **Dataset Analysis & Preprocessing** — Explored and prepared the symptom/disease dataset for supervised classification.
- 🧪 **Model Training & Evaluation** — Trained and compared multiple classification algorithms including Logistic Regression, KNN, Naïve Bayes, Decision Tree, Random Forest, and Gradient Boosting.
- 🏆 **Model Selection** — Evaluated model performance and selected Logistic Regression for application deployment.
- 💾 **Model Serialization** — Saved the trained model using Joblib for integration with the Django application.
- ⚙️ **Prediction Pipeline** — Built the backend pipeline that converts selected symptoms into the feature representation required by the model and performs real-time inference.
- 📊 **Probability-Based Ranking** — Used `predict_proba()` to generate and rank the Top 3 model predictions.
- 🌐 **Django Integration** — Connected the trained ML model with a Django backend to process prediction requests.
- 🎨 **Frontend Development** — Built the responsive user interface for symptom selection, analysis results, and care guidance.
- 🚦 **Guidance Logic** — Implemented application-level urgency classification and specialist mapping based on predicted conditions.
- 📍 **Healthcare Search Integration** — Added Google Maps integration for finding nearby specialists.
- 📋 **Consultation Support** — Implemented appointment preparation checklists and condition-specific consultation questions.
- ⚠️ **Safety Messaging** — Added medical disclaimers and emergency-care guidance to ensure predictions are presented as educational information rather than professional diagnosis.

---

# 📂 Repository Structure

```text
DiseaseSense/
│
├── Disease_Prediction_Model_Training.ipynb   # Model training, EDA & evaluation
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
    │   ├── views.py                          # Prediction pipeline & application logic
    │   ├── wsgi.py                           # WSGI entry point
    │   └── asgi.py                           # ASGI entry point
    │
    ├── templates/
    │   └── index.html                        # Main application interface
    │
    └── static/
        ├── Logo.webp                         # Application logo
        └── Favicon.webp                      # Browser favicon
```

---

# 🚀 Getting Started

Follow the steps below to set up and run DiseaseSense locally.

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/DiseaseSense.git
cd DiseaseSense
```

---

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

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Navigate to the Django Application

```bash
cd app
```

---

## 5️⃣ Start the Development Server

```bash
python manage.py runserver
```

---

## 6️⃣ Open the Application

Visit the following URL in your browser:

```text
http://127.0.0.1:8000/
```

The DiseaseSense web application should now be running locally.

---

# 🔮 Future Enhancements

Future versions of DiseaseSense could improve the system's reliability, explainability, and overall functionality through:

- 🧠 **Explainable AI (XAI)** — Use techniques such as SHAP to show which symptoms contribute most to each prediction.
- 📊 **Model Validation & Calibration** — Introduce cross-validation, probability calibration, and evaluation on additional datasets.
- 🔍 **Improved Symptom Processing** — Support symptom synonyms, variations in user input, and more flexible symptom descriptions.
- 📈 **Symptom Progression Tracking** — Allow users to record symptoms over time and monitor changes between assessments.
- 🧬 **Expanded Risk Assessment** — Explore additional models and ensemble approaches for broader disease-risk analysis.
- 🌍 **Multi-Language Support** — Allow users to interact with the application in multiple languages.
- 📄 **Clinical Summary Export** — Generate downloadable summaries containing symptoms, predictions, and consultation notes for discussion with a healthcare professional.
- 👤 **User Accounts & History** — Allow users to securely save previous assessments and track symptom history.
- 🤖 **AI-Powered Follow-Up Assistant** — Add conversational follow-up interactions while maintaining clear safety boundaries.
- 🔗 **Healthcare API Integration** — Explore integration with verified healthcare/provider services for more reliable specialist and appointment information.

---

# ⚠️ Project Limitations & Considerations

DiseaseSense is an educational machine learning application and has several important limitations:

- **Dataset Dependence** — Model performance depends heavily on the quality, structure, and distribution of the training dataset.
- **Limited Symptom Input** — The current application supports a maximum of three selected symptoms, which does not represent the full complexity of real clinical assessments.
- **Dataset Generalization** — High evaluation accuracy on the project dataset does not guarantee similar performance on unseen, real-world patient data.
- **No Clinical Validation** — The model has not been clinically validated and should not be used for medical diagnosis or treatment decisions.
- **Model Confidence ≠ Diagnostic Certainty** — Probability scores generated by the model represent statistical estimates and should not be interpreted as medical certainty.
- **Rule-Based Guidance** — Urgency levels, specialist recommendations, and consultation guidance are application-level logic and are not generated or medically validated by the machine learning model.
- **No Patient History** — The current system does not consider important clinical factors such as age, medical history, medications, examination findings, laboratory results, or imaging.
- **External Service Dependency** — Nearby specialist search relies on external map/search services and may depend on their availability and accuracy.

These limitations are important when interpreting DiseaseSense results and highlight areas for future development and validation.

---

# ⚠️ Project Disclaimer

DiseaseSense is an **educational Machine Learning and Full-Stack Web Development project** created to demonstrate the practical integration of data analysis, supervised learning, backend development, and interactive web interfaces.

The predictions generated by DiseaseSense are based on a machine learning model trained on the project's dataset and **have not been clinically validated**.

The results, confidence scores, urgency classifications, specialist recommendations, and other guidance provided by the application:

- Are intended for **educational and demonstration purposes only**.
- **Do not constitute medical diagnosis or professional medical advice.**
- Should not be used to make decisions about treatment, medication, or other healthcare actions.
- Should not be interpreted as medically validated diagnostic probabilities.

Users should consult a **qualified healthcare professional** for medical concerns. If you believe you are experiencing a medical emergency, seek immediate assistance from your local emergency services or the nearest appropriate healthcare facility.

---

