import requests

def monitor_financeiro_atualizado():
    print("\n[💰] ACESSANDO RADAR FINANCEIRO - ORÁCULO SENTINEL...")
    
    # URL para pegar Dólar, Bitcoin e Monero (via USDT ou direto se disponível)
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,BTC-BRL,ETH-BRL"
    
    try:
        response = requests.get(url, timeout=10)
        dados = response.json()
        
        # Extraindo valores
        dolar = dados['USDBRL']['bid']
        btc = dados['BTCBRL']['bid']
        
        print(f"💵 Dólar Comercial: R$ {float(dolar):.2f}")
        print(f"₿ Bitcoin: R$ {float(btc):.2f}")
        
        # Lógica de Impacto (Para o seu portfólio de notícias)
        if float(dolar) > 5.50:
            print("⚠️ ALERTA: Dólar em alta. Impacto negativo previsto para importações.")
        else:
            print("✅ Estabilidade detectada no par USD/BRL.")

    except Exception as e:
        print(f"[!] Erro ao captar dados financeiros: {e}")

        resultado = f"💵 Dólar: R$ {float(dolar):.2f} | ₿ BTC: R$ {float(btc):.2f}"
        return resultado
    except:
        return "⚠️ Erro ao acessar dados financeiros."


