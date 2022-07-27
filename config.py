import pymongo
import certifi


connection_string = "mongodb+srv://FSDI30:Tec.1234567890@cluster0.4pwow3y.mongodb.net/?retryWrites=true&w=majority"


client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())


db = client.get_database("Store")
