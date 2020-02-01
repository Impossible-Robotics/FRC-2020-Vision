import cv2
import grip

cam = cv2.VideoCapture(0)
pipeline = grip.GripPipeline()

while (True):
    ret, frame = cam.read()


    pipeline.process(frame)
   
    mod_img = None
    if (len(pipeline.filter_contours_output) > 0):
        x, y, w, h = cv2.boundingRect(pipeline.filter_contours_output[0])
        mod_img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4) 
    
    if (mod_img is not None):
        cv2.imshow("Frame", mod_img)
   
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
