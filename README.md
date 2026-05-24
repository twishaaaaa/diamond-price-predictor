# 💎 Luminos — Diamond Price Predictor

A real-world Machine Learning web application that predicts diamond prices based on the 4 C's (Carat, Cut, Color, Clarity) and other physical characteristics.

---

## 🌐 Live Demo

| | Link |
|--|--|
| 🤖 **Live API** | [diamond-price-predictor.hf.space/docs](https://twishaaaaas-diamond-price-predictor.hf.space/docs) |
| 💎 **Frontend UI** | [GitHub Pages](https://twishaaaaa.github.io/diamond-price-predictor/frontend/diamond-price-predictor.html) |
| 📦 **GitHub Repo** | [twishaaaaa/diamond-price-predictor](https://github.com/twishaaaaa/diamond-price-predictor) |

---

## 📸 Screenshots

### 💎 Luminos Frontend
![Frontend](assets/frontend.png)

### 🎯 Price Prediction Result
![Result](assets/result.png)

### ⚡ Live API Docs
![API](assets/api.png)
---

## 🧠 What This Project Does

- User inputs diamond characteristics (carat, cut, color, clarity, polish, symmetry)
- A trained **Random Forest ML model** predicts the market price
- Returns predicted price + price range + confidence score
- Beautiful mobile-friendly UI built with vanilla HTML/CSS/JS

---

## 🏗️ Architecture

```
┌─────────────────────┐         ┌──────────────────────────┐
│   Luminos Frontend  │  HTTP   │   FastAPI Backend         │
│   (HTML/CSS/JS)     │ ──────► │   (Python)                │
│                     │  POST   │                           │
│  • Carat slider     │ /predict│  • Loads ML model         │
│  • Color picker     │ ◄─────  │  • Encodes features       │
│  • Clarity picker   │  JSON   │  • Returns prediction     │
│  • Cut selector     │         │                           │
└─────────────────────┘         └──────────────────────────┘
                                          │
                                          ▼
                                ┌──────────────────────────┐
                                │   Random Forest Model     │
                                │   (scikit-learn)          │
                                │                           │
                                │  • Trained on 53,940 rows │
                                │  • R² Score: ~0.98        │
                                │  • Features: 9 columns    │
                                └──────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **ML Model** | scikit-learn (Random Forest) | Price prediction |
| **Data** | pandas, numpy | Data processing |
| **Backend** | FastAPI + uvicorn | REST API |
| **Frontend** | HTML + CSS + JavaScript | User interface |
| **Deployment** | Hugging Face Spaces + Docker | Cloud hosting |
| **Version Control** | Git + GitHub | Code management |

---

## 📊 ML Model Details

- **Algorithm:** Random Forest Regressor
- **Dataset:** [Kaggle Diamonds Dataset](https://kaggle.com/datasets/shivam2503/diamonds) — 53,940 rows
- **Target:** `log(price)` — log transformation for better accuracy
- **R² Score:** ~0.98 (model explains 98% of price variance)
- **Features used:**

| Feature | Description | Encoding |
|---------|-------------|----------|
| carat | Diamond weight | Numeric |
| cut | Cut quality | Ordinal (1–5) |
| color | Color grade | Ordinal (1–7) |
| clarity | Clarity grade | Ordinal (1–9) |
| depth | Depth percentage | Numeric |
| table | Table percentage | Numeric |
| x, y, z | Physical dimensions | Numeric |

---

## 📁 Project Structure

```
diamond-price-predictor/
│
├── backend/
│   ├── main.py              ← FastAPI application
│   ├── train.py             ← ML model training script
│   ├── requirements.txt     ← Python dependencies
│   └── Dockerfile           ← Docker config for HF Spaces
│
├── frontend/
│   └── diamond-price-predictor.html  ← Luminos UI
│
├── notebooks/
│   └── diamond_model.ipynb  ← EDA + model training notebook
│
├── data/                    ← Dataset (not tracked in git)
└── .gitignore
```

---

## 🚀 Run Locally

### Prerequisites
- Python 3.11+
- pip

### Setup

```bash
# Clone the repo
git clone https://github.com/twishaaaaa/diamond-price-predictor.git
cd diamond-price-predictor

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r backend/requirements.txt
```

### Download Dataset

1. Go to [Kaggle Diamonds Dataset](https://kaggle.com/datasets/shivam2503/diamonds)
2. Download `diamonds.csv`
3. Place it in the `data/` folder

### Train the Model

```bash
cd backend
python train.py
```

### Start the API

```bash
cd backend
uvicorn main:app --reload
```

API will be live at: `http://localhost:8000/docs`

### Start the Frontend

```bash
cd frontend
python -m http.server 3000
```

Open: `http://localhost:3000/diamond-price-predictor.html`

---

## 📡 API Reference

### `POST /predict`

Predict the price of a diamond.

**Request Body:**
```json
{
  "carat": 1.0,
  "cut": 5,
  "color": 7,
  "clarity": 8,
  "depth": 61.7,
  "table": 57.0,
  "x": 6.4,
  "y": 6.4,
  "z": 3.9
}
```

**Response:**
```json
{
  "predicted_price": 5842,
  "range_low": 5083,
  "range_high": 6602,
  "currency": "USD"
}
```

### `GET /health`

Check if API is running.

```json
{
  "status": "online",
  "model": "Random Forest Diamond Predictor"
}
```

---

## 🎓 What I Learned

- **Data Analysis** — Explored 53,940 diamond records, identified skewed distributions, found outliers
- **Feature Engineering** — Applied log transformation, ordinal encoding for categorical variables
- **Machine Learning** — Trained and evaluated Random Forest vs Linear Regression, used cross-validation
- **API Development** — Built a production REST API with FastAPI and pydantic validation
- **Docker** — Containerized the application for cloud deployment
- **Cloud Deployment** — Deployed on Hugging Face Spaces with environment secrets

---

## 👤 Author

**Twisha**
- GitHub: [@twishaaaaa](https://github.com/twishaaaaa)
- Hugging Face: [@twishaaaaas](https://huggingface.co/twishaaaaas)

---

## 📄 License

This project is licensed under the MIT License.

---

> Built as part of an IT + AI/ML internship portfolio project 💎