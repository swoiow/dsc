## Ref
[github puppeteer](https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md)

[alekzonder/docker-puppeteer](https://github.com/alekzonder/docker-puppeteer)

## Note
[小改 Chromium](https://paper.seebug.org/537/)

## Usage
```
docker run -it --rm -p 0.0.0.0:9081:9081 -v /usr/src/www/view.js:/app/main.js js:test node /app/main.js
```