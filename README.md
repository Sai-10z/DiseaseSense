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

---

# 🚀 Tech Stack

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

---

# ✨ Core Features

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

📸 Project Snapshots

The snapshots below demonstrate the complete DiseaseSense workflow, from the initial landing page and symptom selection to machine learning results and personalized care guidance.

1. 🏠 Home / Landing Page

The landing page introduces DiseaseSense and allows users to begin a symptom assessment.

<p align="center"> <img src="./Snapshots/home.png" alt="DiseaseSense Home / Landing Page" width="1000"> </p>

2. 🩺 Symptom Analysis

Users can select up to three symptoms through interactive searchable fields before running the analysis.

<p align="center"> <img src="./Snapshots/symptoms.png" alt="DiseaseSense Symptom Analysis" width="1000"> </p>

3. 📊 Analysis Results

Displays the predicted condition, model confidence, reported symptoms, and Top 3 model predictions.

<p align="center"> <img src="./Snapshots/results.png" alt="DiseaseSense Analysis Results" width="1000"> </p>

4. 👨‍⚕️ Care Guidance & Specialist Recommendation

Provides specialist recommendations, appointment preparation guidance, consultation questions, and emergency-care guidance.

<p align="center"> <img src="./Snapshots/consult.png" alt="DiseaseSense Care Guidance and Specialist Recommendation" width="1000"> </p>

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

---

# 📂 Repository Structure

```text
DiseaseSense/
│
├── Disease_Prediction_Model_Training.ipynb   Model training and evaluation
├── README.md                                 # Project documentation
├── requirements.txt                          # Python dependencies
├── Snapshots/                              # Application Snapshots
│   ├── home.jpg
│   ├── symptoms.jpg
│   ├── results.jpg
│   └── consult.jpg
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
        ├── Logo.jpg                         # Application logo
        └── Favicon.jpg                      # Browser favicon
```

---

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
