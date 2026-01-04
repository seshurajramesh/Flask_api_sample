import os
import redis
import dotenv

dotenv.load_dotenv()


redis_client = redis.StrictRedis(host=os.getenv("REDIS_HOST", "localhost"),port=os.getenv("REDIS_PORT", 6379),db=0,decode_responses=True)