import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    #print(data.decode())
    received_info = data.decode()
    if len(received_info) > len('ETag'):
        ETag_pos = received_info.find('ETag:')
        #print(ETag_pos)
        if (ETag_pos > 0):
            ETag_pos = ETag_pos + len('ETag:') + 1
            ETag_end = received_info.find('\r', ETag_pos)
            print('ETag:', received_info[ETag_pos:ETag_end])

mysock.close()