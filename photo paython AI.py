import cv2 
img = cv2.imread('img/cat.jpg',100,0)
imge=cv2.resize(img,(900,900))
pixels=imge.size
shap=imge.shape
cv2.rectangle(imge,(200,200),(450,400),(0,255,0),5)
cv2.putText(imge ,'cat face',(220,220),cv2.FONT_HERSHEY_COMPLEX,3/4,(0,0,255),1)
cv2.imshow('sabri',imge)
print('img pixel :',pixels)
print('img shape :',shap)
cv2.waitKey(0)