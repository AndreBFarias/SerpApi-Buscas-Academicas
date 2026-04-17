"""Testes para scholarlens.formatacao."""

import pandas as pd

from scholarlens.formatacao import filter_relevant_results


def test_filter_relevant_results_aplica_minimo_citations():
    df = pd.DataFrame({
        "title": ["A", "B", "C"],
        "link": ["http://a", "http://b", "http://c"],
        "citation_count": [0, 5, 100],
    })
    resultado = filter_relevant_results(df, min_citations=5)
    assert len(resultado) == 2
    assert set(resultado["title"]) == {"B", "C"}


def test_filter_relevant_results_remove_duplicatas_por_link():
    df = pd.DataFrame({
        "title": ["A", "A duplicado", "B"],
        "link": ["http://a", "http://a", "http://b"],
        "citation_count": [10, 10, 10],
    })
    resultado = filter_relevant_results(df, min_citations=0)
    assert len(resultado) == 2


def test_filter_relevant_results_sem_filtro_retorna_tudo():
    df = pd.DataFrame({
        "title": ["A", "B"],
        "link": ["http://a", "http://b"],
        "citation_count": [0, 0],
    })
    resultado = filter_relevant_results(df, min_citations=0)
    assert len(resultado) == 2
