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
    
    try:
        # Vamos tentar "visitar" a página. Tempo de 10 segundos para o site responder
        resposta = requests.get(url_alvo, headers=cabecalhos, timeout=10)
        
        # Se a resposta for um código de erro, paramos aqui.
        resposta.raise_for_status()

        # Agora, entregamos o HTML da página para o BeautifulSoup
        pagina_organizada = BeautifulSoup(resposta.content, 'html.parser')

        # Identificamos onde estão as manchetes que queremos.
        lista_de_manchetes = pagina_organizada.find_all('a', class_='feed-post-link')

        if not lista_de_manchetes:
            print("⚠️ Puxa, não encontrei nenhuma manchete onde eu costumava procurar.")
            print("Pode ser que a estrutura do site G1 tenha mudado.")
            return None

        noticias_coletadas = []
        for manchete in lista_de_manchetes:
            titulo = manchete.get_text(strip=True)  # Pega o texto limpo do link
            link = manchete['href']                 # Pega o endereço do link
            
            # Guarda a noticia se tiver título e link
            if titulo:
                noticias_coletadas.append({'titulo': titulo, 'link': link})

        print(f"✅ Sucesso! Encontrei {len(noticias_coletadas)} notícias fresquinhas.")
        return noticias_coletadas
        # Em caso de erro do site
    except requests.exceptions.HTTPError as erro:
        print(f"❌ Problema de HTTP: {erro}. A página pode estar fora do ar ou a URL mudou.")
    except requests.exceptions.ConnectionError:
        print("❌ Problema de Conexão. Parece que você está sem internet. Pode verificar?")
    except requests.exceptions.Timeout:
        print("❌ O site demorou demais para responder. Tente novamente mais tarde.")
    except Exception as erro_geral:
        print(f"❌ Encontrei um erro inesperado: {erro_geral}")
    
    return None

def salvar_dados(dados_das_noticias):
    """
    Pega a lista de notícias e salva tudo de forma organizada em um arquivo de texto.
    """
    if not dados_das_noticias:
        print("Como não coletei dados, não há nada para salvar.")
        return

    nome_do_arquivo = "manchetes_g1.txt"
    data_e_hora = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

    try:
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(f"Manchetes do G1\n")
            arquivo.write(f"Coletadas em: {data_e_hora}\n")
            arquivo.write("="*40 + "\n\n")

            for noticia in dados_das_noticias:
                arquivo.write(f"Título: {noticia['titulo']}\n")
                arquivo.write(f"Link: {noticia['link']}\n")
                arquivo.write("-"*40 + "\n")

        print(f"💾 Perfeito! Todas as notícias foram salvas no arquivo '{nome_do_arquivo}'")

    except IOError as e:
        print(f"❌ Tive um problema ao tentar criar o arquivo: {e}")

# --- Programa ---

if __name__ == "__main__":
    
    # Inicializa para buscar as notícias do G1
    noticias = buscar_noticias_do_g1()
    
    # Caso retorne noticias, salva elas em um arquivo
    if noticias:
        salvar_dados(noticias)