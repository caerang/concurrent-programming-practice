import socket

s = socket.create_connection(('httpbin.org', 80))
s.setblocking(False)
s.send(b'GET /delay/5 HTTP/1.1\r\nHost: httpbin.org\r\n\r\n')
# 소켓에 읽을 데이터가 없다.
# BlockingIOError 발생
buf = s.recv(1024)
print(buf)
