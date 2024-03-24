import os
import cv2
 
path = "Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        print(file_name)       
        images.append(file_name)
        
print(len(images))
count = len(images)

frame=cv2.imread(images[0])

height,width,color=frame.shape

newvideo=cv2.VideoWriter("friendship-day.mp4",cv2.VideoWriter_fourcc(*"DIVX"),5,(width,height))
for x in range(0,count,1):
    frame=cv2.imread(images[x])
    newvideo.write(frame)

newvideo.release()