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

- Python 3.8 ou superior
- Chave de API SerpApi (gratuita para até 100 buscas/mês em [serpapi.com](https://serpapi.com))

---

## Instalação

```bash
git clone https://github.com/AndreBFarias/SerpApi-Buscas-Academicas.git
cd SerpApi-Buscas-Academicas
pip install -r requirements.txt
```

---

## Configuração

Exporte sua chave de API antes de executar:

```bash
export SERPAPI_KEY="sua_chave_aqui"
```

---

## Uso

Execute os scripts na seguinte ordem:

### 1. Coleta de dados

```bash
python Coleta_Academica_SerpApi.py --query "inteligência artificial regulatória" --paginas 5
```

### 2. Formatação dos resultados

```bash
python Formatacao_Resultados.py
```

### 3. Extração de conteúdo

```bash
python Extracao_Conteudo.py --links links.csv
```

---

### Licença GLP
> Livre para modificar e usar em rituais arcanos desde que tudo permaneça livre.
