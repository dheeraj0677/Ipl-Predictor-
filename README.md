# 🏏 IPL 2026 Match Predictor

<p align="center">
  <img src="https://img.shields.io/badge/IPL-2026-blue?style=for-the-badge&logo=cricket&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-0.115.0-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/ML-Custom%20Model-orange?style=for-the-badge" />
</p>

> A full-stack web application that predicts IPL 2026 match outcomes using a custom machine learning model trained on **10 seasons of historical IPL data (2016–2025)**.

---

## 📸 Preview

The app features a premium dark-themed UI showing:
- 🔴 **Today's Match** with live win probability bars
- 📅 **Upcoming Fixtures** with predictions for each match
- 📊 **Team Standings** based on historical performance
- ⚔️ **Head-to-Head Stats** between any two teams

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🤖 ML Predictions | Custom weighted model — H2H, team form, recent results, venue |
| 📅 Full IPL 2026 Schedule | Complete official fixture list with venues |
| 📊 Team Standings | Win rates calculated from 2016–2025 data |
| ⚔️ H2H Stats | Head-to-head records between all teams |
| 🏟️ Venue Analysis | Team performance broken down by venue |
| 🎯 Confidence Score | Each prediction displays a confidence % |

---

## 🧠 How the Model Works

The prediction engine uses a **weighted scoring algorithm** — no external ML libraries required!

```
Score = H2H (30%) + Overall Win Rate (20%) + Recent Form (30%) + Venue Win Rate (20%)
```

- **H2H (30%)** — Historical head-to-head win ratio
- **Overall Form (20%)** — All-time win rate (2016–2025)
- **Recent Form (30%)** — Last 5 matches performance
- **Venue Advantage (20%)** — Win rate at the specific match venue

Probabilities are normalized and a confidence % is returned alongside the predicted winner.

---

## 🗂️ Project Structure

```
IPL/
├── backend/
│   ├── app.py              # FastAPI application & API routes
│   ├── model.py            # ML prediction engine + historical data
│   ├── schedule.py         # IPL 2026 full schedule, teams, venues
│   ├── generate_schedule.py# Schedule utility/generation script
│   ├── check.py            # Quick sanity check script
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html          # Main UI page
│   ├── style.css           # Dark-mode premium styling
│   └── script.js           # API calls & dynamic rendering
└── README.md
```

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip

### 1. Clone the Repository
```bash
git clone https://github.com/dheeraj0677/Ipl-Predictor-.git
cd Ipl-Predictor-
```

### 2. Install Dependencies
```bash
pip install -r backend/requirements.txt
```

### 3. Run the Backend Server
```bash
cd backend
python app.py
```

The server starts at **http://localhost:8000**

### 4. Open the App
Navigate to **http://localhost:8000** in your browser — the frontend is served automatically.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves the frontend UI |
| `GET` | `/api/today` | Today's match with prediction |
| `GET` | `/api/upcoming?limit=10` | Upcoming matches with predictions |
| `GET` | `/api/schedule` | Full IPL 2026 schedule |
| `GET` | `/api/predict?team1=MI&team2=CSK&venue=Mumbai` | Predict a custom matchup |
| `GET` | `/api/stats?team1=MI&team2=CSK` | Head-to-head statistics |
| `GET` | `/api/standings` | Team standings by win rate |
| `GET` | `/api/teams` | All team info (name, color, abbreviation) |

### Example Response — `/api/predict?team1=MI&team2=CSK&venue=Mumbai`
```json
{
  "prediction": {
    "team1": "MI",
    "team2": "CSK",
    "venue": "Mumbai",
    "team1_probability": 58.3,
    "team2_probability": 41.7,
    "predicted_winner": "MI",
    "confidence": 58.3,
    "model_accuracy": 68.0
  },
  "h2h": {
    "total_matches": 14,
    "team1_wins": 8,
    "team2_wins": 6,
    "team1_win_pct": 57.1,
    "team2_win_pct": 42.9
  }
}
```

---

## 🏟️ Teams Covered

| Abbreviation | Team Name |
|---|---|
| MI | Mumbai Indians |
| CSK | Chennai Super Kings |
| RCB | Royal Challengers Bengaluru |
| KKR | Kolkata Knight Riders |
| SRH | Sunrisers Hyderabad |
| DC | Delhi Capitals |
| RR | Rajasthan Royals |
| PBKS | Punjab Kings |
| GT | Gujarat Titans |
| LSG | Lucknow Super Giants |

---

## 📊 Data

- **Training Data:** 200+ IPL matches from **2016 to 2025**
- **Features Used:** Season, Team 1, Team 2, Winner, Venue, Toss Winner, Toss Decision
- **No external datasets needed** — data is fully embedded in `model.py`

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/) |
| ML Engine | Custom Python (no scikit-learn / pandas) |
| Frontend | HTML5, CSS3 (Vanilla), JavaScript (Vanilla) |
| API Docs | Auto-generated at `/docs` (Swagger UI) |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Dheeraj**  
GitHub: [@dheeraj0677](https://github.com/dheeraj0677)

---

<p align="center">Made with ❤️ for cricket fans 🏏</p>
