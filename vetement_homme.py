# import the bibliothéque
import pandas as pd
from requests import get
from bs4 import BeautifulSoup as bs


#pour les vêtements
def get_info_vetement(containers):
    list = []
    for container in containers:
        link_image = container.find('a','card-image ad__card-image waves-block waves-light').img['src']
        price = container.find('p','ad__card-price').a.text
        adress = container.find('p','ad__card-location').span.text
        type = container.find('p','ad__card-description').a.text
        dic = {
            "type":type,
            "adress":adress,
            "price":price,
            "link_image":link_image
        }
        list.append(dic)
    return list



#function for getting type vetements
def main_info_vetement(size_page):
    DF = pd.DataFrame()
    for index in range(size_page):
        url = f'https://sn.coinafrique.com/categorie/vetements-homme?page={index}'
        html_content = get(url)
        request = bs(html_content.content,'html.parser')
        containers = request.find_all('div','col s6 m4 l3')
        data_list = get_info_vetement(containers)
        DF = pd.concat([DF,pd.DataFrame(data_list)],axis=0).reset_index(drop=True)
    return DF
