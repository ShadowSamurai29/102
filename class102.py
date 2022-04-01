import cv2 
import dropbox
import time
import random
start_time = time.time()
def take_snap() : 
    number = random.randint(0,100)
    camera = cv2.VideoCapture(0)
    result = True 
    while(result) : 
        ret,frame = camera.read()
        image_itachi = "img" + str(number) + '.png' 
        cv2.imwrite (image_itachi, frame)
        result =  False
    return image_itachi 
    print("snapshot taken boy/girl")
    camera.release()
    cv2.destroyAllWindows()

def uploadfile (image_itachi) :
    access_token = ""
    file = image_itachi
    file_from = file
    file_2 = "/testfolder/" + (image_itachi)
    dbx = dropbox.Dropbox(access_token)
    with open (file_from, "rb") as f :
        dbx.files_upload (f.read(), file_2, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main () :
    while(True) : 
        if((time.time()-start_time)>=5) :
            name = take_snap()
            uploadfile(name)

main()

