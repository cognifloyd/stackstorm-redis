# Redis Integration Pack

[Redis](https://redis.io) Key-Value Datastore pack

## Configuration

Copy the example configuration in [redis.yaml.example](./redis.yaml.example)
to `/opt/stackstorm/configs/redis.yaml` and edit as required.

It must contain:

* ``host`` - Hostname or IP of Redis server
* ``port`` - Redis Port (Default: 6379)
* ``database`` - Database number to use (Default: 0)


Optionally it may also contain ``password``, if Redis requires authentication.

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Actions

* ``set`` - Set a key
* ``del`` - Delete a key
