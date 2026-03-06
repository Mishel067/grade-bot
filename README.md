# GradeBot

A Telegram bot for tracking school grades with statistics, graphs, and data export.

Built with Python, SQLite, and Matplotlib.

## ✨ Features
- `/add subject grade1 grade2 ...` — add grades
- `/stats` — view average scores by subject
- `/graph` — visualize your progress over time
- `/export` — download all data as CSV

All data is stored locally in an SQLite database and persists between restarts.

## 📸 Screenshots

![Adding grades](screenshots/gradebot_add.png)
![Statistics](screenshots/gradebot_stats.png)
![Progress graph](screenshots/gradebot_graph.png)

## 🛠️ Tech Stack
- Python 3
- `telebot` (pyTelegramBotAPI)
- `sqlite3`
- `matplotlib`


## 🚀 How to Run
1. Get a bot token from [@BotFather](https://t.me/BotFather)
2. Set it in `YOUR_TOKEN_HERE` in the code
3. Install dependencies:
```bash
pip install pyTelegramBotAPI matplotlib pandas
```
4. Run:
```bash
python gradebot.py
```

Made by Misha • Vladimir, Russia
```

