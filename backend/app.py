from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def gerar_resposta(mensagem):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": mensagem,
            "stream": False
        }
    )

    return response.json()["response"]

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mensagem = data["mensagem"]

    texto_resposta = gerar_resposta(mensagem)

    return jsonify({"resposta": texto_resposta})

if __name__ == "__main__":
    app.run(port=5000, debug=True)