from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from fpdf import FPDF
import os

def gerar_pdf(texto, filename="saida.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for linha in texto.split('\n'):
        pdf.multi_cell(0, 10, txt=linha)
    pdf.output(filename)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Envie um texto e eu vou gerar um PDF.")

async def texto_para_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    gerar_pdf(texto)
    await update.message.reply_document(document=open("saida.pdf", "rb"))

if name == 'main':
    TOKEN = os.environ["BOT_TOKEN"]
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, texto_para_pdf))
    app.run_polling()
