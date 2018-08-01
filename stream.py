import socket
import cv2
import numpy
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Stream cam')
    parser.add_argument('--ip', dest='ip', help='stream cam to this ip.', default='0.0.0.0', type=str)
    parser.add_argument('--port', dest='port', help='stream port', default=8000, type=int)
    parser.add_argument('--camid', dest='camid', help='Camera ID', default=0, type=int)
    parser.add_argument('--exposure', dest='exposure', help='Camera exposure', default=1, type=int)
    parser.add_argument('--quality', dest='quality', help='Encode quality', default=80, type=int)
    args = parser.parse_args()
    return args

def stream(ip, port, camid=0, exposure=1, quality=80):
    address = (ip, port)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(address)

    capture = cv2.VideoCapture(camid)
    capture.set(15, exposure)
    ret, frame = capture.read()
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY), quality]

    while ret:
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = numpy.array(imgencode)
        stringData = data.tostring()
        sock.send(str(len(stringData)).ljust(16))
        sock.send(stringData)
        ret, frame = capture.read()
        if cv2.waitKey(10) == 27:
            break
    sock.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    args = parse_args()
    print("> Cam ID {}".format(args.camid))
    stream(args.ip, args.port, args.camid, args.exposure, args.quality)