from unittest import mock
from flask import Flask
from about import me
from data import mock_data
import json


app = Flask("server")


@app.get("/")
def home():
    return "Hello from Flask!"


@app.get("/test")
def test():
    return "This is just a simple test!"


@app.get("/about")
def about():
    return "My name is Mario"


############################################################################
# API ENDPOINTS = PRODUCTS
############################################################################

@app.get("/api/version")
def version():
    return "1.0"


@app.get("/api/about")
def about_me():
    return json.dumps(me)
# return f'{me["first"]} {me["last"]}'


########################################################################
## get /api/products
# return mock_data as json string
########################################################################
@app.get("/api/products")
def products():
    return json.dumps(mock_data)


@app.get("/api/products/<id>")
def get_products_by_id(id):
    for prod in mock_data:
        if str(prod["id"]) == id:
            return json.dumps(prod)

    return "Not found"

#############################################################
# GET api/products_category/<category>
# return all products category whose category is
#
# create a results list
# travel the list, get every product category
# add products to a list
# outside the for loop, return the result as a json
#############################################################


@app.get("/api/products_category/<category>")
def get_product_by_category(category):
    print("your category ", category)
    results = []
    category = category.lower()
    for products in mock_data:
        if products["category"].lower() == category:
            results.append(products)
    return json.dumps(results)


#########################################################################
# GET /api/products_cheapest
########################################################################
@app.get("/api/products_cheapest")
def get_product_cheapest():
    product_cheapest = mock_data[0]
    for product in mock_data:
        if product["price"] < product_cheapest["price"]:
            product_cheapest = product
    return json.dumps(product_cheapest)

    ########################################################################
    ## GET /api/categories
    # 1- Return ok
    # 2- travel mock_data, and print the category of every product
    # 3- put the category in a list and at the end of the for loop, return the list as json
    ########################################################################


@app.get("/api/categories")
def get_categories():

    categories = []

    for product in mock_data:
        cat = product["category"]
        if not cat in categories:
            print(product["category"])
            categories.append(cat)

    return json.dumps(categories)


app.run(debug=True)
