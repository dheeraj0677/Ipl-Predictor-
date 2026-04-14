"""
IPL 2026 Match Prediction API
FastAPI backend serving ML predictions
"""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from model import IPLPredictor
from schedule import (
    IPL_2026_SCHEDULE, TEAMS, TEAM_COLORS, VENUES,
    get_today_matches, get_upcoming_matches, get_all_matches
)

app = FastAPI(title="IPL 2026 Predictor", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize predictor
print("Training ML model...")
predictor = IPLPredictor()
print("Model ready!")

# Serve frontend
frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_dir):
    app.mount("/static", StaticFiles(directory=frontend_dir), name="static")


from fastapi.responses import RedirectResponse

@app.get("/")
async def serve_index():
    return RedirectResponse(url="/static/index.html")


@app.get("/api/today")
async def get_today():
    """Get today's match(es) with prediction."""
    matches = get_today_matches()
    results = []
    for m in matches:
        prediction = predictor.predict(m["team1"], m["team2"], m["venue"])
        h2h = predictor.get_h2h_stats(m["team1"], m["team2"])
        results.append({
            "match": m,
            "prediction": prediction,
            "h2h": h2h,
            "team1_full": TEAMS.get(m["team1"], m["team1"]),
            "team2_full": TEAMS.get(m["team2"], m["team2"]),
            "team1_color": TEAM_COLORS.get(m["team1"], "#ffffff"),
            "team2_color": TEAM_COLORS.get(m["team2"], "#ffffff"),
            "venue_full": VENUES.get(m["venue"], m["venue"]),
        })
    return {"today": results, "date": __import__('datetime').date.today().isoformat()}


@app.get("/api/predict")
async def predict_match(
    team1: str = Query(..., description="Team 1 abbreviation"),
    team2: str = Query(..., description="Team 2 abbreviation"),
    venue: str = Query("Mumbai", description="Venue city")
):
    """Predict a specific match outcome."""
    prediction = predictor.predict(team1, team2, venue)
    h2h = predictor.get_h2h_stats(team1, team2)
    return {
        "prediction": prediction,
        "h2h": h2h,
        "team1_full": TEAMS.get(team1, team1),
        "team2_full": TEAMS.get(team2, team2),
        "team1_color": TEAM_COLORS.get(team1, "#ffffff"),
        "team2_color": TEAM_COLORS.get(team2, "#ffffff"),
    }


@app.get("/api/schedule")
async def get_schedule():
    """Get full schedule with predictions."""
    matches = get_all_matches()
    results = []
    for m in matches:
        prediction = predictor.predict(m["team1"], m["team2"], m["venue"])
        results.append({
            "match": m,
            "prediction": prediction,
            "team1_full": TEAMS.get(m["team1"], m["team1"]),
            "team2_full": TEAMS.get(m["team2"], m["team2"]),
            "team1_color": TEAM_COLORS.get(m["team1"], "#ffffff"),
            "team2_color": TEAM_COLORS.get(m["team2"], "#ffffff"),
            "venue_full": VENUES.get(m["venue"], m["venue"]),
        })
    return {"schedule": results}


@app.get("/api/upcoming")
async def get_upcoming(limit: int = Query(10, description="Number of upcoming matches")):
    """Get upcoming matches with predictions."""
    matches = get_upcoming_matches(limit)
    results = []
    for m in matches:
        prediction = predictor.predict(m["team1"], m["team2"], m["venue"])
        results.append({
            "match": m,
            "prediction": prediction,
            "team1_full": TEAMS.get(m["team1"], m["team1"]),
            "team2_full": TEAMS.get(m["team2"], m["team2"]),
            "team1_color": TEAM_COLORS.get(m["team1"], "#ffffff"),
            "team2_color": TEAM_COLORS.get(m["team2"], "#ffffff"),
            "venue_full": VENUES.get(m["venue"], m["venue"]),
        })
    return {"upcoming": results}


@app.get("/api/stats")
async def get_stats(
    team1: str = Query(..., description="Team 1 abbreviation"),
    team2: str = Query(..., description="Team 2 abbreviation"),
):
    """Get head-to-head and team statistics."""
    h2h = predictor.get_h2h_stats(team1, team2)
    return {
        "h2h": h2h,
        "team1_full": TEAMS.get(team1, team1),
        "team2_full": TEAMS.get(team2, team2),
        "team1_color": TEAM_COLORS.get(team1, "#ffffff"),
        "team2_color": TEAM_COLORS.get(team2, "#ffffff"),
    }


@app.get("/api/standings")
async def get_standings():
    """Get team standings based on historical performance."""
    stats = predictor.get_team_stats()
    for s in stats:
        s["full_name"] = TEAMS.get(s["team"], s["team"])
        s["color"] = TEAM_COLORS.get(s["team"], "#ffffff")
    return {"standings": stats}


@app.get("/api/teams")
async def get_teams():
    """Get all team info."""
    teams_list = []
    for abbr, name in TEAMS.items():
        teams_list.append({
            "abbr": abbr,
            "name": name,
            "color": TEAM_COLORS.get(abbr, "#ffffff"),
        })
    return {"teams": teams_list}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
