# Stream WebCamera by TCP and Opencv

ZERO latency.

## Requirement

- Unix system
- python opencv
- numpy

## Usage

**NOTES: Run reciever first!**

### Recieve Image
```
python receive.py --ip 0.0.0.0 --port PORT
```

### Stream cam
*Exposure* and *quality* influnce the image transmission efficiency.

camid: /dev/video*

```
python stream.py --ip IP(e.g. 192.168.1.1) --port PORT --camid 0 --exposure 1 --quality 80
```

