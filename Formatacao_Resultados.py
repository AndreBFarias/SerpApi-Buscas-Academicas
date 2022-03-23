# Ritual de Magia Negra Digital: Formatacao_Resultados.py - Alquimia de dados brutos, transmutando caos em elixires tabulares para análise sedutora.
# Explicação do Ritual: Formatacao_Resultados.md

# 1. Carrega resultados raw de JSON.
# 2. Formata em DataFrame Pandas, extraindo campos chave.
# 3. Filtra por citações mínimas e remove duplicatas.
# 4. Exporta para CSV.
# 5. Função principal que executa o fluxo.
import pandas as pd
import json

# 1
def load_raw_results(filename='raw_academic_results.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# 2
def format_to_dataframe(results):
    df = pd.DataFrame(results)
    df['title'] = df['title'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    df['link'] = df['link'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    df['snippet'] = df['snippet'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    df['authors'] = df.get('publication_info', {}).apply(lambda x: x.get('authors', []) if isinstance(x, dict) else [])
    df['citation_count'] = df.get('inline_links', {}).apply(lambda x: x.get('cited_by', {}).get('total', 0) if isinstance(x, dict) else 0)
    return df[['title', 'link', 'snippet', 'authors', 'citation_count']]

# 3
def filter_relevant_results(df, min_citations=0):
    return df[df['citation_count'] >= min_citations].drop_duplicates(subset=['link'])

# 4
def export_formatted(df, filename='formatted_academic_results.csv'):
    df.to_csv(filename, index=False, encoding='utf-8')

# 5
def main():
    results = load_raw_results()
    df = format_to_dataframe(results)
    filtered_df = filter_relevant_results(df)
    export_formatted(filtered_df)
    return filtered_df

# "A ordem nasce do caos, como a beleza surge da escuridão." — Friedrich Nietzsche