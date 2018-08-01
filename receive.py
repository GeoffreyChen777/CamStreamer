import socket
import cv2
import numpy
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Stream cam')
    parser.add_argument('--ip', dest='ip', help='stream cam to this ip.', default='0.0.0.0', type=str)
    parser.add_argument('--port', dest='port', help='stream port', default=8000, type=int)
    args = parser.parse_args()
    return args

def recvdata(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def receive(conn):
    while 1:
        length = recvdata(conn, 16)
        if length is None:
            break
        stringData = recvdata(conn, int(length))
        data = numpy.fromstring(stringData, dtype='uint8')
        decimg = cv2.imdecode(data, 1)
        cv2.imshow('CAM',decimg)
        if cv2.waitKey(10) == 27:
            s.close()
            cv2.destroyAllWindows()
            break
    cv2.destroyAllWindows()

def ShowCam(ip, port):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(address)
    s.listen(True)
    conn, addr = s.accept()
    while 1:
        receive(conn)
        cv2.destroyAllWindows()
        conn, addr = s.accept()

if __name__ == '__main__':
    args = parse_args()

    print("> Listening on: {}:{}".format(args.ip, args.port))

    ShowCam(args.ip, args.port)


