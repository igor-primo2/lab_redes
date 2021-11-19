import socket

HOST = '127.0.0.1'
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print 'iniciando'
print 'gimme name of file'

file_name = raw_input()
while file_name <> '\x18':
    request = 'GET /{} HTTP/1.1\r\n'.format(file_name)
    request += 'Host: depressed.boy.depr\r\n'
    request += 'Accept-Language: la\r\n'
    tcp.send(request);
    msg = raw_input()

tcp.close()
