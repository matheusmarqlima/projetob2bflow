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

