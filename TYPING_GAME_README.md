# 🚀 Online Typing Speed Game

A modern, web-based typing speed game built with Python Flask, featuring real-time leaderboards and multiplayer functionality!

## ✨ Features

- 🎯 **Real-time Typing Test**: 60-second timed typing challenges
- 📊 **Live Statistics**: WPM (Words Per Minute) and accuracy tracking
- 🏆 **Global Leaderboard**: See how you rank against other players
- 🎨 **Modern UI**: Beautiful, responsive design that works on all devices
- 📱 **Multiplayer Ready**: Anyone on your network can play and compete
- 💾 **Persistent Scores**: All scores are saved in a local database
- 🔄 **Multiple Texts**: Educational content from various topics

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Internet connection (for initial Flask installation)

### Installation & Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Game**:
   ```bash
   python typing_game.py
   ```

3. **Open in Browser**:
   - Game: http://localhost:5000
   - Leaderboard: http://localhost:5000/leaderboard

## 🎮 How to Play

### Game Rules
1. Click "Start New Game" to begin
2. Type the displayed text as quickly and accurately as possible
3. You have 60 seconds to complete the text
4. Your score is calculated based on WPM and accuracy
5. Submit your score to compete on the leaderboard!

### Controls
- **Start New Game**: Begin a new typing test
- **Reset**: Clear current game and start over
- **Submit Score**: Save your result to the leaderboard
- **Leaderboard**: View all player scores

### Scoring System
- **WPM (Words Per Minute)**: Speed of typing
- **Accuracy**: Percentage of correctly typed words
- **Final Score**: WPM × (Accuracy ÷ 100)

## 🌐 Multiplayer Setup

### For Local Network (Lab/Classroom)
1. Find your computer's IP address:
   ```bash
   # Windows
   ipconfig
   
   # Look for "IPv4 Address" (usually 192.168.x.x)
   ```

2. Run the game with network access:
   ```bash
   python typing_game.py
   ```

3. Share the URL with classmates:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```

### Example Network Setup
- **Your Computer**: 192.168.1.100
- **Classmates Access**: http://192.168.1.100:5000
- **Everyone can play and see the same leaderboard!**

## 📊 Leaderboard Features

- **Real-time Updates**: New scores appear immediately
- **Top 20 Players**: See the best performers
- **Detailed Stats**: WPM, accuracy, score, and timestamp
- **Medals**: 🥇🥈🥉 for top 3 players
- **Mobile Friendly**: Responsive design for phones/tablets

## 🛠️ Technical Details

### Architecture
- **Backend**: Python Flask web framework
- **Database**: SQLite (no setup required)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Modern CSS with gradients and animations

### File Structure
```
Ai_Final/
├── typing_game.py          # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html         # Main game page
│   └── leaderboard.html   # Leaderboard page
├── typing_leaderboard.db  # SQLite database (auto-created)
└── TYPING_GAME_README.md  # This file
```

### Database Schema
```sql
CREATE TABLE leaderboard (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT NOT NULL,
    wpm REAL NOT NULL,
    accuracy REAL NOT NULL,
    score INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## 🎯 Educational Content

The game includes typing texts about:
- **Technology**: Python, AI, Machine Learning
- **Science**: Internet, Cybersecurity, Data Science
- **Innovation**: Blockchain, Virtual Reality, Cloud Computing
- **Classic**: Pangrams and general knowledge

## 🔧 Customization

### Adding New Texts
Edit `TYPING_TEXTS` in `typing_game.py`:
```python
TYPING_TEXTS = [
    "Your new text here...",
    "Another educational paragraph...",
    # Add more texts
]
```

### Changing Game Duration
Modify the timer in `typing_game.py`:
```python
gameState.timeLeft = 60  # Change to desired seconds
```

### Styling Changes
Edit CSS in the HTML templates to customize colors, fonts, and layout.

## 🚨 Troubleshooting

### Common Issues

1. **Port Already in Use**:
   ```bash
   # Change port in typing_game.py
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

2. **Flask Not Found**:
   ```bash
   pip install flask
   ```

3. **Database Errors**:
   - Delete `typing_leaderboard.db` and restart
   - The database will be recreated automatically

4. **Network Access Issues**:
   - Check Windows Firewall settings
   - Ensure you're on the same network
   - Try using `127.0.0.1` instead of localhost

## 🎉 Perfect for Lab Sessions!

This typing game is ideal for:
- **Computer Lab Classes**: Everyone can compete
- **Programming Workshops**: Fun break between coding
- **Team Building**: Friendly competition
- **Skill Assessment**: Test typing proficiency
- **Educational Gaming**: Learning while having fun

## 📈 Future Enhancements

Potential improvements:
- User accounts and profiles
- Different difficulty levels
- Custom text uploads
- Real-time multiplayer features
- Sound effects and animations
- Export results to CSV/PDF

---

**Enjoy the game and happy typing! 🚀⌨️** 