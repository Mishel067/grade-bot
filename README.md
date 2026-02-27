# grade-bot
Telegram bot for tracking school grades - built by a 12-years-old developer
[README.md](https://github.com/user-attachments/files/25607780/README.md)
# GradeBot 📊

A simple Telegram bot for trackind school grades - built by a 6th grader.
No fluff. Just works.

## Features
- `/add <subject> <grade>` - add one or multiple grades
  Example: 1/add math 5` or `/add russian 4 5 3`
- `/stats` - shows average per subject + helpful tips
- `/export` - downloads your grades as CSV
- Smart validation:
  - Only grades 1-5 accepted
  - Only real subjects (e.g. `math`, `physics`) - no `chips` or `cat`
  - Private: each user sees only their own data

## How to Run
1. Install Python 3.8+
2. Run:

```bash
   pip install pyTelegramBotAPI
3. Create a bot via @BotFather
4. Paste your token into `gradebot.py`:
`TOKEN = 'YOUR_TOKEN_HERE'

5. Run `python gradebot.py`
> Works in Google Colab - but for 24/7 use, run on your PC or a cheap VPS.
## Privacy
Grades are storedper `chat_id` - no sharing,
no leaks.

## Made by
Misha, 6t grade, Vladimir
"I built it myself. And it works."

