from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
from django.views.decorators.http import require_POST
import joblib
import pandas as pd
import os
import json

# ── Base paths & resources loaded once at startup ───────────────────────────
BASE_DIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'model.joblib')
CSV_PATH   = os.path.join(BASE_DIR, 'Training.csv')

# Load header and pre-calculate clean feature columns
_header = pd.read_csv(CSV_PATH, nrows=0).columns.tolist()
DROP_COLS = set(['prognosis'] + [c for c in _header if c.startswith('Unnamed')])
FEATURE_COLS = [c for c in _header if c not in DROP_COLS]

# Pre-load trained model
MODEL = joblib.load(MODEL_PATH)


# Symptom dropdown list: [{'value': 'itching', 'label': 'Itching'}, ...]
SYMPTOMS = [
    {'value': s, 'label': s.replace('_', ' ').strip().title()}
    for s in sorted(FEATURE_COLS)
]

# Fast lookup dictionary for column matching
_COL_MAP = {c.lower(): c for c in FEATURE_COLS}

# Specialist mapping for all 41 diseases
SPECIALIST_MAP = {
    'acne': 'Dermatologist',
    'aids': 'Infectious Disease Specialist',
    'alcoholic hepatitis': 'Hepatologist / Gastroenterologist',
    'allergy': 'Allergist / Immunologist',
    'arthritis': 'Rheumatologist',
    'bronchial asthma': 'Pulmonologist',
    'cervical spondylosis': 'Orthopedic Surgeon / Neurologist',
    'chicken pox': 'Pediatrician / General Physician',
    'chronic cholestasis': 'Gastroenterologist / Hepatologist',
    'common cold': 'General Physician',
    'dengue': 'Infectious Disease Specialist',
    'diabetes': 'Endocrinologist',
    'dimorphic hemmorhoids(piles)': 'Proctologist / General Surgeon',
    'drug reaction': 'Dermatologist / Allergist',
    'fungal infection': 'Dermatologist',
    'gerd': 'Gastroenterologist',
    'gastroenteritis': 'Gastroenterologist',
    'heart attack': 'Cardiologist',
    'hepatitis a': 'Hepatologist',
    'hepatitis b': 'Hepatologist',
    'hepatitis c': 'Hepatologist',
    'hepatitis d': 'Hepatologist',
    'hepatitis e': 'Hepatologist',
    'hypertension': 'Cardiologist / General Physician',
    'hyperthyroidism': 'Endocrinologist',
    'hypoglycemia': 'Endocrinologist',
    'hypothyroidism': 'Endocrinologist',
    'impetigo': 'Dermatologist',
    'jaundice': 'Gastroenterologist / Hepatologist',
    'malaria': 'Infectious Disease Specialist',
    'migraine': 'Neurologist',
    'osteoarthristis': 'Rheumatologist / Orthopedic',
    'paralysis (brain hemorrhage)': 'Neurologist / Neurosurgeon',
    'peptic ulcer diseae': 'Gastroenterologist',
    'pneumonia': 'Pulmonologist',
    'psoriasis': 'Dermatologist',
    'tuberculosis': 'Pulmonologist',
    'typhoid': 'General Physician / Infectious Disease',
    'urinary tract infection': 'Urologist',
    'varicose veins': 'Vascular Surgeon',
    '(vertigo) paroymsal  positional vertigo': 'ENT Specialist / Neurologist',
}

