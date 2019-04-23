import pymongo
import dns
import os
import sys
import pprint

def main():
    #url=mongodb+srv://mehufarm:<password>@cluster0-2rfy9.mongodb.net/test?retryWrites=true
    url = 'mongodb+srv://{}:{}@{}/{}'.format(
        os.environ["MONGO_USERNAME"],
        os.environ["MONGO_PASSWORD"],
        os.environ["MONGO_HOST"],
        os.environ["MONGO_DBNAME"]
    )

    client = pymongo.MongoClient(url)
    db = client[os.environ["MONGO_DBNAME"]]
    collection = db['start'] #put the name of your collection in the quotes

    #pprint.pprint(posts.find_one({'candy' : 'Hershey'}))
    #1. print the number of documents in collection
    print(collection.count_documents({}))
    #2. print the first document in the collection
    pprint.pprint(collection.find_one())
    #3. print all documents in the collection
    for x in collection.find():
        pprint.pprint(x)
    #4. print all documents with a particular value for some attribute
    for x in collection.find({"name" :"zia"}):
        pprint.pprint(x)
    #ex. print all documents with the birth date 12/1/1990


if __name__=="__main__":
    main()
