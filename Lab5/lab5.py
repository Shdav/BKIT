import telebot
from telebot import types
bot = telebot.TeleBot('5041309858:AAF1SXcC3ZKkbNe4XRKRfd8UK1t7NpYeQxw');
name = '';
surname = '';
age = 0;
markup = types.ReplyKeyboardMarkup() 
@bot.message_handler(content_types=['text'])
def start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("reg","state")
    bot.send_message(message.chat.id, "Следуйте указаниям:", reply_markup=user_markup)
    if message.text == "state" or message.text == "reg":
        if message.text == "state":
            bot.send_message(message.from_user.id, """Ты приступил к выполнению 6-ой лабы \n Для смены кнопок снова нажми state""")
            bot.register_next_step_handler(message, state)
        if message.text == "reg":
            bot.send_message(message.from_user.id, "Ты приступил к выполнению 5-ой лабы \n Как тебя зовут?")
            bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, """Нажми кнопку reg для выполнения 5-ой лабы, для 6-ой state """)
def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?");
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, "Сколько тебе лет?");
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, "Что-то пошло не так... введите данные заново, нажав /reg");
             return
                    
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
    keyboard.add(key_yes); #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no);
    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?';
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        ... #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, "Запомню :-)");
    else:
        call.data == "no"
        ...
        bot.send_message(call.message.chat.id, "Введите Ваши данные заново, нажав /reg")     

bot.polling(none_stop=True, interval=0)