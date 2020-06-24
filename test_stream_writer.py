import socket
import time

host = 'localhost'
port = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
while True:
    print('\nListening for a client at',host , port)
    conn, addr = s.accept()
    print('\nConnected by', addr)
    try:
        print('\nReading file...\n')
        while 1:
            out = "test01"
            print('Sending line', out)
            conn.send(out.encode())
            time.sleep(0.5)
    except socket.error:
        print ('Error Occured.\n\nClient disconnected.\n')
conn.close()
