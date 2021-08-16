#!/usr/bin/env python3 

from http import server
import os
from socketserver import ForkingMixIn


chemin = os.path.dirname(__file__)+ "/web"

os.chdir(chemin)




class ForkingHTTPServer(ForkingMixIn,server.HTTPServer):
    pass


serv = ForkingHTTPServer(("",8080),server.CGIHTTPRequestHandler)
serv.serve_forever()
#serv = server.HTTPServer(("",8080),server.CGIHTTPRequestHandler)
#serv.serve_forever()


