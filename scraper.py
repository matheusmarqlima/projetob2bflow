import datetime  
import sys       

# --- Verificação de Ferramentas Essenciais ---

try:
    import requests  
    from bs4 import BeautifulSoup  
except ImportError:
    # Se não encontrar as ferramentas, avisamos o usuário 
    print("\n--- Opa! Parece que faltam algumas ferramentas na sua caixa. ---")
    print("Para este script funcionar, precisamos das bibliotecas 'requests' e 'beautifulsoup4'.")
    print("Você pode instalá-las facilmente. Abra seu terminal e digite:")
    print("\npip install requests beautifulsoup4\n")
    print("------------------------------------------------------------------")
    sys.exit(1)  # Encerra o programa 

def buscar_noticias_do_g1():
    """
    Navega até a página inicial do G1 e procura pelas últimas notícias, guardando o título e o link de cada uma.
    Retorna uma lista com as notícias encontradas ou nada (None) se houver um problema.
    """
    url_alvo = "https://g1.globo.com/"
    
    
    # Usar cabeçalho de "User-Agent" para que o site pense que é um navegador comum que está acessando a página.
    cabecalhos = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print("🚀 Olá! Começando a buscar as últimas notícias no G1...")
