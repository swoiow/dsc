# Docker Aria2

[OpenGG/docker-aria2](https://github.com/OpenGG/docker-aria2)
[Aria2 & YAAW 使用说明](https://aria2c.com/usage.html)

> prepare.sh
```
useradd dockeruser

mkdir config

# Set proper permissions. Change 1001:1002 to your own uid:gid .
chown -R dockeruser:dockeruser config

find config -type d -exec chmod 755 {} +
find config -type f -exec chmod 644 {} +

# Create download dir
mkdir downloads

# Set proper permissions. Change 1001:1002 to your own uid:gid .
chown -R dockeruser:dockeruser downloads
find downloads -type d -exec chmod 755 {} +
find downloads -type f -exec chmod 644 {} +
```


> docker command
```
docker run \
  -itd --rm\
  --name aria2 \
  -u=dockeruser:dockeruser \
  -v config:/config \
  -v downloads:/downloads \
  -p 6800:6800 \
  opengg/aria2
```
