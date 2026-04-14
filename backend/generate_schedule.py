import random
import json
import re
from datetime import datetime, timedelta

def generate_schedule():
    # Groups for 2024 format:
    group_a = ["MI", "KKR", "RR", "DC", "LSG"]
    group_b = ["CSK", "SRH", "RCB", "PBKS", "GT"]
    venues = {
        "CSK": "Chennai", "MI": "Mumbai", "RCB": "Bengaluru", "KKR": "Kolkata",
        "DC": "Delhi", "SRH": "Hyderabad", "RR": "Jaipur", "PBKS": "Mullanpur",
        "GT": "Ahmedabad", "LSG": "Lucknow"
    }

    matches = []
    
    for i in range(len(group_a)):
        for j in range(len(group_b)):
            matches.append((group_a[i], group_b[j]))
            matches.append((group_b[j], group_a[i]))
            
    for i in range(len(group_a)):
        for j in range(i+1, len(group_a)):
            matches.append((group_a[i], group_a[j]))
            
    for i in range(len(group_b)):
        for j in range(i+1, len(group_b)):
            matches.append((group_b[i], group_b[j]))

    random.seed(111)
    # Simple backtracking to assign dates
    start_date = datetime(2026, 3, 28)
    
    # We have 70 matches. Let's make a list of available slots:
    # Double headers on Saturday and Sunday
    slots = []
    curr_date = start_date
    while len(slots) < 70:
        if curr_date.weekday() >= 5:
            slots.append({"date": curr_date, "time": "15:30"})
            slots.append({"date": curr_date, "time": "19:30"})
        else:
            slots.append({"date": curr_date, "time": "19:30"})
        curr_date += timedelta(days=1)
    
    slots = slots[:70] # Just in case
    
    # Now assign matches to slots
    # condition: no team can play twice on the same day
    
    def solve(match_idx, assigned):
        if match_idx == 70:
            return assigned
            
        for i in range(len(matches)):
            # Try to place matches[i] in slots[match_idx]
            match_teams = matches[i]
            slot_date = slots[match_idx]["date"]
            
            # Check if either team already plays on slot_date in assigned
            conflict = False
            for prev_m, prev_s in assigned:
                if prev_s["date"] == slot_date:
                    if prev_m[0] in match_teams or prev_m[1] in match_teams:
                        conflict = True
                        break
            
            # Check if either team is playing on consecutive days? Not strict, but let's just make sure no same day
            if conflict: continue
            
            # Use it
            new_matches = matches[:]
            new_matches.pop(i)
            matches.clear()
            matches.extend(new_matches)
            
            assigned.append((match_teams, slots[match_idx]))
            
            res = solve(match_idx + 1, assigned)
            if res is not None:
                return res
            
            # backtrack
            matches.insert(i, match_teams)
            assigned.pop()
            
        return None

    # Sort matches somehow or randomize to avoid deterministic stuck?
    random.shuffle(matches)
    
    solution = solve(0, [])
    if not solution:
        print("Failed to schedule")
        return
        
    schedule_data = []
    match_id = 1
    for m, slot in solution:
        schedule_data.append({
            "match": match_id,
            "date": slot["date"].strftime("%Y-%m-%d"),
            "team1": m[0], "team2": m[1],
            "venue": venues[m[0]], "time": slot["time"]
        })
        match_id += 1
        
    # Add playoffs
    last_date = solution[-1][1]["date"]
    
    curr_date = last_date + timedelta(days=2) 
    schedule_data.append({
        "match": match_id, "date": curr_date.strftime("%Y-%m-%d"),
        "team1": "TBD", "team2": "TBD", "venue": "Chennai", "time": "19:30"
    })
    match_id += 1
    curr_date += timedelta(days=1)
    schedule_data.append({
        "match": match_id, "date": curr_date.strftime("%Y-%m-%d"),
        "team1": "TBD", "team2": "TBD", "venue": "Ahmedabad", "time": "19:30"
    })
    match_id += 1
    curr_date += timedelta(days=2)
    schedule_data.append({
        "match": match_id, "date": curr_date.strftime("%Y-%m-%d"),
        "team1": "TBD", "team2": "TBD", "venue": "Chennai", "time": "19:30"
    })
    match_id += 1
    curr_date += timedelta(days=2)
    schedule_data.append({
        "match": match_id, "date": curr_date.strftime("%Y-%m-%d"),
        "team1": "TBD", "team2": "TBD", "venue": "Ahmedabad", "time": "19:30"
    })
    
    # Format the string
    res = "IPL_2026_SCHEDULE = [\n"
    for item in schedule_data:
        res += f"    {json.dumps(item)},\n"
    res += "]\n"

    # read schedule.py and replace
    with open("schedule.py", "r") as f:
        content = f.read()
        
    content = re.sub(r'IPL_2026_SCHEDULE\s*=\s*\[.*?\]\n', res, content, flags=re.DOTALL)
    
    with open("schedule.py", "w") as f:
        f.write(content)

if __name__ == "__main__":
    generate_schedule()
