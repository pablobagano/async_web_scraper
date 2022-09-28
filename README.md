# Projeto Final - Curso Python Pro Mentorama
## O projeto em questão é um Web Scraper Assíncrono, criado com a biblioteca aiohttpp.
Todas as bibliotecas necessárias estão contidas no arquivo 'requirements.txt'
### A função 'main'é alimentada com um endereço web que passa por três estágios:
####  1 - A biblioteca BeautifulSoup extrai as informações do site e cria uma lista com todos os sites contidos no endereço
####  2 - Cada link da lista passa pelo BeautifulSoup que, assincronicamente, captura os títulos de cada um dos links e os armazena numa lista
####  3 - A lista é renderizada num template e exibida ao usuário

