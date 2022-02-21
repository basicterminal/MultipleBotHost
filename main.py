from multiple.host import *
clients = []

for token in open("tokens.txt", "r").readlines():
    clients.append(token.strip())

for token in clients:
    multiplebothost.AddClient(token = token)

multiplebothost.Start()
