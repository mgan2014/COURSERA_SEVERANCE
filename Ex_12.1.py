import socket
def find_value(str_all, str_key):
    if len(str_all) > len(str_key):
            key_pos = str_all.find(str_key)
            #print(key_pos)
            if (key_pos > 0):
                key_pos = key_pos + len(str_key) + 1
                key_end = str_all.find('\r', key_pos)
                print(str_key, str_all[key_pos:key_end])

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
    find_value(received_info,'Last-Modified:')
    find_value(received_info,'ETag:')
    find_value(received_info,'Content-Length:')
    find_value(received_info,'Cache-Control:')
    find_value(received_info,'Content-Type:')
    

mysock.close()