### PUT and DELETE --- HTTP Verbs 
### Working with API's --- json

from flask import Flask,jsonify,request


app = Flask(__name__)
##Initial data in my list
items = [
{"id":1,"name":"Item1","description":"This is the item1"},
{"id":2,"name":"Item2","description":"This is the item2"},
]


@app.route("/")
def home():
    return "Welcome to the sample TO DO list app"

#GET:Retrive all the items
@app.route("/items",methods=['GET'])
def get_items():
    return jsonify(items)

##Get: Retrive the specific items by id
@app.route("/items/<int:item_id>",methods =['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    return jsonify(item)

##Post : Create a new task

@app.route("/items",methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'item not found'})
    new_item = {
        "id":items[-1]['id'] +1 if items else 1,
        'name':request.json['name'],
        'description':request.json['description']

    }
    items.append(new_item)
    return jsonify(new_item)

##Put : Update an existing items

@app.route("/items/<int:item_id>",methods = ['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'Item not found'})
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)


if __name__ == "__main__":
    app.run(debug=True)