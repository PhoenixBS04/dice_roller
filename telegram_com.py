from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram.ext import (
Updater,
CommandHandler,
CallbackQueryHandler,
ConversationHandler,
CallbackContext,
)
from utilus import *
from telegram import Bot
TOKEN = "5510644908:AAFsI-gFY5a0RN-VXlk1rnTfUf7b25PRMIU"
bot = Bot(TOKEN)

CHOOSE_DICE = 1
ROLL_DICE = 2


def common_menus(dice):
    keys = [
        [InlineKeyboardButton("Back to menu", callback_data="choose_dice")],
        [InlineKeyboardButton("Reroll", callback_data=f"d{dice}")]
    ]
    reply_markup = InlineKeyboardMarkup(keys)
    return reply_markup


def start(update: Update, context: CallbackContext) -> int:
    keys = [[InlineKeyboardButton("Let's begin!", callback_data="choose_dice")]]
    reply_markup = InlineKeyboardMarkup(keys)
    update.message.reply_text(
        "Greetings, traveller 🤟! \n\n"
        "I am dice roller, you can press start so to start (surprise surprise) "
        "using me", reply_markup=reply_markup)
    return ROLL_DICE


def choosing_dice(update, context):
    query = update.callback_query
    query.answer()
    keys = [
        [InlineKeyboardButton("d4", callback_data="d4"), InlineKeyboardButton("d6", callback_data="d6")],
        [InlineKeyboardButton("d12", callback_data="d12"), InlineKeyboardButton("d20", callback_data="d20")]
    ]
    reply_markup = InlineKeyboardMarkup(keys)
    query.edit_message_text("Choose what u want to roll\n"
                            "Bep bop (I am bot so I am making robotic sounds)", reply_markup=reply_markup)
    return ROLL_DICE


def rolling_dice(update, context):
    query = update.callback_query
    query.answer()
    how_many = query.data
    sides = how_many_sides(how_many)
    dice = roll_dice(sides)
    reply_markup = common_menus(sides)
    query.edit_message_text(f"Result: {dice}", reply_markup=reply_markup)
    return ROLL_DICE


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ROLL_DICE: [
                CallbackQueryHandler(rolling_dice, pattern="^d4|d6|d12|d20$"),
                CallbackQueryHandler(choosing_dice, pattern="^choose_dice$")
            ]
        },
        fallbacks=[CommandHandler('start', start)],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


main()