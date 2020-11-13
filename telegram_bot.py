import telegram, telepot
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackQueryHandler

token = '1450436381:AAF6WGHOl8q4h2oSsv3g6NV5GtwcOYPaAd8'
barumi = telepot.Bot(token)

user_data = barumi.getUpdates()

updater = Updater(token, use_context = True)
dispatcher = updater.dispatcher

def start(update, context):
    chat_id = update.effective_chat.id
    user_name = update.effective_chat.first_name
    context.bot.sendMessage(chat_id, text = '안녕하세요 바루미입니다.😊 \n%s님의 통계를 보내드리겠습니다. \n\n/tasks를 입력하시면 보고 싶은 통계를 선택하실 수 있습니다. \n\n/image를 입력하시면 통계를 사진으로 확인하실 수 있습니다.'% user_name)
    
def stop(update, context):
    chat_id = update.effective_chat.id
    user_name = update.effective_chat.first_name
    context.bot.sendMessage(chat_id, text = '감사합니다. %s님 ❤ 다음에도 이용하고 싶으면 /start를 보내주세요.'% user_name)
    
start_handler = CommandHandler('start', start)
stop_handler = CommandHandler('stop', stop)
 
dispatcher.add_handler(start_handler)
dispatcher.add_handler(stop_handler)

def task_buttons(update, context):
    buttons = [[
        InlineKeyboardButton('마스크 벗은 횟수', callback_data = 1)
        , InlineKeyboardButton('기록측정한 총 시간', callback_data = 2)
    ], [
         InlineKeyboardButton('바른자세 총 시간', callback_data = 3)
        , InlineKeyboardButton('나쁜자세 총 시간', callback_data = 4)
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    context.bot.send_message(
        chat_id = update.message.chat_id
        , text = '버튼을 눌러주세요.'
        , reply_markup = reply_markup
    )

def callback_buttons(update, context):
    query = update.callback_query
    data = query.data
    
    context.bot.send_chat_action(
        chat_id = update.effective_chat.id
        , action = ChatAction.TYPING
    )
    context.bot.edit_message_text(
        text = '[{}] 데이터를 불러오는데 성공했습니다.'.format(data)
        , chat_id = query.message.chat_id
        , message_id = query.message.message_id
    )
    
task_buttons_handler = CommandHandler('tasks', task_buttons)
callback_buttons_handler = CallbackQueryHandler(callback_buttons)

dispatcher.add_handler(task_buttons_handler)
dispatcher.add_handler(callback_buttons_handler)

updater.start_polling()
updater.idle()