from flask import Flask, render_template, request, redirect, url_for, flash
import os
from dotenv import load_dotenv
import google.generativeai as genai
import markdown   # ← conversor de Markdown para HTML

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev")

# Configurar a API do Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Prompt base para manter o tema do projeto
PROMPT_SISTEMA = """
Você é um especialista em turismo especializado no Litoral Paraibano.
Responda sempre como um guia turístico com profundo conhecimento sobre praias, cultura,
história e curiosidades da região litorânea da Paraíba.

Se a pergunta do usuário fugir do tema, responda brevemente e redirecione a conversa
de volta ao tema do litoral paraibano.
"""


@app.route("/")
def index():
    destaques = [
        {"slug": "tambaú", "titulo": "Praia de Tambaú", "img": "praias/tambau.jpg"},
        {"slug": "coqueirinho", "titulo": "Praia do Coqueirinho", "img": "praias/coqueirinho.jpg"},
        {"slug": "barra-de-camaratuba", "titulo": "Barra de Camaratuba", "img": "praias/barra-de-camaratuba.jpg"},
    ]
    return render_template("index.html", destaques=destaques)


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/praias/<slug>")
def praias(slug):
    paginas = {
        "tambaú": "tambau.html",
        "coqueirinho": "coqueirinho.html",
        "barra-de-camaratuba": "barra-de-camaratuba.html"
    }
    page = paginas.get(slug)
    if not page:
        return redirect(url_for("index"))
    return render_template(f"praias/{page}")


@app.route("/gemini", methods=["GET", "POST"])
def gemini():
    if request.method == "POST":
        pergunta = request.form.get("pergunta", "").strip()

        if not pergunta:
            flash("Digite uma pergunta!", "warning")
            return redirect(url_for("gemini"))

        try:
            model = genai.GenerativeModel("gemini-2.0-flash")

            # Incluindo o prompt instruindo o modelo a focar no tema
            mensagem_final = f"{PROMPT_SISTEMA}\n\nPergunta do usuário: {pergunta}"

            response = model.generate_content(mensagem_final)
            resposta_markdown = response.text

            # Convertendo MARKDOWN → HTML
            resposta_html = markdown.markdown(resposta_markdown)

        except Exception as e:
            resposta_html = f"<p><strong>Erro ao consultar o Gemini:</strong> {e}</p>"

        return render_template("gemini_result.html", pergunta=pergunta, resposta=resposta_html)

    return render_template("gemini.html")


if __name__ == "__main__":
    app.run(debug=True)
