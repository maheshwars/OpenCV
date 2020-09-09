import cv2
import datetime as dt

cap = cv2.VideoCapture(0)  #"Megamind.avi"(720,528) or 0 for videocam(640,480)
"""fourcc = cv2.VideoWriter_fourcc(*'XVID')                       #format of video to be saved
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (720,528))     # params-(1. filename,2. 4cc code,3. no. of frames, 
                                                                    #4. (width of original vid,height of orignal vid))"""
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))               #to get widhth of each frame
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))              #to get height of each frame                                    
#cap.set(3,3000)                                         # 3 for cv2.CAP_PROP_FRAME_WIDTH
#cap.set(4,3000)                                          # 4 for cv2.CAP_PROP_FRAME_HEIGHT
#print(cap.get(3))
#print(cap.get(4))

while(cap.isOpened()):                                          #inplace of True you can also write cap.isOpened()
    ret, frame = cap.read()
    if ret == True:

        
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + '  Height: ' + str(cap.get(4))
        datet =  str(dt.datetime.now())
        frame = cv2.putText(frame , datet, (10,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
        frame = cv2.rectangle(frame, (9,20), (520,55), (255,0,0), 2)
        cv2.imshow('frame', frame)
        
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
#out.release()
cv2.destroyAllWindows()