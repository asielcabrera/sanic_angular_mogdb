from sanic import Sanic, response
from sanic_cors import CORS

from models.product import Products
from redis import Redis

import json
import os

redis = Redis(host=os.environ['REDIS_HOSTNAME'])
list_products_redis = "list_of_all_products"

score = 1

app = Sanic(__name__)
CORS(app)

app.static('', 'dist/sanic-angular')


@app.route("/")
def index(request):
    return response.file('./dist/sanic-angular/index.html')



@app.route('/api/product', methods=['GET'])
def get_products(request):
    results_redis = redis.get(list_products_redis)
    if not results_redis:
        data = []

        productos = Products.objects()

        if len(productos) > 0:
            for producto in productos:
                _id = producto.id

                data.append({"_id": str(_id), "name": producto.name, "description": producto.description})
                redis.setex(list_products_redis, 10 , str(data))
        
            return response.json({ "data": data})
    else:
        return response.json({ "data": json.loads(results_redis)})



@app.route('/api/product', methods=['POST'])
def add_products(request):
    
    data = request.json

    pro = Products.objects(name=data['name'])
    
    if len(pro) == 0:
        newProduct = Products(name= data['name'], description=data['description'], precio=data['precio'])
        newProduct.save()

    return response.json({
        "data": data
    })

@app.route('/api/product/<id>', methods=['DELETE'])
def remove_products(request, id):
    Products.objects(id=id).delete()
    return response.json({
    })

@app.route('/api/product/<id>', methods=['PUT'])
def update_products(request, id):
    data = request.json
    update = Products.objects(id=id)[0]
    update.name = data['name']
    update.description = data['description']
    # update.precio = data['precio']
    update.save()

    return response.json(update.to_json())

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)