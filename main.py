import pandas as pd
from twilio.rest import Client

account_sid = "AC32255c278cc5331740f22c6ac58671db"
auth_token  = "d6cf6955b18d6fd945c3e2288af2ac1a"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:                                                                  
    tabela_vendas =  pd.read_excel(f'{mes}.xlsx')    #Vai ler a tabela
    if (tabela_vendas['Vendas'] > 55000).any(): 
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5538991252366", 
            from_="+18608133282",
            body=f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)