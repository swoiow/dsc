#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from functools import partial
from http.server import *


def server(HandlerClass=BaseHTTPRequestHandler,
           ServerClass=ThreadingHTTPServer,
           protocol="HTTP/1.0", port=8000, bind="", cert=None):
    """Test the HTTP request handler class.
    This runs an HTTP server on port 8000 (or the port argument).
    """
    server_address = (bind, port)

    HandlerClass.protocol_version = protocol
    with ServerClass(server_address, HandlerClass) as httpd:
        if cert:
            import ssl

            httpd.socket = ssl.wrap_socket(httpd.socket,
                                           server_side=True,
                                           certfile=cert,
                                           ssl_version=ssl.PROTOCOL_TLSv1)
            print("Using ssl mode...")

        sa = httpd.socket.getsockname()
        serve_message = "Serving HTTP on {host} port {port} (http://{host}:{port}/) ..."
        print(serve_message.format(host=sa[0], port=sa[1]))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            sys.exit(0)


if __name__ == '__main__':
    import argparse


    parser = argparse.ArgumentParser()
    parser.add_argument('--cgi', action='store_true',
                        help='Run as CGI Server')
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('--cert', '-c', default=None,
                        help='set cert path and use ssl mode.')
    parser.add_argument('--directory', '-d', default=os.getcwd(),
                        help='Specify alternative directory '
                             '[default:current directory]')
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    args = parser.parse_args()
    if args.cgi:
        handler_class = CGIHTTPRequestHandler
    else:
        handler_class = partial(SimpleHTTPRequestHandler,
                                directory=args.directory)

    server(HandlerClass=handler_class, port=args.port, bind=args.bind, cert=args.cert)
