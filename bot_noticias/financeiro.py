import requests

def monitor_financeiro_atualizado():
    print("\n[💰] ACESSANDO RADAR FINANCEIRO - ORÁCULO SENTINEL...")
    # API da AwesomeAPI (Dólar, Bitcoin e Ethereum)
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,BTC-BRL,ETH-BRL"
    
    try:
        response = requests.get(url, timeout=10)
        dados = response.json()
        
        # Uso do .get() para evitar o KeyError (Erro de chave ausente)
        dolar_data = dados.get('USDBRL', {})
        btc_data = dados.get('BTCBRL', {}) # Corrigido para BTCBRL
        
        # Pega o valor de compra ('bid'), se não existir usa "0"
        valor_dolar = dolar_data.get('bid', '0')
        valor_btc = btc_data.get('bid', '0')
        
        # Formata os valores para 2 casas decimais
        resultado = f"💵 Dólar: R$ {float(valor_dolar):.2f} | ₿ BTC: R$ {float(valor_btc):.2f}"
        print(f"[✅] {resultado}")
        return resultado

    except Exception as e:
        print(f"[!] Erro ao captar dados financeiros: {e}")
        return "⚠️ Erro ao acessar radar financeiro."

