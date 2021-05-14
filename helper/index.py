from flask import Flask, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from classifier import imageRecog
import numpy
import cv2

app = Flask(__name__)
# REPLACE MONGOLINK WITH THE MONGODB LINK
# app.config["MONGO_URI"] = {MONGO LINK}
mongo = PyMongo(app)


@app.route('/flask', methods=['POST'])
def index():
    imgObj = mongo.db.images.find_one(
        {'_id': ObjectId(request.get_json()['id'])})
    image = cv2.imdecode(numpy.fromstring(
        imgObj['selectedFile'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
    tags = classifier(image)
    for tag in tags:
        imgObj['tags'].append(tag)
    mongo.db.images.find_one_and_update({'_id': ObjectId(request.get_json()['id'])}, {
                                        "$set": {"tags": imgObj['tags']}}, upsert=True)
    return "worked"


if __name__ == "__main__":
    app.run(port=8000, debug=True)
