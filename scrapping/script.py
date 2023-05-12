from bs4 import BeautifulSoup
import mysql.connector
import requests

try:
    page = requests.get(f"https://www.etsy.com/fr/c/?ref=cat_back_arrow&explicit=1")
    def main(page):
        cnx = mysql.connector.connect(user='root', password='BTlfo9malmo9atila10#',
                                      host='127.0.0.1', database='ecom')
        cursor = cnx.cursor()

        src=page.content

        soup = BeautifulSoup(src,"html.parser")

        produits = soup.find_all("li", {'class': 'wt-list-unstyled'})
        for produit in produits:
            produit_nom = produit.find('h3').text.strip()
            produit_prix = produit.find("span", {'class': 'currency-value'}).text.strip().replace(',', '.')
            produit_image_tag = produit.find('img')
            produit_image = produit_image_tag['src']
            produit_categorie = 1
            description = ""
            quantite = 1000
            query = "INSERT INTO boutique_produit(designation,description,prix,image,quantite,categories_id) VALUES(%s,%s,%s,%s,%s,%s)"
            values = (produit_nom, description, float(produit_prix), produit_image, quantite, produit_categorie)
            cursor.execute(query, values)
            cnx.commit()
        cursor.close()
        cnx.close()

        '''
        categories = soup.find_all("div",{'class': 'category-grid-text-width-center'})
        
        def get_cat_info(categories):
            for category in categories:
                cat_title = category.contents[1].text.strip()
                print(cat_title)
        get_cat_info(categories)
        

        for category in categories:
            name = category.find('p', {'class': 'ingress-title'}).text.strip()
            query = "INSERT INTO boutique_categorie (nom_categorie) VALUES (%s)"
            values = (name,)
            cursor.execute(query, values)
            cnx.commit()
        cursor.close()
        cnx.close()
        '''



    main(page)
except mysql.connector.Error as error:
    print("Error occurred during database operation:", error)