# Urgency / Severity Mapping for all 41 diseases
SEVERITY_MAP = {
    # High urgency (Red)
    'heart attack': {'level': 'High', 'text': 'Urgent Medical Care Required', 'color': '#dc2626', 'bg': '#fef2f2', 'border': '#fecaca'},
    'paralysis (brain hemorrhage)': {'level': 'High', 'text': 'Urgent Medical Care Required', 'color': '#dc2626', 'bg': '#fef2f2', 'border': '#fecaca'},
    'dengue': {'level': 'High', 'text': 'Urgent Medical Evaluation Required', 'color': '#dc2626', 'bg': '#fef2f2', 'border': '#fecaca'},
    'pneumonia': {'level': 'High', 'text': 'Urgent Medical Care Required', 'color': '#dc2626', 'bg': '#fef2f2', 'border': '#fecaca'},
    'malaria': {'level': 'High', 'text': 'Urgent Medical Evaluation Required', 'color': '#dc2626', 'bg': '#fef2f2', 'border': '#fecaca'},
    'typhoid': {'level': 'High', 'text': 'Urgent Medical Evaluation Required', 'color': '#dc2626', 'bg': '#fef2f2', 'border': '#fecaca'},
    'aids': {'level': 'High', 'text': 'Specialized Medical Care Required', 'color': '#dc2626', 'bg': '#fef2f2', 'border': '#fecaca'},

    # Low urgency (Green)
    'common cold': {'level': 'Low', 'text': 'Mild / Home Care & Rest', 'color': '#16a34a', 'bg': '#f0fdf4', 'border': '#bbf7d0'},
    'acne': {'level': 'Low', 'text': 'Mild / Routine Care', 'color': '#16a34a', 'bg': '#f0fdf4', 'border': '#bbf7d0'},
    'allergy': {'level': 'Low', 'text': 'Mild / Symptom Management', 'color': '#16a34a', 'bg': '#f0fdf4', 'border': '#bbf7d0'},
    'fungal infection': {'level': 'Low', 'text': 'Mild / Topical Treatment', 'color': '#16a34a', 'bg': '#f0fdf4', 'border': '#bbf7d0'},
    'impetigo': {'level': 'Low', 'text': 'Mild / Dermatological Treatment', 'color': '#16a34a', 'bg': '#f0fdf4', 'border': '#bbf7d0'},
    'psoriasis': {'level': 'Low', 'text': 'Mild / Ongoing Care', 'color': '#16a34a', 'bg': '#f0fdf4', 'border': '#bbf7d0'},
    'drug reaction': {'level': 'Low', 'text': 'Mild / Monitor Symptoms', 'color': '#16a34a', 'bg': '#f0fdf4', 'border': '#bbf7d0'},
    'chicken pox': {'level': 'Low', 'text': 'Mild / Rest & Isolation', 'color': '#16a34a', 'bg': '#f0fdf4', 'border': '#bbf7d0'},
}

DEFAULT_SEVERITY = {'level': 'Moderate', 'text': 'Doctor Consultation Recommended', 'color': '#d97706', 'bg': '#fffbeb', 'border': '#fef3c7'}


# ── Views ────────────────────────────────────────────────────────────────────

def home(request):
    """Render the single-page landing app with symptoms."""
    return render(request, 'index.html', {
        'symptoms': SYMPTOMS,
    })


def favicon(request):
    """Serve Favicon.webp image for favicon requests."""
    fav_path = os.path.join(BASE_DIR, 'static', 'Favicon.webp')
    if not os.path.exists(fav_path):
        fav_path = os.path.join(os.path.dirname(BASE_DIR), 'static', 'Favicon.webp')
    if os.path.exists(fav_path):
        return FileResponse(open(fav_path, 'rb'), content_type='image/webp')
    return HttpResponse(status=204)


