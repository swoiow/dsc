FROM node:10-alpine

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true
ENV NODE_PATH="/usr/local/share/.config/yarn/global/node_modules:${NODE_PATH}"
ENV CHROMIUM_BIN="/usr/bin/chromium-browser"

WORKDIR /app

RUN set -ex && apk update && apk upgrade && \
    echo @edge http://nl.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories && \
    echo @edge http://nl.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories && \
    apk add --no-cache harfbuzz@edge chromium@edge nss@edge dumb-init

RUN yarn global add puppeteer express && yarn cache clean

# Add user so we don't need --no-sandbox.
RUN addgroup -S sandbox && adduser -S -g sandbox sandbox \
    && mkdir -p /home/sandbox/Downloads \
    && mkdir -p /app \
    && chown -R sandbox:sandbox /home/sandbox \
    && chown -R sandbox:sandbox /app

# Run everything after as non-privileged user.
USER sandbox

ENTRYPOINT ["dumb-init", "--"]

# Run command example: docker run --cap-add=SYS_ADMIN imagine_name
