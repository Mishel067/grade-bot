import telebot
import csv
import io
user_grades ={}
valid = { 'математика', 'русский', 'английский', 'физика', 'химия', 'биология', 'история', 'география', 'информатика', 'литература', 'обж', 'физкультура', 'музыка', 'рисование', 'технология'}
bot = telebot.TeleBot('YOUR_TOKEN_HERE')
@bot.message_handler(commands=['start'])
def start_command(message):
  bot.reply_to(message, '👋 Привет! Я GradeBot - твой школьный помощник по оценкам.\n\n Команды: \n• /add предмет оценка - добавить оценку\n• /stats - показать средний балл\n• /export - скачать CSV файл\n•/help или /about - помощь с GradeBot\n\nУдачи в учёбе!💯')
@bot.message_handler(commands=['add'])
def add_command(message):
  chat_id = message.chat.id
  text = message.text.split()
  if len(text) < 2:
    bot.reply_to(message, '❌ Пример: /add математика 5')
    return
  subject = text[1].lower()
  grades = text[2:]
  try:
    if subject not in valid:
      bot.reply_to(message, f'❌ \'{subject}\' - не похоже на предмет.\n' "Разрешены: "+', '.join(sorted(valid))[:122] + '...')
      return
    grades = [int(g) for g in grades]
    if not all(0 < g < 6 for g in grades):
      bot.reply_to(message,'❌ Оценки должны быть от 1 до 5')
      return
  except ValueError:
    bot.reply_to(message, '❌ Оценки должны быть от 1 до 5 цифрами (1-5)')
    return
  if chat_id not in user_grades:
    user_grades[chat_id] = {}
  if subject not in user_grades[chat_id]:
    user_grades[chat_id][subject] = []
  user_grades[chat_id][subject].extend(grades)
  bot.reply_to(message, f'✅ Добавлено: {subject} → {', '.join(map(str, grades))}')
@bot.message_handler(commands=['stats'])
def stats_command(message):
  chat_id = message.chat.id
  if chat_id not in user_grades:
    bot.reply_to(message, '📊 У тебя пока нет оценок добавь через /add.')
    return
  grades_dict = user_grades[chat_id]
  lines = []
  total_sum = 0
  total_count = 0

  for subj, grades in grades_dict.items():
    avg = sum(grades) / len(grades)
    total_sum += sum(grades)
    total_count += len(grades)
    if avg < 4.0:
      advice = '⚠️ Стоит повторить тему!'
    elif avg > 4.8:
      advice = '🌟 Отлично! Продолжай в том же духе!'
    else:
      advice = '✅ Хорошо, но можно лучше.'
    lines.append(f'{subj}: {', '.join(map(str, grades))} → {avg:.2f} {advice}')
  overall = total_sum / total_count if total_count else 0
  responce = '📊 Статистика:\n'+ '\n'.join(lines)
  responce += f'\n\n📌 ИТОГО: {overall:.2f}'
  bot.reply_to(message, responce)
@bot.message_handler(commands=['export'])
def export_command(message):
  chat_id = message.chat.id
  if chat_id not in user_grades:
    bot.reply_to(message,'📎 У тебя пока нет  оценок для экспорта.')
    return
  output = io.StringIO()
  writer = csv.writer(output)
  writer.writerow(['Предмет', "Оценки", 'Среднее'])
  for subj, grades in user_grades[chat_id].items():
    avg = sum(grades) / len(grades)
    writer.writerow([subj, ', '.join(map(str, grades)), f'{avg:.2f}'])
  output.seek(0)
  csv_data = output.getvalue().encode('utf-8')
  bot.send_document(
      message.chat.id,
      io.BytesIO(csv_data),
      caption='📤 Твои оценки (CSV)',
      visible_file_name ='оценки.csv'
  )
@bot.message_handler(commands=['help', 'about'])
def help_command(message):
  bot.reply_to(message,'❓🤖 Помощь по GradeBot\n\n/add предмет оценка\n→ Добавить одну или несколько оценок.\nПример: /add математика 5 или: /add русский 4 5 3\n\n/stats\n→ Показать средний балл по всем предметам.\n\n/export\n→ Получить файл с оценками (CSV).\n\n⚠️ Советы:\n• Предмет пиши строчными буквами (без заглавных).\n• Оценки - только цифры от 1 до 5.\n• Бот не работает ночью - как и ты! 😴')
@bot.message_handler(content_types=['text'])
def handle_text (message):
  responce = f'Вы написали: {message.text}'
  bot.send_message(message.chat.id, responce)
print('Бот запущен...')
bot.polling(none_stop=True)