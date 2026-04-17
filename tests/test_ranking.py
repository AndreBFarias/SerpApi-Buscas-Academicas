"""Testes para scholarlens.ranking."""

import pandas as pd

from scholarlens.ranking import add_sharing_metrics, count_domains, rank_domains


def test_count_domains_extrai_netloc():
    df = pd.DataFrame({
        "link": [
            "https://arxiv.org/abs/2301.00001",
            "https://arxiv.org/abs/2301.00002",
            "https://scholar.google.com/citations?user=x",
            "https://nature.com/articles/x",
        ]
    })
    resultado = count_domains(df)
    assert set(resultado["domain"]) == {
        "arxiv.org",
        "scholar.google.com",
        "nature.com",
    }
    arxiv = resultado[resultado["domain"] == "arxiv.org"]
    assert int(arxiv["count"].iloc[0]) == 2


def test_add_sharing_metrics_preenche_dominios_ausentes_com_zero():
    df = pd.DataFrame({"domain": ["a.com", "b.com"], "count": [3, 1]})
    sharing = {"a.com": 50}
    resultado = add_sharing_metrics(df, sharing)
    a = resultado[resultado["domain"] == "a.com"]
    b = resultado[resultado["domain"] == "b.com"]
    assert int(a["shares"].iloc[0]) == 50
    assert int(b["shares"].iloc[0]) == 0


def test_rank_domains_ordena_descendente_por_score():
    df = pd.DataFrame({
        "domain": ["a.com", "b.com", "c.com"],
        "count": [1, 5, 3],
        "shares": [10, 0, 20],
    })
    resultado = rank_domains(df)
    assert list(resultado["domain"]) == ["c.com", "b.com", "a.com"]
