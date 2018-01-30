import redis
import configparser



r = redis.Redis(host='192.168.50.8',port=7000,db=0,password='W3qIOFe6DFqowwXaOgnh8nlR9QTc6DXR4P6pi1dHthVLbhnvDiVe5PCMak74j0Yt')

CONFIG = configparser.ConfigParser()
CONFIG.read("system.ini")
redis_host = CONFIG.get("redis", "REDIS_HOST")
redis_port = CONFIG.get("redis", "REDIS_PORT")
redis_db = CONFIG.get("redis", "REDIS_DB")
redis_pwd = CONFIG.get("redis", "REDIS_PASSWORD")
redisConnect = redis.Redis(redis_host, redis_port, redis_db, redis_pwd)

keys= redisConnect.keys()

class RedisTool:
    @staticmethod
    def hexists(name, key):
        return redisConnect.hexists(name, key)

    @staticmethod
    def hget(name, key):
        return redisConnect.hget(name, key)

    @staticmethod
    def getset(name, value):
        return redisConnect.getset(name, value)

    @staticmethod
    def hdel(name, *keys):
        return redisConnect.hdel(name, *keys)

    @staticmethod
    def hgetall(name):
        return redisConnect.hgetall(name)

    @staticmethod
    def hkeys(name):
        return redisConnect.hkeys(name)

    @staticmethod
    def hlen(name):
        return redisConnect.hlen(name)

        # Set key to value within hash name Returns 1 if HSET created a new field, otherwise 0

    @staticmethod
    def hset(name, key, value):
        return redisConnect.hset(name, key, value)

    @staticmethod
    def setex(name, time, value):
        return redisConnect.setex(name, time, value)

    @staticmethod
    def get(name):
        return redisConnect.get(name)

    @staticmethod
    def exists(name):
        return redisConnect.exists(name)

    @staticmethod
    def set(name, value):
        return redisConnect.set(name, value)