import asyncio

import aioredis


class CacheEngine:
    def REDIS_DSN(self):
        dsn = f"redis://redis:password@0.0.0.0:63790/20"
        return dsn

    async def create_pool(self):
        pool = await aioredis.create_redis_pool(self.REDIS_DSN)
        return pool

async def main():
    redis = aioredis.from_url('redis://redis:password@127.0.0.1:6379/0')
    await redis.set("my-key", "value")
    value = await redis.get("my-key")
    print(value)


if __name__ == "__main__":
    asyncio.run(main())