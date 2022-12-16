# Disparity Calculator for SoftWare(SW)

# Abstract

calcurate distance through disparity and object-detection bbox (yolov7).

Its systems has left and light camera on Jetson, and calcurate video frame with realtime.


# Inference

## video on PyQt
```sh
python3 main.py --qt
```

## image
```sh
python3 main.py --image
```
## video
```sh
python3 main.py --vid
```


# Formula

・<b>Disparity formula</b> and <b>camera size</b>：


<b>Disparity formula by python</b>
```python
def disranse_formula(disparity):
    T=2.6
    f = 0.315
    img_element = 0.0001*2.8
    K = int(T*f/img_element)
    return K/disparity
```

## Relation of Disparity and Distance(Z axis)


# References
- [ONNX-YOLOv7-Object-Detection](https://github.com/ibaiGorordo/ONNX-YOLOv7-Object-Detection)




