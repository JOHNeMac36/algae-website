#!/usr/bin/python3

import http.server
import socketserver
import os

PORT = 3000

web_dir = os.path.join(os.path.dirname(__file__), 'public_html')
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("0.0.0.0", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
