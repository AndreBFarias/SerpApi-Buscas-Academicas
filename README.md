<div align="center">
  
[![Licença](https://img.shields.io/badge/licença-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![Estrelas](https://img.shields.io/github/stars/AndreBFarias/SerpApiBuscasAcademicas.svg?style=social)](https://github.com/AndreBFarias/SerpApi-Buscas-Academicas/)
[![Contribuições](https://img.shields.io/badge/contribuições-bem--vindas-brightgreen.svg)](https://github.com/AndreBFarias/SerpApiBuscasAcademicas/issues)

<div style="text-align: center;">
  <h1 style="font-size: 2em;">SerpApi para Buscas Acadêmicas</h1>
  <img src="assets/logo.png" width="200" text-align= "center" alt="Ícone Acadêmico">
</div>
</div>
Uma ferramenta open source para buscas acadêmicas via SerpApi (Google Scholar), com coleta assíncrona, formatação, extração de conteúdo e ranking de domínios/compartilhamentos. Útil para mapear tendências em papers, citações e impacto social – perfeito para pesquisadores, lobistas ou analistas de dados caçando insights em temas como "mudanças climáticas" ou "IA regulatória".


---

## Pré-requisitos

- Python 3.8 ou superior.
## Pacotes: 
- serpapi
- aiohttp
- beautifulsoup4
- pandas
- urllib

## Instalação

```bash
# Instale pacotes:
pip install serpapi aiohttp beautifulsoup4 pandas
```

### Uso
- Configure sua chave SerpApi como variável de ambiente (SERPAPI_KEY).
- Execute Coleta_Academica_SerpApi.py com sua query e páginas.
- Prossiga com Formatacao_Resultados.py, Extracao_Conteudo.py (passando links) e Ranking_Dominios_Compartilhamentos.py.

### Exemplo:

```python import asyncio
asyncio.run(main('sua_chave', 'sua_query', num_pages=3))
```

### Dependências
>Bibliotecas open source para buscas e análise.

### Licença GLP 
> Livre para modificar e usar em rituais arcanos desde que tudo permaneça livre.
