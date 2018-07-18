from lib.base import BaseRedisAction

__all__ = [
    'DelRedisAction'
]


class DelRedisAction(BaseRedisAction):
    def run(self, key):
        v = self._client.get(key)
        return (True,v)