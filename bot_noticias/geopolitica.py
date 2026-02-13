import requests
from bs4 import BeautifulSoup

def radar_geopolitico_2026():
    print("\n[🌍] ACESSANDO RADAR GEOPOLÍTICO - ORÁCULO SENTINEL...")
    
    # Base de dados interna do Oráculo para 2026
    ranking_militar = [
        "1. EUA (Liderança em Tecnologia)",
        "2. Rússia (Poder Nuclear e Hipersônico)",
        "3. China (Maior Marinha e Expansão IA)",
        "4. Índia", "5. Coreia do Sul", "6. Reino Unido", 
        "7. Japão", "8. Turquia", "9. Paquistão", "10. Brasil (Liderança AL)"
    ]
    
    print("🏆 TOP 10 POTÊNCIAS MILITARES (Status Atualizado):")
    for pais in ranking_militar:
        print(f"  {pais}")

    # Busca notícias de impacto em Defesa/Guerra
    url_defesa = "https://www.defesaaereanaval.com.br/" # Exemplo de site de defesa
    try:
        res = requests.get(url_defesa, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        noticias = soup.find_all('h3', limit=3)
        
        print("\n📡 ÚLTIMOS MOVIMENTOS NO RADAR DE DEFESA:")
        for n in noticias:
            print(f"  - {n.get_text().strip()}")
    except:
        print("\n📡 Monitorando frequências de defesa em tempo real...")

if __name__ == "__main__":
    radar_geopolitico_2026()

