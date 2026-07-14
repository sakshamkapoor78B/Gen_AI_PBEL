import cv2
import os

detector=cv2.CascadeClassfier(cv2.data.haarcadcades+"haarcascade_frontalface_alt.xml")
cv2.namedWindow("Face Detection System",cv2.WINDOW_NORMAL)
cam = cv2.VideoCapture(0)
while True:
    rect,frame = cam.read()
    face = detector.detectMultiScale(frame,1.2)
    print (len(face))
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,100),3)
    cv2.imshow("Face Detection System",frame)
    if cv2.waitKey(5)==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()



# Detect Face
def face_detect(frame):
    detector = cv2.CascadeClassifier(cv2.data.haarcadcades+"haarcascade_frontalface_alt.xml")
    face = detector.detectMultiScale(frame,1.2)
    return face

# Gray Scale
def gray_scale(image):
    cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Cut face
def cut_face(image,face_coord):
    cut_faces = []
    for(x,y,w,h) in face_coord:
        face = image[y:y+h ,x:x+w]
        cut_faces.append(face)
    return cut_faces


# Resize
def resize(images,size=(80,100)):
    resized_images =[]
    for image in images:
        img = cv2.resize(image,size)
        resized_images.append(img)
    return resized_images

# Normalize intensity
def normalize_intensity(images):
    normalized_faces=[]
    for img in images:
        normalized_faces.append(cv2.equalizeHist(img))
    return normalized_faces

# Image Plot
import matplotlib.pyplot as plt
def plot(image,title= " "):
    plt.figure(figsize=(12,12))
    if image.shape == 3:
        cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    plt.imshow(image, c= 'gray')
    plt.title()
    plt.axes("off")
    plt.show()



# Pipeline
def pipeline(image,face_coord):
    faces = cut_face(image,face_coord)
    faces = resize(faces)
    faces = normalize_intensity(faces)
    return faces

# Draw Rectangle
def draw_rectangle(frame,coords):
    for (x,y,w,h) in coords:
        cv2.rectangle(frame,(x,y),(x+w,y+h)(0,0,200),2)


# Let's Create our own images dataset
name = input ("Enter your name: ")
no_Samples = int(input("Enter value for sample: "))
folder = "Dataset/"+name.lower()
if os.path.exists(folder):
    print("Folder with this name is already existed")
else:
    os.mkdir(folder)
    start_cap = False
    sample=1

    cam = cv2.VideoCapture(0)

    while True:
        rect,frame = cam.read()
        gray =gray_scale(frame)
        coords = face_detect(gray)
        if len(coords)>0:
            faces = pipeline(gray,coords)
            image_name = folder +"/"+str(sample)+".jpg"
            cv2.imwrite(image_name,0)
        else:
            print("No Face Found")
