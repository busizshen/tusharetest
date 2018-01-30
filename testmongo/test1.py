# coding：utf-8
import pymongo
from pymongo import MongoClient

client = MongoClient()

client = MongoClient('10.0.0.9', 27017)
# 连接mongodb数据库
client = MongoClient('mongodb://10.0.0.9:27017/')
# 指定数据库名称
db = client.test_database
# 获取非系统的集合
db.collection_names(include_system_collections=False)
# 获取集合名
posts = db.posts
# 查找单个文档
posts.find_one()
# 给定条件的一个文档
posts.find_one({"author": "Mike"})
# 使用ID查找需要ObjectID
from bson.objectid import ObjectId

post_id = '5728aaa96795e21b91c1aaf0'
document = client.db.collection.find_one({'_id': ObjectId(post_id)})
import datetime

new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]
# 插入多条记录
result = posts.insert_many(new_posts)
# 返回插入的ID
result.inserted_ids
# 递归集合
for post in posts.find():
    post

# 递归条件集合
for post in posts.find({"author": "Mike"}):
    post

# 文档的记录数
posts.count()

# 区间查询
d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    print
    post
# 给集合profiles建立索引 唯一索引
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
# 查看索引信息
list(db.profiles.index_information())
#
user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)

# 聚合查询
from pymongo import MongoClient

db = MongoClient('mongodb://10.0.0.9:27017/').aggregation_example
# 准备数据
result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
                                {"x": 2, "tags": ["cat"]},
                                {"x": 2, "tags": ["mouse", "cat", "dog"]},
                                {"x": 3, "tags": []}])
result.inserted_ids
'''
{ "_id" : ObjectId("576aaa973e5269020848cc7c"), "x" : 1, "tags" : [ "dog", "cat" ] }
{ "_id" : ObjectId("576aaa973e5269020848cc7d"), "x" : 2, "tags" : [ "cat" ] }
{ "_id" : ObjectId("576aaa973e5269020848cc7e"), "x" : 2, "tags" : [ "mouse", "cat", "dog" ] }
{ "_id" : ObjectId("576aaa973e5269020848cc7f"), "x" : 3, "tags" : [ ] }
'''
from bson.son import SON

# $unwind 解开-后面的变量
pipeline = [
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
]
list(db.things.aggregate(pipeline))
# 使用聚合函数with command
db.command('aggregate', 'things', pipeline=pipeline, explain=True)