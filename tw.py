import plotly.express as px

# Dados de exemplo (substitua com seus dados reais)
usuarios = ['Usuario1', 'Usuario2', 'Usuario3']
contagens = [100, 200, 150]

# Criar figura e plotar gráfico de barras
fig = px.bar(x=usuarios, y=contagens)
fig.show()
