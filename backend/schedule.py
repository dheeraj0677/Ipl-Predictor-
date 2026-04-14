"""
IPL 2026 Schedule Data - All announced fixtures
"""
from datetime import date

# Team abbreviations and full names
TEAMS = {
    "CSK": "Chennai Super Kings",
    "MI": "Mumbai Indians",
    "RCB": "Royal Challengers Bengaluru",
    "KKR": "Kolkata Knight Riders",
    "DC": "Delhi Capitals",
    "SRH": "Sunrisers Hyderabad",
    "RR": "Rajasthan Royals",
    "PBKS": "Punjab Kings",
    "GT": "Gujarat Titans",
    "LSG": "Lucknow Super Giants",
}

TEAM_COLORS = {
    "CSK": "#FFCB05",
    "MI": "#004BA0",
    "RCB": "#EC1C24",
    "KKR": "#3A225D",
    "DC": "#17479E",
    "SRH": "#FF822A",
    "RR": "#EA1A85",
    "PBKS": "#DD1F2D",
    "GT": "#1C1C1C",
    "LSG": "#A72056",
}

VENUES = {
    "Bengaluru": "M. Chinnaswamy Stadium, Bengaluru",
    "Mumbai": "Wankhede Stadium, Mumbai",
    "Kolkata": "Eden Gardens, Kolkata",
    "Chennai": "MA Chidambaram Stadium, Chennai",
    "Delhi": "Arun Jaitley Stadium, Delhi",
    "Hyderabad": "Rajiv Gandhi International Cricket Stadium, Hyderabad",
    "Ahmedabad": "Narendra Modi Stadium, Ahmedabad",
    "Lucknow": "Ekana Cricket Stadium, Lucknow",
    "Jaipur": "Sawai Mansingh Stadium, Jaipur",
    "Mullanpur": "New PCA Stadium, Mullanpur",
    "New Chandigarh": "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh",
    "Guwahati": "ACA Stadium, Guwahati",
    "Dharamshala": "HPCA Cricket Stadium, Dharamshala",
    "Raipur": "Nava Raipur Cricket Stadium, Raipur",
}

