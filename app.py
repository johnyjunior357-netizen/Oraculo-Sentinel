from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__, template_folder='web_interface')

def buscar_dados_db():
    conn = sqlite3.connect('database/sentinel.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute("SELECT titulo, link, categoria FROM noticias ORDER BY id DESC LIMIT 10")
    noticias = [dict(row) for row in c.fetchall()]
    
    c.execute("SELECT par, valor FROM moedas")
    moedas = [dict(row) for row in c.fetchall()]
    
    conn.close()
    return {"noticias": noticias, "moedas": moedas}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/noticias')
def api_noticias():
    try:
        dados = buscar_dados_db()
        return jsonify(dados)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

