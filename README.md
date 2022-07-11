[![opensource](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](#)
[![Licença](https://img.shields.io/badge/licença-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![Estrelas](https://img.shields.io/github/stars/AndreBFarias/SerpApiBuscasAcademicas.svg?style=social)](https://github.com/AndreBFarias/SerpApi-Buscas-Academicas/)
[![Contribuições](https://img.shields.io/badge/contribuições-bem--vindas-brightgreen.svg)](https://github.com/AndreBFarias/SerpApiBuscasAcademicas/issues)

# SerpApi para Buscas Acadêmicas

![Ícone Acadêmico](assets/logo.png)

Pipeline modular para buscas acadêmicas via SerpApi (Google Scholar). Realiza coleta assíncrona de papers, formatação de resultados, extração de conteúdo e geração de rankings por domínio e compartilhamentos. Útil para mapear tendências em publicações científicas, citações e impacto social de temas específicos.

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


### Licença GLP
> Livre para modificar e usar em rituais arcanos desde que tudo permaneça livre.
