# Ritual de Magia Negra Digital: Extracao_Conteudo.py - Raspar das profundezas, extraindo essências de páginas como almas despidas.
# Explicação do Ritual: Extracao_Conteudo.md

# 1. Função assíncrona para raspar conteúdo de uma URL, focando em parágrafos.
# 2. Extrai conteúdos de múltiplas URLs em paralelo.
# 3. Salva extraídos em JSON.
# 4. Função principal que orquestra a extração.
import asyncio
import aiohttp
from bs4 import BeautifulSoup

# 1
async def fetch_page_content(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                text = ' '.join([p.text for p in soup.find_all('p')])
                return {'url': url, 'content': text.strip()}
            return {'url': url, 'content': ''}
    except Exception:
        return {'url': url, 'content': ''}

# 2
async def extract_contents(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page_content(session, url) for url in urls]
        contents = await asyncio.gather(*tasks)
        return contents

# 3
def save_extracted_contents(contents, filename='extracted_contents.json'):
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(contents, f, ensure_ascii=False, indent=4)

# 4
async def main(urls):
    contents = await extract_contents(urls)
    save_extracted_contents(contents)
    return contents

# "As palavras são veias que sangram verdades ocultas." — Olavo de Carvalho