import cv2
import os


filter = "haarcascade_frontalface_alt.xml"
path = "./uploads/"
dir_list = os.listdir(path)

f = open("./pic-data.txt", "w")
f.write("")
f.close()

print("hello")

pic_data =[]
for i in dir_list:

    img = cv2.imread("./uploads/"+i)
    print(i)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    stop_data = cv2.CascadeClassifier('./data/haarcascades/'+(filter))

    found = stop_data.detectMultiScale(img_gray, minSize =(20, 20))

    amount_found = len(found)

    if amount_found != 0:
        for (x, y, width, height) in found:
            print("Picture: "+(i)+" x: "+str(x)+" y: "+str(y)+" Width: "+str(width)+" Height: "+str(height))
            
            cv2.rectangle(img_rgb, (x, y),(x + height, y + width),(0, 255, 0), 5)
            pic_data.append(str(x)+","+str(y)+","+str(width)+","+str(height))

            f = open("./pic-data.txt", "a")
            f.write((i)+str(pic_data)+"\n")
            f.close()

    else:
        f = open("./pic-data.txt", "a")
        f.write((i)+"\n")
        f.close()