# IPL 2026 Schedule - Phase 1 & Phase 2 (all announced matches)
IPL_2026_SCHEDULE = [
    # ===== Matches 1-11 (already played) =====
    {"match": 1,  "date": "2026-03-28", "team1": "DC",   "team2": "CSK",  "venue": "Delhi",         "time": "15:30"},
    {"match": 2,  "date": "2026-03-28", "team1": "KKR",  "team2": "RR",   "venue": "Kolkata",        "time": "19:30"},
    {"match": 3,  "date": "2026-03-29", "team1": "PBKS", "team2": "DC",   "venue": "New Chandigarh", "time": "15:30"},
    {"match": 4,  "date": "2026-03-29", "team1": "RCB",  "team2": "MI",   "venue": "Bengaluru",      "time": "19:30"},
    {"match": 5,  "date": "2026-03-30", "team1": "DC",   "team2": "GT",   "venue": "Delhi",          "time": "19:30"},
    {"match": 6,  "date": "2026-03-31", "team1": "SRH",  "team2": "MI",   "venue": "Hyderabad",      "time": "19:30"},
    {"match": 7,  "date": "2026-04-01", "team1": "CSK",  "team2": "RCB",  "venue": "Chennai",        "time": "19:30"},
    {"match": 8,  "date": "2026-04-02", "team1": "SRH",  "team2": "RR",   "venue": "Hyderabad",      "time": "19:30"},
    {"match": 9,  "date": "2026-04-03", "team1": "SRH",  "team2": "LSG",  "venue": "Hyderabad",      "time": "19:30"},
    {"match": 10, "date": "2026-04-04", "team1": "SRH",  "team2": "DC",   "venue": "Hyderabad",      "time": "15:30"},
    {"match": 11, "date": "2026-04-04", "team1": "CSK",  "team2": "PBKS", "venue": "Chennai",        "time": "19:30"},
    # ===== Official Schedule (from iplt20.com images) =====
    {"match": 12, "date": "2026-04-06", "team1": "KKR",  "team2": "PBKS", "venue": "Kolkata",        "time": "19:30"},
    {"match": 13, "date": "2026-04-07", "team1": "RR",   "team2": "MI",   "venue": "Guwahati",       "time": "19:30"},
    {"match": 14, "date": "2026-04-08", "team1": "DC",   "team2": "GT",   "venue": "Delhi",          "time": "19:30"},
    {"match": 15, "date": "2026-04-09", "team1": "KKR",  "team2": "LSG",  "venue": "Kolkata",        "time": "19:30"},
    {"match": 16, "date": "2026-04-10", "team1": "RR",   "team2": "RCB",  "venue": "Guwahati",       "time": "19:30"},
    {"match": 17, "date": "2026-04-11", "team1": "PBKS", "team2": "SRH",  "venue": "New Chandigarh", "time": "15:30"},
    {"match": 18, "date": "2026-04-11", "team1": "CSK",  "team2": "DC",   "venue": "Chennai",        "time": "19:30"},
    {"match": 19, "date": "2026-04-12", "team1": "LSG",  "team2": "GT",   "venue": "Lucknow",        "time": "15:30"},
    {"match": 20, "date": "2026-04-12", "team1": "MI",   "team2": "RCB",  "venue": "Mumbai",         "time": "19:30"},
    {"match": 21, "date": "2026-04-13", "team1": "SRH",  "team2": "RR",   "venue": "Hyderabad",      "time": "19:30"},
    {"match": 22, "date": "2026-04-14", "team1": "CSK",  "team2": "KKR",  "venue": "Chennai",        "time": "19:30"},
    {"match": 23, "date": "2026-04-15", "team1": "RCB",  "team2": "LSG",  "venue": "Bengaluru",      "time": "19:30"},
    {"match": 24, "date": "2026-04-16", "team1": "MI",   "team2": "PBKS", "venue": "Mumbai",         "time": "19:30"},
    {"match": 25, "date": "2026-04-17", "team1": "GT",   "team2": "KKR",  "venue": "Ahmedabad",      "time": "19:30"},
    {"match": 26, "date": "2026-04-18", "team1": "RCB",  "team2": "DC",   "venue": "Bengaluru",      "time": "15:30"},
    {"match": 27, "date": "2026-04-18", "team1": "SRH",  "team2": "CSK",  "venue": "Hyderabad",      "time": "19:30"},
    {"match": 28, "date": "2026-04-19", "team1": "KKR",  "team2": "RR",   "venue": "Kolkata",        "time": "15:30"},
    {"match": 29, "date": "2026-04-19", "team1": "PBKS", "team2": "LSG",  "venue": "New Chandigarh", "time": "19:30"},
    {"match": 30, "date": "2026-04-20", "team1": "GT",   "team2": "MI",   "venue": "Ahmedabad",      "time": "19:30"},
    {"match": 31, "date": "2026-04-21", "team1": "SRH",  "team2": "DC",   "venue": "Hyderabad",      "time": "19:30"},
    {"match": 32, "date": "2026-04-22", "team1": "LSG",  "team2": "RR",   "venue": "Lucknow",        "time": "19:30"},
    {"match": 33, "date": "2026-04-23", "team1": "MI",   "team2": "CSK",  "venue": "Mumbai",         "time": "19:30"},
    {"match": 34, "date": "2026-04-24", "team1": "RCB",  "team2": "GT",   "venue": "Bengaluru",      "time": "19:30"},
    {"match": 35, "date": "2026-04-25", "team1": "DC",   "team2": "PBKS", "venue": "Delhi",          "time": "15:30"},
    {"match": 36, "date": "2026-04-25", "team1": "RR",   "team2": "SRH",  "venue": "Jaipur",         "time": "19:30"},
    {"match": 37, "date": "2026-04-26", "team1": "GT",   "team2": "CSK",  "venue": "Ahmedabad",      "time": "15:30"},
    {"match": 38, "date": "2026-04-26", "team1": "LSG",  "team2": "KKR",  "venue": "Lucknow",        "time": "19:30"},
    {"match": 39, "date": "2026-04-27", "team1": "DC",   "team2": "RCB",  "venue": "Delhi",          "time": "19:30"},
    {"match": 40, "date": "2026-04-28", "team1": "PBKS", "team2": "RR",   "venue": "New Chandigarh", "time": "19:30"},
    {"match": 41, "date": "2026-04-29", "team1": "MI",   "team2": "SRH",  "venue": "Mumbai",         "time": "19:30"},
    {"match": 42, "date": "2026-04-30", "team1": "GT",   "team2": "RCB",  "venue": "Ahmedabad",      "time": "19:30"},
    {"match": 43, "date": "2026-05-01", "team1": "RR",   "team2": "DC",   "venue": "Jaipur",         "time": "19:30"},
    {"match": 44, "date": "2026-05-02", "team1": "CSK",  "team2": "MI",   "venue": "Chennai",        "time": "19:30"},
    {"match": 45, "date": "2026-05-03", "team1": "SRH",  "team2": "KKR",  "venue": "Hyderabad",      "time": "15:30"},
    {"match": 46, "date": "2026-05-03", "team1": "GT",   "team2": "PBKS", "venue": "Ahmedabad",      "time": "19:30"},
    {"match": 47, "date": "2026-05-04", "team1": "MI",   "team2": "LSG",  "venue": "Mumbai",         "time": "19:30"},
    {"match": 48, "date": "2026-05-05", "team1": "DC",   "team2": "CSK",  "venue": "Delhi",          "time": "19:30"},
    {"match": 49, "date": "2026-05-06", "team1": "SRH",  "team2": "PBKS", "venue": "Hyderabad",      "time": "19:30"},
    {"match": 50, "date": "2026-05-07", "team1": "LSG",  "team2": "RCB",  "venue": "Lucknow",        "time": "19:30"},
    {"match": 51, "date": "2026-05-08", "team1": "DC",   "team2": "KKR",  "venue": "Delhi",          "time": "19:30"},
    {"match": 52, "date": "2026-05-09", "team1": "RR",   "team2": "GT",   "venue": "Jaipur",         "time": "19:30"},
    {"match": 53, "date": "2026-05-10", "team1": "CSK",  "team2": "LSG",  "venue": "Chennai",        "time": "15:30"},
    {"match": 54, "date": "2026-05-10", "team1": "RCB",  "team2": "MI",   "venue": "Raipur",         "time": "19:30"},
    {"match": 55, "date": "2026-05-11", "team1": "PBKS", "team2": "DC",   "venue": "Dharamshala",    "time": "19:30"},
    {"match": 56, "date": "2026-05-12", "team1": "GT",   "team2": "SRH",  "venue": "Ahmedabad",      "time": "19:30"},
    {"match": 57, "date": "2026-05-13", "team1": "RCB",  "team2": "KKR",  "venue": "Raipur",         "time": "19:30"},
    {"match": 58, "date": "2026-05-14", "team1": "PBKS", "team2": "MI",   "venue": "Dharamshala",    "time": "19:30"},
    {"match": 59, "date": "2026-05-15", "team1": "LSG",  "team2": "CSK",  "venue": "Lucknow",        "time": "19:30"},
    {"match": 60, "date": "2026-05-16", "team1": "KKR",  "team2": "GT",   "venue": "Kolkata",        "time": "19:30"},
    {"match": 61, "date": "2026-05-17", "team1": "PBKS", "team2": "RCB",  "venue": "Dharamshala",    "time": "15:30"},
    {"match": 62, "date": "2026-05-17", "team1": "DC",   "team2": "RR",   "venue": "Delhi",          "time": "19:30"},
    {"match": 63, "date": "2026-05-18", "team1": "CSK",  "team2": "SRH",  "venue": "Chennai",        "time": "19:30"},
    {"match": 64, "date": "2026-05-19", "team1": "RR",   "team2": "LSG",  "venue": "Jaipur",         "time": "19:30"},
    {"match": 65, "date": "2026-05-20", "team1": "KKR",  "team2": "MI",   "venue": "Kolkata",        "time": "19:30"},
    {"match": 66, "date": "2026-05-21", "team1": "CSK",  "team2": "GT",   "venue": "Chennai",        "time": "19:30"},
    {"match": 67, "date": "2026-05-22", "team1": "SRH",  "team2": "RCB",  "venue": "Hyderabad",      "time": "19:30"},
    {"match": 68, "date": "2026-05-23", "team1": "LSG",  "team2": "PBKS", "venue": "Lucknow",        "time": "19:30"},
    {"match": 69, "date": "2026-05-24", "team1": "MI",   "team2": "RR",   "venue": "Mumbai",         "time": "15:30"},
    {"match": 70, "date": "2026-05-24", "team1": "KKR",  "team2": "DC",   "venue": "Kolkata",        "time": "19:30"},
    # ===== Playoffs (TBD) =====
    {"match": 71, "date": "2026-05-26", "team1": "TBD",  "team2": "TBD",  "venue": "Ahmedabad",      "time": "19:30"},
    {"match": 72, "date": "2026-05-27", "team1": "TBD",  "team2": "TBD",  "venue": "Ahmedabad",      "time": "19:30"},
    {"match": 73, "date": "2026-05-29", "team1": "TBD",  "team2": "TBD",  "venue": "Ahmedabad",      "time": "19:30"},
    {"match": 74, "date": "2026-05-31", "team1": "TBD",  "team2": "TBD",  "venue": "Ahmedabad",      "time": "19:30"},
]


def get_today_matches():
    """Get today's matches from the schedule."""
    today = date.today().isoformat()
    return [m for m in IPL_2026_SCHEDULE if m["date"] == today and m["team1"] != "TBD"]


def get_upcoming_matches(limit=10):
    """Get upcoming matches from today onwards."""
    today = date.today().isoformat()
    upcoming = [m for m in IPL_2026_SCHEDULE if m["date"] > today and m["team1"] != "TBD"]
    return upcoming[:limit]


def get_all_matches():
    """Return all non-TBD matches."""
    return [m for m in IPL_2026_SCHEDULE if m["team1"] != "TBD"]
