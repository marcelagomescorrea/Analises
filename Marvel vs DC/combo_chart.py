#Create combo chart
fig, ax1 = plt.subplots(figsize=(14,6))
ax2 = ax1.twinx()


#gráfico de barras usando o matplotlib
#ax1 = plt.subplot(111)
anos = dados_por_ano['Ano'].sort_values().unique()
w = 0.5

## barra da marvel
filmes_marvel = dados_por_ano[dados_por_ano['Compania'] == 'Marvel'].sort_values(
                                            by=['Ano'])['Quantidade de Filmes']
ax1.bar(anos - w/2, height=filmes_marvel, width=w, color = '#f4686b',
                 label='Marvel - Qtd. de Filmes')
# barra da DC
#filmes_dc = dados_por_ano[dados_por_ano['Compania'] == 'DC'].sort_values(
 #                                           by=['Ano'])['Quantidade de Filmes']
#ax1.bar(anos + w/2, height=filmes_dc, width=w, color = 'lightskyblue',
 #                label = 'DC - Qtd. de Filmes')


# adicionando os valores no topo das barras
#for idx, v in enumerate(anos):
 #   print('Teste {}|{}'.format(idx,v))
#    ax1.text(v - w/2 - 0.07, filmes_marvel.iloc[idx] + .02,
 #            str(int(filmes_marvel.iloc[idx])), color='#67090F')
    
 #   ax1.text(v + w/2 - 0.07, filmes_dc.iloc[idx] + .02,
 #            str(int(filmes_dc.iloc[idx])), color='darkblue')


ax1.set_xticks(anos)
ax1.legend()

# titulos
ax1.set_title('Marvel vs DC', { 'fontsize' : 20 })
ax1.set_ylabel('Quantidade de Filmes', { 'fontsize' : 16 })
ax1.set_xlabel('Ano', { 'fontsize' : 16 })


#gráfico de linha usando seaborn
sns.lineplot(x='Ano', y='Média da Nota', marker='o',
                 data = dados_por_ano, palette=['darkblue','#ad1019'], ax = ax2)

ax2.set_ylabel('Média da Nota', { 'fontsize' : 16 })
handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles=handles, labels=labels)



#show plot
plt.show()