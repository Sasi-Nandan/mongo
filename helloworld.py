from pymongo import MongoClient
import gridfs
db = MongoClient().gridfs_example
fs = gridfs.GridFS(db)
a = fs.put(b"hello world")
fs.get(a).read()
