import requests

def monitor_financeiro_atualizado():
    # 1. Definimos a URL e o alvo
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,BTC-BRL,ETH-BRL"
    
    try:
        print("\n[💰] ACESSANDO RADAR FINANCEIRO - ORÁCULO SENTINEL...")
        
        # 2. Tentamos buscar os dados (com timeout para não travar o Termux)
        response = requests.get(url, timeout=10)
        dados = response.json()

        # 3. Uso do .get() -> se a API falhar, ele usa um dicionário vazio {} em vez de quebrar
        dolar_data = dados.get('USDBRL', {})
        btc_data = dados.get('BTCBRL', {})

        # 4. Pegamos o valor 'bid' (compra). Se não existir, vira "0"
        valor_dolar = dolar_data.get('bid', '0')
        valor_btc = btc_data.get('bid', '0')

        # 5. Formatação final para o painel
        resultado = f"💵 Dólar: R$ {float(valor_dolar):.2f} | ₿ BTC: R$ {float(valor_btc):.2f}"
        print(f"[{resultado}]")
        return resultado

    except Exception as e:
        # Se qualquer coisa der errado (falta de internet, API fora do ar), 
        # o código cai aqui, avisa o erro no terminal, mas NÃO trava o sistema.
        print(f"[!] Erro ao capturar dados financeiros: {e}")
        return "⚠️ Erro ao acessar radar financeiro (Offline)."

# Desenvolvido por Crispim & Oráculo

