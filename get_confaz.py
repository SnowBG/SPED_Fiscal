import requests
from bs4 import BeautifulSoup as bs


class atos_pmpf():
    
    def pega_links_por_ano(self):
        page = requests.get('https://www.confaz.fazenda.gov.br/legislacao/atos-pmpf', verify=False)
        sp = bs(page.content, 'html.parser')
        links=[]
        for link in sp.find_all('a'):
            links.append(link.get('href'))
            links = [l for l in links if l is not None]
        links_anos = [links[l] for l, lk in enumerate(links) if 'atos-pmpf/2' in lk]
        return links_anos


    def pega_links_dos_atos(self):
        links = self.pega_links_por_ano()
        links_at=[]
        for link in links:
            page = requests.get(link, verify=False)
            sp = bs(page.content, 'html.parser')
            for link in sp.find_all('a'):
                links_at.append(link.get('href'))
                links_at = [l for l in links_at if l is not None]
        links_atos = [links_at[l] for l, lk in enumerate(links_at) if '/pmpf0' in lk]
        return links_atos


    def pega_tabela(self):
        links = self.pega_links_dos_atos()
        table = []
        for link in links:
            page = requests.get(link, verify=False)
            sp = bs(page.content, 'html.parser')
            for tb in sp.find_all('table'):
                table.append(tb)
        return table

    
    def grava_arquivo(self, path, file_name):
        
    

a = atos_pmpf()
a.pega_tabela()

    
    
