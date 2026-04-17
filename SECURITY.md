# Política de Segurança -- ScholarLens

## Versões Suportadas

| Versão | Suportada |
| ------ | --------- |
| 2.0.x  | sim       |

## Credenciais

A chave SerpApi deve ser fornecida via variável de ambiente `SERPAPI_KEY`. Nunca commite em código.

## Reportando

1. **Não** abra issue pública
2. Email ao mantenedor com descrição, passos e impacto

## Tempo de Resposta

- Recebimento: 48h
- Avaliação: 7 dias
- Correção: 30 dias

## Escopo

- `src/scholarlens/`
- CI/CD
- Scripts de instalação

## Fora do Escopo

- Vulnerabilidades em `aiohttp`, `beautifulsoup4`, `pandas`, `serpapi` (reporte upstream)
- Disponibilidade do SerpApi
