import cv2
import numpy as np
cap=cv2.VideoCapture(0)
whT=320
confThreshold=0.5
nmsThreshold=0.3


classesfile='C:\machine learning projects\computer vision\yolo projects\important yolo files\coco.names'
classnames=[]
with open(classesfile,'rt') as f:
    classnames=f.read().rstrip('\n').split('\n')


modelconfigurtion='C:\machine learning projects\computer vision\yolo projects\important yolo files\yolov3-320.cfg'
modelweights='C:\machine learning projects\computer vision\yolo projects\important yolo files\yolov3.weights'

net=cv2.dnn.readNetFromDarknet(modelconfigurtion,modelweights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

def findobjects(outputs,img):
    hT,wT,cT=img.shape
    bbox=[]
    classIds=[]
    confs=[]
    for output in outputs:
        for det in output:
            scores=det[5:]
            classId=np.argmax(scores)
            confidence=scores[classId]
            if confidence>confThreshold:
                w,h=int(det[2]*wT),int(det[3]*hT)
                x,y=int(det[0]*wT-w/2),int(det[1]*hT-h/2)
                bbox.append([x,y,w,h])
                classIds.append(classId)
                confs.append(float(confidence))


    indices=cv2.dnn.NMSBoxes(bbox,confs,confThreshold,nmsThreshold)
    for i in indices:

        box=bbox[i]
        x,y,w,h=box[0],box[1],box[2],box[3]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img,f'{classnames[classIds[i]].upper()} {int(confs[i]*100)}%',
                    (x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)



while True:
    success,img=cap.read()
    blob=cv2.dnn.blobFromImage(img,1/255,(whT,whT),[0,0,0],1,crop=False)
    net.setInput(blob)
    layerNames=net.getLayerNames()
    outputnames=[layerNames[i-1] for i in net.getUnconnectedOutLayers()]
    outputs=net.forward(outputnames)
    findobjects(outputs,img)
    cv2.imshow('image',img)
    cv2.waitKey(1)
