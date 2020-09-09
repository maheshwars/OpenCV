import cv2

cap = cv2.VideoCapture("Megamind.avi")  #"Megamind.avi"(720,528) or 0 for videocam(640,480)
fourcc = cv2.VideoWriter_fourcc(*'XVID')                       #4cc of video to be saved
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (720,528))     # params-(1. filename,2. 4cc code,3. no. of frames, 
                                                                    #4. (width of original vid,height of orignal vid))
while(cap.isOpened()):                                          #inplace of True you can also write cap.isOpened()
    ret, frame = cap.read()
    if ret == True:

        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))              // to get widhth of each frame
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))              //to get height of each frame

        out.write(frame)                                    #to write a video file per frame
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        #out.write(gray)                                        //not working
        #cv2.imshow('frame',frame)                              //for normal
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()