import time

def capturar_noticias():
    # Temas de interesse do Oráculo: Tecnologia e Rússia
    temas = ["Tecnologia Avançada", "Geopolítica Rússia", "Segredos Governamentais"]
    print(f"🤖 [SENTINEL] Iniciando captura nos temas: {temas}")
    
    # Simulando uma captura de banco de dados ou API
    noticias = [
        "Nova tecnologia russa de IA detectada.",
        "Avanço em sistemas de criptografia quântica.",
        "Movimentação cibernética no leste europeu."
    ]
    
    for noticia in noticias:
        print(f"✅ Notícia capturada: {noticia}")
        time.sleep(1) # Simula o tempo de processamento

if __name__ == "__main__":
    print("--- SISTEMA ORÁCULO SENTINEL ATIVADO ---")
    print("Desenvolvido por Crispim")
    capturar_noticias()

