# Changelog

## [2.0.0] - 2026-04-16

### Mudado
- Projeto renomeado de `SerpApi-Buscas-Academicas` para `ScholarLens` (sprint S17 do portfólio)
- Código reorganizado em `src/scholarlens/` (layout src)
- Scripts renomeados para PT-BR curto: `coleta.py`, `extracao.py`, `formatacao.py`, `ranking.py`
- Removidos cabeçalhos "Ritual de Magia Negra Digital" de todos os scripts
- Removido `__init__.py` raiz com imports quebrados
- `pyproject.toml` corrigido: build-backend válido (setuptools.build_meta), nome `scholarlens`, deps pinadas

### Adicionado
- 6 testes pytest (formatacao.filter_relevant_results, ranking.count_domains/add_sharing_metrics/rank_domains)
- `.github/workflows/ci.yml` (ruff + pytest)
- `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `.mailmap`

## [1.0.0] - 2024-11-30

### Adicionado
- Coleta assíncrona de papers via SerpApi (Google Scholar)
- Extração paralela de conteúdo de URLs via aiohttp + BeautifulSoup
- Formatação em DataFrame Pandas
- Ranking de domínios por contagem e compartilhamentos
