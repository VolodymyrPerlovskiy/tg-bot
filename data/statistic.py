import prettytable as pt
from telegram import ParseMode
from telegram import CallbackContext, Updater


def send_table(update: Updater, context: CallbackContext):
    table = pt.PrettyTable(['Symbol', 'Price', 'Change'])
    table.align['Symbol'] = 'l'
    table.align['Price'] = 'r'
    table.align['Change'] = 'r'

    data = [
        ('ABC', 20.85, 1.626),
        ('DEF', 78.95, 0.099),
        ('GHI', 23.45, 0.192),
        ('JKL', 98.85, 0.292),
    ]
    for symbol, price, change in data:
        table.add_row([symbol, f'{price:.2f}', f'{change:.3f}'])

    
    # or use markdown
    update.message.reply_text(f'```{table}```', parse_mode=ParseMode.MARKDOWN_V2)