import pandas as pd

df=pd.read_csv('risco_credito.csv')
df[df['risco']=='alto'].apply(pd.Series.value_counts)
# se garantias = NENHUMA então RISCO=ALTO
df[(df['risco']=='alto') & (df['garantias']=='nenhuma')].apply(pd.Series.value_counts)
# se garantias = NENHUMA e divida = ALTA então RISCO=ALTO
df[(df['risco']=='alto') & (df['garantias']=='nenhuma') & (df['divida']=='alta')].apply(pd.Series.value_counts)
# se garantias = NENHUMA e divida = ALTA e historia = ruim então RISCO=ALTO
df[(df['risco']=='alto') & (df['garantias']=='nenhuma') & (df['divida']=='alta') & (df['historia']=='ruim')].apply(pd.Series.value_counts)
# se garantias = NENHUMA e divida = ALTA e historia = RUIM e renda = 0_15 então RISCO=ALTO
df[(df['risco']=='alto') & (df['garantias']=='nenhuma') & (df['divida']=='alta') & (df['historia']=='ruim') & (df['renda']=='0_15')].apply(pd.Series.value_counts)
