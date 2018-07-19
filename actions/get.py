from lib.base import BaseRedisAction

__all__ = [
    'GetRedisAction'
]


class GetRedisAction(BaseRedisAction):
    def run(self, key):
        v = self._client.get(key)
        return (True,v)
