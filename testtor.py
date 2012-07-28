import socks
s = socks.socksocket()
s.setproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050)

HOST = 'eqt5g4fuenphqinx.onion'

s.connect((HOST, 80))
s.send("GET / HTTP/1.1\r\nHost: %s\r\n\r\n" % (HOST))

data = ''
buf = s.recv(1024)
while len(buf):
    data += buf
    buf = s.recv(1024)
s.close()

print(data)