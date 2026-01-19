## PUt and delete - Http verbs
## working with apis-- JSON


from flask import Flask,jsonify,request

app = Flask(__name__)


## Initial Data in my to do list 
items=[
    {"id":1,"name":"Item1","description":"This is item1"},
    {"id":2,"name":"Item2","description":"This is item2"}
]


@app.route('/')
def home():
    return "Welcome to sample to do list"


## Get: Retrive all items
@app.route('/items',methods=['GET'])
def getitems():
    return  jsonify(items)

## get: retrieve a specific item by id
@app.route('/items/<int:item_id>',methods=['GET'])
def getitem(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return  jsonify({"error":"item not found"})
    return jsonify(item)

## POST : create a new task
@app.route('/items',methods=['POST'])
def createitem():
    if not request.json or not 'name' in request.json:
         return  jsonify({"error":"item not found"})
        
    newitem={
        "id": items[-1]["id"] +1 if items else 1,
        "name": request.json['name'],
        "description":request.json['description'],
    }
    items.append(newitem)
    return jsonify(newitem)

# PUT: Update an existing item
@app.route('/items/<int>:item_id>',methods=['PUT'])
def updateitem(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)


# Delete: Delete an item
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items=[item for item in items if item["id"]!=item_id]
    return jsonify({"result":"Item deleted"})



if __name__ == '__main__':
    app.run(debug=True)