# Ritual de Magia Negra Digital: Coleta_Academica_SerpApi.py - Invocação das sombras acadêmicas, conjurando papers como ecos de saberes proibidos via SerpApi.
# Explicação do Ritual: Coleta_Academica_SerpApi.md

# 1. Função assíncrona para buscar resultados individuais via SerpApi.
# 2. Coleta resultados em páginas múltiplas de forma assíncrona para eficiência.
# 3. Salva resultados raw em JSON.
# 4. Função principal que orquestra a coleta e salva.
import asyncio
import aiohttp
from serpapi import GoogleSearch

# 1
async def fetch_scholar_results(session, params):
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get('organic_results', [])

# 2
async def collect_results(api_key, query, num_pages=1, engine='google_scholar'):
    params = {
        'api_key': api_key,
        'engine': engine,
        'q': query,
        'num': 10
    }
    async with aiohttp.ClientSession() as session:
        tasks = []
        for page in range(num_pages):
            params['start'] = page * 10
            tasks.append(fetch_scholar_results(session, params.copy()))
        all_results = await asyncio.gather(*tasks)
        flattened = [item for sublist in all_results for item in sublist]
        return flattened

# 3
def save_raw_results(results, filename='raw_academic_results.json'):
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

# 4
async def main(api_key, query, num_pages=1):
    results = await collect_results(api_key, query, num_pages)
    save_raw_results(results)
    return results

# "O conhecimento é o veneno que liberta a mente das correntes da ignorância." — Friedrich Nietzsche