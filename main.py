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

# Inicializa o bot
if __name__ == '__main__':
    app = ApplicationBuilder().token("7396990967:AAFPb7QlPkGBZPJ88khZgbOoQX91ugV35Y0").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pdf", gerar))

    print("Bot iniciado.")
    app.run_polling()
