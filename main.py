import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from fpdf import FPDF

# Função que gera um PDF simples
def gerar_pdf(texto, nome_arquivo="arquivo.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, texto)
    pdf.output(nome_arquivo)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Envie /pdf para gerar um PDF.")

# Comando /pdf
async def gerar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gerar_pdf("Exemplo de conteúdo gerado pelo bot!")
    await update.message.reply_document(document=open("arquivo.pdf", "rb"))

# Inicializa o bot com webhook
if __name__ == '__main__':
    TOKEN = os.getenv("7396990967:AAFPb7QlPkGBZPJ88khZgbOoQX91ugV35Y0")  # Use variável de ambiente
    WEBHOOK_URL = os.getenv("https://telegram-pdf-bot.up.railway.app")  # Defina isso no Railway com a URL do seu app

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pdf", gerar))

    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        webhook_url=f"{WEBHOOK_URL}/{TOKEN}"
    )