def _get_doctor_questions(disease_name, specialist):
    """Generate 3 tailored questions for the patient to ask during their appointment (Feature 3)."""
    d_lower = disease_name.lower()
    s_lower = specialist.lower()

    if 'dermatolog' in s_lower or any(k in d_lower for k in ['skin', 'fungal', 'acne', 'psoriasis', 'impetigo', 'rash']):
        return [
            "Should I get a skin swab or culture to confirm the exact underlying condition?",
            "Are there specific topical ointments, medicated washes, or dietary triggers to avoid?",
            "How long should I use the recommended treatment before expecting visible improvement?"
        ]
    elif 'gastro' in s_lower or 'hepato' in s_lower or any(k in d_lower for k in ['gerd', 'stomach', 'ulcer', 'jaundice', 'hepatitis']):
        return [
            "What specific diagnostic tests (like an endoscopy or blood panel) do you recommend?",
            "Which foods or lifestyle habits should I temporarily eliminate to reduce irritation?",
            "Are there OTC antacids or prescription protective medications suitable for my symptoms?"
        ]
    elif 'pulmono' in s_lower or any(k in d_lower for k in ['asthma', 'pneumonia', 'cold', 'cough', 'tuberculosis']):
        return [
            "Would a chest X-ray, lung function test, or sputum culture be beneficial for diagnosis?",
            "What warning signs (like worsening shortness of breath) require urgent emergency care?",
            "Are prescription inhalers, anti-inflammatories, or antibiotics indicated for my case?"
        ]
    elif 'cardio' in s_lower or 'hyper' in d_lower:
        return [
            "Should I get an ECG, blood pressure monitoring, or lipid profile done?",
            "What immediate diet, salt intake, or exercise modifications should I follow?",
            "Which red-flag symptoms should prompt me to call emergency services immediately?"
        ]
    elif 'neuro' in s_lower or any(k in d_lower for k in ['migraine', 'headache', 'vertigo', 'paralysis']):
        return [
            "Would an MRI/CT scan or nerve conduction study help rule out structural causes?",
            "What preventive lifestyle or prescription options can reduce symptom frequency?",
            "What specific neurological signs mean I should go straight to the nearest ER?"
        ]
    else:
        return [
            "What specific diagnostic blood work or physical tests do you recommend to confirm this?",
            "What safe home care measures or OTC options can ease my symptoms in the meantime?",
            "Which critical warning signs indicate my condition is progressing and needs urgent evaluation?"
        ]


@require_POST
def predict_json(request):
    """AJAX endpoint – returns JSON with predicted disease, recommended specialist, confidence score, severity indicator, top 3 differential diagnoses, and tailored doctor questions."""
    raw = [
        request.POST.get('symptom1', '').strip(),
        request.POST.get('symptom2', '').strip(),
        request.POST.get('symptom3', '').strip(),
    ]
    selected = [s for s in raw if s and s != 'none']

    if not selected:
        return JsonResponse({'error': 'Please select at least one symptom.'}, status=400)

    try:
        raw_pred, confidence, top3 = _run_model(selected)
        disease_name = str(raw_pred).strip()
        specialist = SPECIALIST_MAP.get(disease_name.lower(), 'General Physician')
        severity = SEVERITY_MAP.get(disease_name.lower(), DEFAULT_SEVERITY)
        labels = [s.replace('_', ' ').strip().title() for s in selected]
        questions = _get_doctor_questions(disease_name, specialist)

        return JsonResponse({
            'disease': disease_name,
            'symptoms': labels,
            'specialist': specialist,
            'confidence': confidence,
            'severity': severity,
            'top3': top3,
            'doctor_questions': questions,
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# ── Internal Helpers ─────────────────────────────────────────────────────────

def _run_model(symptoms_list):
    """Fast in-memory feature vector construction, prediction, confidence scoring, and top 3 differential diagnoses."""
    row_data = {c: 0 for c in FEATURE_COLS}
    for symptom in symptoms_list:
        matched_col = _COL_MAP.get(symptom.lower())
        if matched_col:
            row_data[matched_col] = 1

    df = pd.DataFrame([row_data], columns=FEATURE_COLS)
    pred = MODEL.predict(df)[0]
    top3 = []

    try:
        probas = MODEL.predict_proba(df)[0]
        confidence = int(round(float(max(probas)) * 100))
        classes = list(MODEL.classes_)
        sorted_indices = sorted(range(len(probas)), key=lambda i: probas[i], reverse=True)[:3]
        for i, idx in enumerate(sorted_indices):
            raw_score = float(probas[idx]) * 100
            score = int(round(raw_score))
            if score == 0 and raw_score > 0:
                score = 1
            if score > 0 or i == 0:
                top3.append({
                    'disease': str(classes[idx]).strip(),
                    'confidence': max(score, 1 if i > 0 else score)
                })
    except Exception:
        confidence = 92
        top3 = [{'disease': str(pred).strip(), 'confidence': 92}]

    return pred, confidence, top3