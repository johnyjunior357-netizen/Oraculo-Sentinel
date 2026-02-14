import sys
import threading
import time
import json
from flask import Flask, render_template, jsonify
from bot_noticias.financeiro import monitor_financeiro_atualizado

app = Flask(__name__)

# Memória central do Oráculo
dados_sentinel = {
    "financeiro": "Iniciando radar...",
    "social": "Varredura ativa...",
    "geopolitico": "Analisando potências...",
    "status": "Online"
}

def radar_bots():
    """Roda em segundo plano no Termux para atualizar o painel"""
    while True:
        dados_sentinel["financeiro"] = monitor_financeiro_atualizado()
        time.sleep(60) # Atualiza a cada 1 minuto no modo servidor

@app.route('/')
def index():
    return render_template('index.html', dados=dados_sentinel)

@app.route('/api/updates')
def updates():
    return jsonify(dados_sentinel)

if __name__ == "__main__":
    # LOGICA PARA O GITHUB ACTIONS (MODO SENTINELA)
    # Corrigido: Aspas fechadas corretamente
    if "--auto-update" in sys.argv:
        print("[🤖] MODO AUTOMÁTICO DETECTADO (GITHUB ACTIONS)")
        resumo = monitor_financeiro_atualizado()
        
        # Salva o resultado em JSON para o GitHub registrar a mudança
        with open('dados_sentinel.json', 'w') as f:
            json.dump({"financeiro": resumo, "ultimo_check": time.ctime()}, f)
            
        print("[✅] Varredura finalizada com sucesso. Encerrando processo.")
        sys.exit(0) # Força a saída para o GitHub Actions não travar

    # LOGICA PARA O TERMUX (MODO MANUAL/PAINEL)
    else:
        print("[🔥] INICIANDO ORÁCULO SENTINEL NO MODO SERVIDOR")
        threading.Thread(target=radar_bots, daemon=True).start()
        # Roda o servidor Flask no IP local do Termux
        app.run(host='0.0.0.0', port=5000, debug=False)

