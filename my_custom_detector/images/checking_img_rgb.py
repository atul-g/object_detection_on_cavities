train="/home/atulu/Documents/cav_detection_tf_obj_det_api/models/research/object_detection/legacy/imgs/train/"
test="/home/atulu/Documents/cav_detection_tf_obj_det_api/models/research/object_detection/legacy/imgs/test/"

from PIL import Image
import os
path = train #or test
c=0
d=0
for file in os.listdir(path):
    extension = file.split('.')[-1]
    if(extension == 'jpg' or extension == 'jpeg' or extension == 'png'):
        fileLoc = path+file
        img = Image.open(fileLoc)
        if(img.mode != 'RGB'):
    	    print(file+', '+img.mode)
    	    ''''
    elif(extension =='jpeg'):
        c+=1
    else:
        d+=1

print(f"there are {c} jpeg files and {d} png files")
'''

