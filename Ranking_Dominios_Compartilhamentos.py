# Ritual de Magia Negra Digital: Ranking_Dominios_Compartilhamentos.py - Encantamento de métricas, forjando rankings como correntes que medem influência acadêmica.
# Explicação do Ritual: Ranking_Dominios_Compartilhamentos.md

# 1. Carrega resultados formatados de CSV.
# 2. Conta domínios dos links.
# 3. Adiciona métricas de compartilhamentos (de dados externos).
# 4. Calcula score e rankea.
# 5. Exporta ranking para CSV.
# 6. Função principal que executa com sharing opcional.
import pandas as pd
from urllib.parse import urlparse

# 1
def load_formatted_results(filename='formatted_academic_results.csv'):
    return pd.read_csv(filename)

# 2
def count_domains(df):
    df['domain'] = df['link'].apply(lambda x: urlparse(x).netloc if isinstance(x, str) else '')
    domain_counts = df['domain'].value_counts().reset_index()
    domain_counts.columns = ['domain', 'count']
    return domain_counts

# 3
def add_sharing_metrics(domain_df, sharing_data):
    # Assumindo sharing_data como dict {domain: shares}
    domain_df['shares'] = domain_df['domain'].map(sharing_data).fillna(0)
    return domain_df

# 4
def rank_domains(df):
    df['score'] = df['count'] + df['shares']
    return df.sort_values(by='score', ascending=False)

# 5
def export_ranking(df, filename='ranking_domains.csv'):
    df.to_csv(filename, index=False, encoding='utf-8')

# 6
def main(sharing_data={}):
    df = load_formatted_results()
    domain_df = count_domains(df)
    domain_df = add_sharing_metrics(domain_df, sharing_data)
    ranked_df = rank_domains(domain_df)
    export_ranking(ranked_df)
    return ranked_df

# "A influência é a sombra que se alonga sobre os fracos." — Ayn Rand