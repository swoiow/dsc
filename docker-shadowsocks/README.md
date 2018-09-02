# shadowsocks docker
*default use debian & shadowsocks lib*

## Usage
*build dockerfile both local and server*

## local side:

  0. `docker run -itd -p 1081:1080 --rm --name ss_client docker-images ss-local -s server_ip -p server_port -b 0.0.0.0 -l 1080 -k password -m encryption`

## server side:

  0. install haproxy
  0. config haproxy [Setup a Shadowsocks Relay](https://github.com/shadowsocks/shadowsocks/wiki/Setup-a-Shadowsocks-relay)
  0. `docker run -itd --rm --user ss --name ss_server docker-images ss-server -s docker-container-ip -p server_port -k password -m encryption`

### easy
use the repository version

### clowwindy
see this [git](https://github.com/clowwindy/shadowsocks-libev)

### python
see this [git](https://github.com/shadowsocks/shadowsocks)