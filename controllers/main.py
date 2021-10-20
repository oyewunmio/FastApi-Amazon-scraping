import bs4

def list_products(is_best_seller, rating, product_name):
    """gets list of products from the platform"""

    # Read html
    e_commerce_html = open('pages/content.html', 'r')
    
    # Parse html
    soup = bs4.BeautifulSoup(e_commerce_html.read(), 'html.parser')
    

    # Gets all the products name based on respective tag class
    product_parent_tag = soup.find_all('div', attrs={'class':'a-section a-spacing-medium'})
    product_list = {}
    for tags in product_parent_tag:
        best_seller_status = tags.find('span', attrs={'class':'a-badge-text'}) #finds the tag holding the Mais vendida for each of the product
        # checks if products has best seller tag or not and set True or False to the best_seller variable. Then append all products to the dictionary product_list
        if best_seller_status == None:
            # not bestseller products
            non_best_seller_product_name = tags.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'}).text
            non_best_seller_price = tags.find('span', attrs={'class':'a-offscreen'}).text.replace('R$', '').strip().replace('.','').replace(',','.')
            best_seller = False
            non_best_seller_rating = tags.find('span', attrs={'class':'a-icon-alt'}).text.strip()
            reconstructed_non_best_seller_rating = float(non_best_seller_price[0]+'.'+non_best_seller_price[2])
            product_list[" ".join(non_best_seller_product_name.split())] = {'price':float(non_best_seller_price), 'best_seller':best_seller, 'rating':reconstructed_non_best_seller_rating}
        else:
            # bestseller products
            best_seller_product_name = tags.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'}).text
            best_seller_price = tags.find('span', attrs={'class':'a-offscreen'}).text.replace('R$', '').strip().replace('.','').replace(',','.')
            best_seller = True
            best_seller_rating = tags.find('span', attrs={'class':'a-icon-alt'}).text.strip()
            reconstructed_best_seller_rating = float(best_seller_price[0]+'.'+best_seller_price[2])
            product_list[" ".join(best_seller_product_name.split())] = {'price':float(best_seller_price), 'best_seller':best_seller, 'rating':reconstructed_best_seller_rating}
    
    #checking api url parameters to determine the kind of product list to return
    if is_best_seller == True:
        #loop to extract and return only best_seller products
        for keys,value in list(product_list.items()):
            for k,v in value.items():
                if v == False:
                    del product_list[keys] #removes non best seller from product list

        if rating != None: #checks if rating path parameter was given and extracts the products with a higher rating than the given value 
            rated_products = {}
            rating_compare = rating
            for keys,value in list(product_list.items()):
                for k,v in value.items():
                    if rating_compare < value['rating']: #checks for products with a greater rating that specified rating value
                        rated_products[keys] = value
            return rated_products
        else:
            return product_list
    
    elif is_best_seller == False:
        #loop to extract and return only non best_seller products
        for keys,value in list(product_list.items()):
            for k,v in value.items():
                if v == True:
                    del product_list[keys] #removes best_seller products from product list
        
        if rating != None: #checks if rating path parameter was given and extracts the products with a higher rating than the given value 
            rated_products = {}
            rating_compare = rating
            for keys,value in list(product_list.items()):
                for k,v in value.items():
                    if rating_compare < value['rating']: #checks for products with a greater rating that specified rating value
                        rated_products[keys] = value
            return rated_products
        else:
            return product_list
    
    else:
        # returns list of all products in absences of is_best_seller flag
        if rating != None: #checks if rating path parameter was given and extracts the products with a higher rating than the given value 
            rated_products = {}
            rating_compare = rating
            for keys,value in list(product_list.items()):
                for k,v in value.items():
                    if rating_compare < value['rating']:
                        rated_products[keys] = value
            return rated_products
        else:
            #extracts the name from the product list if the parameter product name is given
            if product_name != None:
                return product_list[product_name]

            return product_list


