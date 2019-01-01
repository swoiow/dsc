# Docker Aria2

[OpenGG/docker-aria2](https://github.com/OpenGG/docker-aria2)

[Aria2 & YAAW 使用说明](https://aria2c.com/usage.html)


### HOW
1. ` git clone `

1.1. (option) change user in ` docker-compose.yml `, as the same time change it below(91192). 

2. ```
    chown -R 91192:91192 config
    chown -R 91192:91192 downloads
   ```

3. change username/password in ` docker-compose.yml `

4. ` docker-compose up `
