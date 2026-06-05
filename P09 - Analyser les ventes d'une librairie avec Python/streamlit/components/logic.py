import pandas as pd


def get_kpi(df_current, df_prev):
    """
    Calcule les KPIs du mois courant + delta vs mois précédent.

    Args:
        df_current : DataFrame filtré sur le mois courant
        df_prev    : DataFrame filtré sur le mois précédent (mêmes filtres)
    """

    def safe_idxmax(series):
        return series.idxmax() if not series.empty else "-"

    def safe_max(series):
        return series.max() if not series.empty else 0

    # --- Mois courant ---
    ca = df_current['price'].sum()
    catalogue = df_current['id_prod'].nunique()
    clients_unique = df_current['client_id'].nunique()
    sessions = df_current['session_id'].nunique()
    panier_moyen = ca / sessions if sessions > 0 else 0

    ca_categ = df_current.groupby('categ', observed=True)['price'].sum()
    best_categ_name = safe_idxmax(ca_categ)
    best_categ_value = safe_max(ca_categ)

    # --- Mois précédent (deltas) ---
    ca_prev = df_prev['price'].sum()
    clients_prev = df_prev['client_id'].nunique()
    sessions_prev = df_prev['session_id'].nunique()
    panier_moyen_prev = ca_prev / sessions_prev if sessions_prev > 0 else 0

    return {
        "ca": ca,
        "ca_delta": ca - ca_prev,
        "sessions": sessions,
        "sessions_delta": sessions - sessions_prev,
        "clients_unique": clients_unique,
        "clients_delta": clients_unique - clients_prev,
        "panier_moyen": panier_moyen,
        "panier_moyen_delta": panier_moyen - panier_moyen_prev,
        "catalogue": catalogue,
        "best_categ_name": best_categ_name,
        "best_categ_value": best_categ_value,
    }
