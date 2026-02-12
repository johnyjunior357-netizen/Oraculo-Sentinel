import requests
from bs4 import BeautifulSoup
import sqlite3
import os
from datetime import datetime

def inicializar_banco():
    # Garante que a pasta database exista para evitar erros de diretório
    if not os.path.exists('database'):
        os.makedirs('database')
    
    conn = sqlite3.connect('database/sentinel.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS noticias 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, link TEXT, categoria TEXT, data TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS moedas 
                 (par TEXT PRIMARY KEY, valor TEXT, data TEXT)''')
    conn.commit()
    conn.close()

def buscar_dados_globais():
    precos = {"BTC": "Indisponível", "USD": "Indisponível"}
    noticias_capturadas = []
    
    # 1. Coleta de Moedas com Timeout de 5 segundos (evita travamento)
    try:
        btc_res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", timeout=5)
        dolar_res = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL", timeout=5)
        
        if btc_res.status_code == 200:
            btc = btc_res.json()
            precos["BTC"] = f"${btc['bitcoin']['usd']:,}"
        
        if dolar_res.status_code == 200:
            dolar = dolar_res.json()
            precos["USD"] = f"R${float(dolar['USDBRL']['bid']):.2f}"
    except Exception as e:
        print(f"⚠️ Alerta Conexão Moedas: {e}")

    # 2. Coleta de Notícias (Geopolítica e Local)
    fontes = [
        {"url": "https://www.techtudo.com.br/seguranca/", "cat": "CIBER-DEFESA"},
        {"url": "https://www.opopular.com.br/goiania", "cat": "GOIÂNIA-LOCAL"}
    ]
    
    for fonte in fontes:
        try:
            res = requests.get(fonte['url'], timeout=5)
            sopa = BeautifulSoup(res.text, 'html.parser')
            links = sopa.find_all('a', class_='feed-post-link', limit=5)
            for link in links:
                noticias_capturadas.append({
                    "titulo": link.text.strip(),
                    "link": link.get('href'),
                    "cat": fonte['cat']
                })
        except Exception as e:
            print(f"⚠️ Alerta Fonte {fonte['cat']}: Site lento ou offline.")
            continue
    
    return precos, noticias_capturadas

def salvar_no_banco(precos, noticias):
    conn = sqlite3.connect('database/sentinel.db')
    c = conn.cursor()
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    # Atualiza Moedas
    c.execute("INSERT OR REPLACE INTO moedas VALUES (?, ?, ?)", ("BTC/USD", precos['BTC'], data_atual))
    c.execute("INSERT OR REPLACE INTO moedas VALUES (?, ?, ?)", ("USD/BRL", precos['USD'], data_atual))
    
    # Salva Notícias (Evita duplicados)
    for n in noticias:
        c.execute("SELECT id FROM noticias WHERE titulo = ?", (n['titulo'],))
        if not c.fetchone():
            c.execute("INSERT INTO noticias (titulo, link, categoria, data) VALUES (?, ?, ?, ?)",
                      (n['titulo'], n['link'], n['cat'], data_atual))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("🛡️ Iniciando Varredura Oráculo Sentinel...")
    inicializar_banco()
    p, n = buscar_dados_globais()
    salvar_no_banco(p, n)
    print("✅ Banco de Dados Atualizado com Sucesso!")

