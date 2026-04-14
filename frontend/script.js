const API_BASE_URL = 'http://localhost:8000/api';

// DOM Elements
const todayContainer = document.getElementById('today-container');
const scheduleContainer = document.getElementById('schedule-container');
const standingsBody = document.getElementById('standings-body');

// Formatting utilities
const formatDate = (dateString) => {
    const options = { month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-US', options);
};

const getDay = (dateString) => new Date(dateString).getDate();
const getMonth = (dateString) => new Date(dateString).toLocaleDateString('en-US', { month: 'short' });

// Fetch data from API
async function fetchTodayMatch() {
    try {
        const response = await fetch(`${API_BASE_URL}/today`);
        const data = await response.json();
        
        if (data.today && data.today.length > 0) {
            renderTodayMatches(data.today);
        } else {
            // If no match today, show the next upcoming match
            fetchNextUpcoming();
        }
    } catch (error) {
        console.error('Error fetching today match:', error);
        todayContainer.innerHTML = `<div class="loading" style="color: #ef4444;">Error loading match data. Is the backend running?</div>`;
    }
}

async function fetchNextUpcoming() {
    try {
        const response = await fetch(`${API_BASE_URL}/upcoming?limit=1`);
        const data = await response.json();
        
        if (data.upcoming && data.upcoming.length > 0) {
            todayContainer.innerHTML = `<p style="text-align:center; color:var(--text-secondary); margin-bottom:1rem;">No match today. Next upcoming match:</p>`;
            renderTodayMatches(data.upcoming, true); // append true
        } else {
            todayContainer.innerHTML = `<div class="loading">No matches scheduled.</div>`;
        }
    } catch (error) {
        console.error('Error fetching next match:', error);
    }
}

async function fetchSchedule() {
    try {
        const response = await fetch(`${API_BASE_URL}/upcoming?limit=10`);
        const data = await response.json();
        
        if (data.upcoming && data.upcoming.length > 0) {
            renderSchedule(data.upcoming);
        } else {
            scheduleContainer.innerHTML = `<div class="loading">No upcoming fixtures found.</div>`;
        }
    } catch (error) {
        console.error('Error fetching schedule:', error);
        scheduleContainer.innerHTML = `<div class="loading" style="color: #ef4444;">Failed to load schedule.</div>`;
    }
}

async function fetchStandings() {
    try {
        const response = await fetch(`${API_BASE_URL}/standings`);
        const data = await response.json();
        
        if (data.standings && data.standings.length > 0) {
            renderStandings(data.standings);
        }
    } catch (error) {
        console.error('Error fetching standings:', error);
        standingsBody.innerHTML = `<tr><td colspan="6" class="loading" style="color: #ef4444;">Failed to load standings.</td></tr>`;
    }
}

// Render Functions
function renderTodayMatches(matches, append = false) {
    let html = '';
    
    matches.forEach(m => {
        const { match, prediction, h2h, team1_full, team2_full, team1_color, team2_color, venue_full } = m;
        
        const predictedWinnerFull = prediction.predicted_winner === match.team1 ? team1_full : team2_full;
        const predictedWinnerColor = prediction.predicted_winner === match.team1 ? team1_color : team2_color;
        
        html += `
            <div class="match-card">
                <div class="match-header">
                    <div class="match-info">
                        <span class="badge">Match ${match.match}</span>
                        <span class="match-time">${formatDate(match.date)} • ${match.time} IST</span>
                    </div>
                    <div class="match-venue">
                        📍 ${venue_full}
                    </div>
                </div>
                
                <div class="match-body">
                    <div class="team">
                        <div class="team-logo" style="border-color: ${team1_color}; color: ${team1_color}; box-shadow: 0 0 20px ${team1_color}40;">
                            ${match.team1}
                        </div>
                        <div class="team-name">${team1_full}</div>
                    </div>
                    
                    <div class="vs">VS</div>
                    
                    <div class="team">
                        <div class="team-logo" style="border-color: ${team2_color}; color: ${team2_color}; box-shadow: 0 0 20px ${team2_color}40;">
                            ${match.team2}
                        </div>
                        <div class="team-name">${team2_full}</div>
                    </div>
                </div>
                
                <div class="prediction-result">
                    <div class="prediction-title">AI Prediction</div>
                    <div class="winner-announce" style="color: ${predictedWinnerColor}; text-shadow: 0 0 20px ${predictedWinnerColor}80;">
                        ${predictedWinnerFull} To Win
                    </div>
                    
                    <div class="probability-bar-container">
                        <div class="prob-fill prob-t1" style="width: ${prediction.team1_probability}%; background-color: ${team1_color};"></div>
                        <div class="prob-fill prob-t2" style="width: ${prediction.team2_probability}%; background-color: ${team2_color};"></div>
                    </div>
                    
                    <div class="prob-labels">
                        <span style="color: ${team1_color}">${prediction.team1_probability}%</span>
                        <span style="color: ${team2_color}">${prediction.team2_probability}%</span>
                    </div>
                </div>
                
                ${h2h ? `
                <div class="stats-panel">
                    <div class="stat-item">
                        <div class="stat-label">Head-to-Head Win Rate</div>
                        <div class="stat-value">
                            <span style="color: ${team1_color}">${h2h.team1_win_pct}%</span> - 
                            <span style="color: ${team2_color}">${h2h.team2_win_pct}%</span>
                        </div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Recent Form</div>
                        <div class="stat-value">
                            <span style="color: ${team1_color}">${h2h.team1_recent_form}</span> - 
                            <span style="color: ${team2_color}">${h2h.team2_recent_form}</span>
                        </div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Model Confidence</div>
                        <div class="stat-value" style="color: ${prediction.confidence > 60 ? '#10b981' : '#f59e0b'};">
                            ${prediction.confidence}%
                        </div>
                    </div>
                </div>
                ` : ''}
            </div>
        `;
    });
    
    if (append) {
        todayContainer.innerHTML += html;
    } else {
        todayContainer.innerHTML = html;
    }
}

function renderSchedule(matches) {
    let html = '';
    
    matches.forEach(m => {
        const { match, prediction, team1_full, team2_full, team1_color, team2_color, venue_full } = m;
        
        // Skip the very first one if it's currently showing in Today's Match
        const today = new Date().toISOString().split('T')[0];
        if (match.date === today && todayContainer.innerHTML.includes(match.team1)) {
            return;
        }

        html += `
            <a href="#" class="schedule-item" onclick="event.preventDefault()">
                <div class="sch-date">
                    <span class="sch-day">${getDay(match.date)}</span>
                    <span class="sch-month">${getMonth(match.date)}</span>
                </div>
                
                <div class="sch-content">
                    <div class="sch-teams">
                        <span style="color: ${team1_color}">${match.team1}</span>
                        <span class="sch-vs">vs</span>
                        <span style="color: ${team2_color}">${match.team2}</span>
                    </div>
                    <div class="sch-venue">📍 ${venue_full} • Match ${match.match}</div>
                </div>
                
                <div class="sch-prediction">
                    <div class="mini-prob">AI Predicts</div>
                    <div class="mini-winner" style="color: ${prediction.predicted_winner === match.team1 ? team1_color : team2_color}">
                        ${prediction.predicted_winner} Win (${Math.max(prediction.team1_probability, prediction.team2_probability)}%)
                    </div>
                </div>
            </a>
        `;
    });
    
    scheduleContainer.innerHTML = html || '<div class="loading">No upcoming schedule.</div>';
}

function renderStandings(standings) {
    let html = '';
    
    standings.forEach((team, index) => {
        html += `
            <tr>
                <td><strong>#${index + 1}</strong></td>
                <td>
                    <div class="team-cell">
                        <div class="team-dot" style="background-color: ${team.color}; box-shadow: 0 0 10px ${team.color}80;"></div>
                        ${team.full_name} (${team.team})
                    </div>
                </td>
                <td style="font-weight: 700; color: ${team.win_rate > 50 ? '#10b981' : 'var(--text-secondary)'}">${team.win_rate}%</td>
                <td>${team.matches}</td>
                <td>${team.wins}</td>
                <td>${team.losses}</td>
            </tr>
        `;
    });
    
    standingsBody.innerHTML = html;
}

// Initialization
document.addEventListener('DOMContentLoaded', () => {
    // Navigation active state
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Fetch data
    fetchTodayMatch();
    fetchSchedule();
    fetchStandings();
});
