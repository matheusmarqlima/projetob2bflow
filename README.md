# 📰 Coletor de Notícias G1 - Desafio b2bflow

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-green)
![Licence](https://img.shields.io/badge/licence-MIT-green)

## 💬 Sobre o Projeto

Este projeto é um script de web scraping desenvolvido em Python como parte do desafio técnico para o processo seletivo de **Estágio de Desenvolvedor(a) Python** da **b2bflow ⚡**.

O objetivo do script é navegar de forma automatizada até o portal de notícias G1, coletar as manchetes principais da página inicial e salvar essas informações (título e link) em um arquivo de texto local.

## 🛠️ Tecnologias Utilizadas

* **Python 3.8+**
* **Requests:** Para realizar as requisições HTTP e buscar o conteúdo da página web.
* **Beautiful Soup 4:** Para parsear o HTML e encontrar as informações desejadas de forma eficiente e simples.

## 🚀 Como Executar

Para rodar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

* Você precisa ter o **Python 3** e o gerenciador de pacotes **pip** instalados.

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/matheusmarqlima/desafio-b2bflow.git](https://github.com/matheusmarqlima/desafio-b2bflow.git)
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd desafio-b2bflow
    ```

3.  **(Recomendado) Crie e ative um ambiente virtual:**
    Isso mantém as dependências do projeto isoladas do seu sistema.

    ```bash
    # Criar o ambiente
    python -m venv venv
    ```

    ```bash
    # Ativar o ambiente (Windows)
    .\venv\Scripts\activate
    ```
    ```bash
    # Ativar o ambiente (macOS/Linux)
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    O arquivo `requirements.txt` lista tudo o que o projeto precisa.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute o script:**
    Agora é só rodar o arquivo principal!
    ```bash
    python coletor_noticias.py
    ```

Pronto! As mensagens do processo aparecerão no seu terminal e, ao final, o arquivo `manchetes_g1.txt` estará na pasta.

## 👨‍💻 Autor

Feito com ❤️ por **Matheus Marques de Lima**.

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matheus-marques-de-lima-b8177a297)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/matheusmarqlima)

## 🙏 Agradecimentos

Obrigado à equipe da **b2bflow** pela oportunidade e pelo desafio interessante!
