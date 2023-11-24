from h11 import Request
from telegram import Update
import datetime
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler


key_token = "6891672927:AAFxi5WARqgHddQV1lN_JYkpPJjmUYNCQxs" #Masukkan KEY-TOKEN BOT 
user_bot = "@Mas1m_Bot" #Masukkan @user bot


async def  start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gunakan /help untuk menampilkan apa yang dapat saya berikan..")
    
async def  help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim pesan, bot akan membalas pesan..")


async def  text_massage(update: Update, context:ContextTypes.DEFAULT_TYPE):
    text_diterima : str = update.message.text
    print(f"Pesan diterima : {text_diterima}")
    text_lwr_diterima = text_diterima.lower()

    greetings_triggers = ['halo', 'hallo', 'helo', 'hello']

    if any(greeting in text_lwr_diterima for greeting in greetings_triggers):
        await update.message.reply_text("Halo")
    elif 'selamat malam' in text_lwr_diterima or 'good night' in text_lwr_diterima:
        await update.message.reply_text("Selamat malam..., jangan lupa istirahat 😊")
    elif 'apa kabar' in text_lwr_diterima:
        await update.message.reply_text("Saya baik, terima kasih! Bagaimana dengan Anda?")
    elif 'gambar' in text_lwr_diterima:
        await update.message.reply_text("Maaf, saya hanya bisa merespons teks. Saya belum bisa memproses gambar.")
    elif 'siapa kamu' in text_lwr_diterima:
        await update.message.reply_text(f"bot adalah : {user_bot}")
    elif 'harga bitcoin' in text_lwr_diterima:
        await update.message.reply_text("Maaf, saya tidak memiliki informasi harga bitcoin saat ini.")
    elif 'lagu terbaru' in text_lwr_diterima:
        await update.message.reply_text("Maaf, saya tidak dapat memberikan informasi tentang lagu terbaru saat ini.")
    elif 'apa itu python' in text_lwr_diterima:
        await update.message.reply_text("Python adalah bahasa pemrograman tingkat tinggi yang sering digunakan untuk pengembangan web, kecerdasan buatan, dan lainnya.")
    elif 'good morning' in text_lwr_diterima or 'selamat pagi' in text_lwr_diterima:
        current_hour = datetime.datetime.now().hour
        if 5 <= current_hour < 12:
            await update.message.reply_text("Selamat pagi! Semoga hari Anda menyenangkan.")
        else:
            await update.message.reply_text("Sudah tidak pagi lagi, tapi halo!")
    elif 'good afternoon' in text_lwr_diterima or 'selamat siang' in text_lwr_diterima:
        current_hour = datetime.datetime.now().hour
        if 12 <= current_hour < 17:
            await update.message.reply_text("Selamat siang! Semoga hari Anda menyenangkan.")
        else:
            await update.message.reply_text("Sudah tidak siang lagi, tapi halo!")
    elif 'good evening' in text_lwr_diterima or 'selamat sore' in text_lwr_diterima:
        current_hour = datetime.datetime.now().hour
        if 17 <= current_hour < 20:
            await update.message.reply_text("Selamat sore! Semoga hari Anda menyenangkan.")
        else:
            await update.message.reply_text("Sudah tidak sore lagi, tapi halo!")
    else:
        await update.message.reply_text("bot teralu stupid untuk mengerti")


async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Gambar kamu bagus")
        
async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")


if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    #MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_massage))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    #error :
    app.add_error_handler(error)
    #polling :
    app.run_polling(poll_interval=1)



