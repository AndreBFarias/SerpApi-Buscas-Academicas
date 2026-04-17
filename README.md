[![Licença](https://img.shields.io/badge/licença-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/)
[![CI](https://github.com/AndreBFarias/ScholarLens/actions/workflows/ci.yml/badge.svg)](https://github.com/AndreBFarias/ScholarLens/actions/workflows/ci.yml)

# ScholarLens

![Ícone Acadêmico](assets/logo.png)

Pipeline modular para buscas acadêmicas via SerpApi (Google Scholar). Coleta assíncrona de papers, formatação de resultados, extração de conteúdo e ranking por domínio e compartilhamentos. Útil para mapear tendências em publicações científicas.

---

## Pré-requisitos

- Python 3.10 ou superior
- Chave SerpApi (gratuita até 100 buscas/mês em [serpapi.com](https://serpapi.com))

## Instalação

```bash
git clone https://github.com/AndreBFarias/ScholarLens.git
cd ScholarLens
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Configuração

```bash
export SERPAPI_KEY="sua_chave_aqui"
```

## Uso

```bash
# Formatação dos resultados já coletados
python -m scholarlens.formatacao

# Ranking
python -m scholarlens.ranking
```

Em scripts, use os módulos diretamente:

```python
import asyncio
from scholarlens.coleta import main as coletar
asyncio.run(coletar(api_key, "inteligencia artificial regulatoria", num_pages=5))
```

## Estrutura

```
ScholarLens/
  src/scholarlens/
    coleta.py        # Coleta assincrona via SerpApi
    extracao.py      # Extracao de conteudo HTML
    formatacao.py    # Normalizacao em DataFrame
    ranking.py       # Ranking por dominio
  tests/             # Testes pytest
  assets/            # Logo e recursos
  .github/workflows/ # CI
  pyproject.toml
  requirements.txt
```

## Testes

```bash
pytest tests/ -v
```

## Contribuição

Ver [CONTRIBUTING.md](CONTRIBUTING.md) e [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Segurança

Ver [SECURITY.md](SECURITY.md).

## Licença

GPL v3 -- ver [LICENSE](LICENSE).
