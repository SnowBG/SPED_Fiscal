'''
Autor: Emerson Lara
Descrição: Este programa busca tabelas no site da CONFAZ relativas aos
preços médios ponderado ao consumidor final (PMPF) de combustíveis
dos atos COTEPE/PMPF a partir de 2010.
'''
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
import pandas as pd
import re


class atos_pmpf():
    '''
    Classe que orquestra o webscrap.
    '''

    def pega_links_por_ano(self):
        '''
        Acessa a seção dos atos-pmpf e retorna a lista de links para cada
        página dos anos a partir de 2010.
        '''

        page = requests.get('https://www.confaz.fazenda.gov.br/'
                            'legislacao/atos-pmpf',
                            verify=False)
        sp = bs(page.content, 'html.parser')
        links = []
        for link in sp.find_all('a'):
            links.append(link.get('href'))
            links = [l for l in links if l is not None]
        links_anos = [links[l] for l, lk in enumerate(links)
                      if 'atos-pmpf/201' in lk]
        is_instance = isinstance(links_anos, list)
        print(is_instance)
        return links_anos

    def pega_links_dos_atos(self):
        '''
        Acessa a seção da lista de atos no ano e retorna a lista de
        links para cada ato, dentro do ano específico.
        '''
        links = self.pega_links_por_ano()
        links_at = []
        for link in links:
            page = requests.get(link, verify=False)
            sp = bs(page.content, 'html.parser')
            for link in sp.find_all('a'):
                links_at.append(link.get('href'))
                links_at = [l for l in links_at if l is not None]
        links_atos = [links_at[l] for l, lk in enumerate(links_at)
                      if '/pmpf0' in lk]
        return links_atos

    def pega_tabela(self):
        '''
        Acessa a seção das tabelas contidas em cada ato, transforma o HTML
        em um DataFrame e converte os dados para planilha XLSX separando um
        arquivo por ato quinzenal.
        '''
        links = self.pega_links_dos_atos()
        for link in links:
            table = ""
            now = dt.now()
            page = requests.get(link, verify=False)
            sp = bs(page.content, 'html.parser')
            for tb in sp.find_all('table'):
                table = table+str(tb)
            self.seleciona_por_uf("", "tabela_"+link[-10:] +
                                  "_"+str(now.microsecond),
                                  ".html", str(table),
                                  'MG')
        return table

    def seleciona_por_uf(self, path, file_name, extention, data, *UF):
        '''
        Acessa a seção das tabelas contidas em cada ato, transforma o HTML
        em um DataFrame e converte os dados para planilha XLSX separando um
        arquivo por ato quinzenal e por Unidade Federal.
        '''
        links = self.pega_links_dos_atos()
        for link in links:
            page = requests.get(link, verify=False)
            parsed_data = bs(page.content, 'html.parser')
            tbl = {}
            for line in parsed_data.find_all('tr')[3:]:
                cells = line.find_all('td')
                state = re.match(r'\*?([A-Z]{2})', cells[0].p.string)
                if state:
                    tbl[state.group(1)] = [i.p.string for i in cells[1:]]
            if UF:
                with open(path+file_name+".csv", 'w') as file:
                    file.write(tbl[UF])

    def grava_arquivo(self, path, file_name, extention, data):
        dados = data
        df = pd.read_html(dados)
        df_p = pd.DataFrame(df[0])
        df_p.drop([0], inplace=True)
        df_p.to_excel(path+file_name+".xlsx", sheet_name="Atos PMPF",
                      header=0)


a = atos_pmpf()
a.pega_tabela()
