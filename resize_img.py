
import cv2 


class ResizeImage:
    def __init__(self,src):
        self.src=src
    def resize_image(self,new_width,new_height):
        try:
            width=int(new_width)
            height=int(new_height)
        except ValueError:
            print("Error: You can only write numbers like: 200")
        else:
            img=cv2.imread(self.src)
            resizedImg=cv2.resize(img,(width,height), interpolation= cv2.INTER_LINEAR)
            # cv2.imshow("resized img win", resizedImg)
            # title=f"width={width} and height={height}"
            # cv2.setWindowTitle("resized img win", title)
            cv2.imwrite("resizedImage.jpg",resizedImg)
            print("image saved successfully in the current path")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
         
            
   
    

        




         



