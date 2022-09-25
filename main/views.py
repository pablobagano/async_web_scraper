from urllib import request
from django.shortcuts import render
from django.views import View
import asyncio
from asyncio import gather, get_event_loop, ensure_future
from bs4 import BeautifulSoup 
from requests import get
from aiohttp import ClientSession
import lxml

"""
A função 'main'é alimentada com um endereço web que passa por três estágios:
1 - A biblioteca BeautifulSoup extrai as informações do site e cria uma lista com todos os sites contidos no endereço
2 - Cada link da lista passa pelo BeautifulSoup que, assincronicamente, captura os títulos de cada um dos links e os armazena numa lista
3 - A lista é renderizada num template e exibida ao usuário
"""


async def main(request):
    async with ClientSession() as session:
        async with session.get('https://www.giannini.com.br/') as resp:
            assert resp.status == 200
            links = []
            titles = []
            data = await resp.text()
            soup = BeautifulSoup(data, 'lxml')
            soup_title = soup.title.text
            for link in soup.find_all("a", href=True):
                if link['href'].startswith('http') is True:
                        if 'facebook.com/login' not in link['href'] and 'instagram.com/accounts/login' not in link['href']:
                            links.append(link['href'])
            for title in links:
                async with ClientSession() as session:
                    async with session.get(title) as resp:
                        try:
                            url = await resp.text()
                            soup = BeautifulSoup(url,'lxml')
                            title = soup.title.text
                        except AttributeError:
                            not titles.append(title)
                        finally:
                            if title not in titles:
                                titles.append(title)
                        if len(titles) == 10:
                            break
    return render(request, 'index.html', {'soup':soup_title, 'list':titles} )
