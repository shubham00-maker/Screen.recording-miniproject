import pyautogui
import cv2
import numpy as np 

#specify resolution 
resolution = (1920,1080)

#specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")
#specify name of output file 
filename = "Recording.avi"

#specify frames rate. we can choose 
# any value and experiment with it 
fps = 60.0

# creating a video writer object 
out = cv2.VideoWriter(filename,codec,fps,resolution)
# create empty window 
cv2.namedWindow("Live",cv2.WINDOW_NORMAL)
# resize this window 
cv2.resizeWindow("Live",480,270)

while True :
    img = pyautogui.screenshot()
    frame =np.array(img)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow('Live',frame)
    # for stopping recording we press q
    if cv2.waitKey(1) == ord('q'):
        break
#release the video writer 
out.release()
# destroy all windows 
cv2.destroyAllWindows()

