import requests
from bs4 import BeautifulSoup

def monitor_social_alertas():
    print("\n[🚨] INICIANDO VARREDURA DO RADAR SOCIAL...")
    
    # Lista de sites para monitorar (Exemplos: Portais de notícias e utilidade pública)
    # Podemos adaptar para sites específicos de Goiânia e Internacionais
    urls = [
        "https://g1.globo.com/go/goias/", 
        "https://www.cnnbrasil.com.br/internacional/"
    ]
    
    # Palavras-chave que o Oráculo Sentinel deve filtrar
    gatilhos = ["desaparecido", "desaparecida", "criança sumida", "serial killer", "procurado", "sequestro"]
    
    alertas_encontrados = []

    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # O Oráculo lê todos os títulos (h2, h3, etc) do site
            titulos = soup.find_all(['h1', 'h2', 'h3'])
            
            for t in titulos:
                texto_limpo = t.get_text().lower()
                for g in gatilhos:
                    if g in texto_limpo:
                        alertas_encontrados.append(t.get_text().strip())
        except Exception as e:
            print(f"[!] Erro ao acessar {url}: {e}")

    # Exibição dos Resultados
    if alertas_encontrados:
        print(f"⚠️ {len(alertas_encontrados)} ALERTAS CRÍTICOS ENCONTRADOS NO RADAR:")
        for i, alerta in enumerate(alertas_encontrados, 1):
            print(f"{i}. {alerta}")
    else:
        print("✅ Radar limpo: Nenhuma ocorrência crítica detectada agora.")

    if alertas_encontrados:
        return f"🚨 {len(alertas_encontrados)} alertas encontrados no radar."
    return "✅ Radar social limpo no momento."


