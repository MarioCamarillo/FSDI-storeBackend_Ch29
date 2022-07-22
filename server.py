import random
from flask import Flask, request
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

    # return "Not found"


@app.post("/api/products")
def save_products():
    product = request.get_json()
    ##########################################################
    # add product to the catalog
    # assign an id to the product
    # return product as a json
    ##########################################################
    mock_data.append(product)
    product["id"] = random.randrange(1, 1000)

    return json.dumps(product)


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
    # GET /api/categories
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

#####################################################
# get return the number of products in the catalog
# /api/count_products   (for us it's mock_data)
#####################################################


@app.get("/api/count_products")
def get_count_products():
    products_count = len(mock_data)
    return json.dumps({"products_count": products_count})


#######################################################
# get /api/search/<text>
# return all the products whose title contains <text>
#######################################################

@app.get("/api/search/<text>")
def get_search_title(text):
    print("Search for this text is:", text)
    title_results = []

    text = text.lower()
    for prod in mock_data:
        if text in prod["title"].lower():
            title_results.append(prod)

    return json.dumps(title_results)


app.run(debug=True)
