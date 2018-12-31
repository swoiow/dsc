# Docker Aria2

[OpenGG/docker-aria2](https://github.com/OpenGG/docker-aria2)

[Aria2 & YAAW 使用说明](https://aria2c.com/usage.html)


### prepare command
```
chown -R 99:99 config
chown -R 99:99 downloads
```


### docker command

> The container is running under uid nobody(99) gid nobody(99). 

```
docker-compose up
```
