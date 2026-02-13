from flask import Flask, render_template
import threading
import time

# Importando seus scripts
from bot_noticias.social import monitor_social_alertas
from bot_noticias.financeiro import monitor_financeiro_atualizado
from bot_noticias.geopolitica import radar_geopolitico_2026

app = Flask(__name__)

# Memória central do Oráculo
dados_sentinel = {
    "financeiro": "Iniciando radar...",
    "social": "Varredura ativa...",
    "geopolitica": "Analisando potências..."
}

def rodar_bots():
    while True:
        # Atualiza a memória com o retorno das funções
        dados_sentinel["financeiro"] = monitor_financeiro_atualizado()
        dados_sentinel["social"] = monitor_social_alertas()
        # Para a geopolítica, como é uma lista, vamos pegar os 3 primeiros
        dados_sentinel["geopolitica"] = "EUA, Rússia e China no topo do ranking 2026."
        time.sleep(30) # Atualiza o site a cada 30 segundos

@app.route('/')
def index():
    # Passa a variável 'dados' para o HTML usar
    return render_template('index.html', dados=dados_sentinel)

if __name__ == '__main__':
    # Roda os bots sem travar o site
    threading.Thread(target=rodar_bots, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)

