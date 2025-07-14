
import cv2 


class ResizeImage:

    def __init__(self,src):
        self.src=src
        
    @staticmethod
    def validate_size(new_width,new_height):
        print(new_height,new_width)
        try:
            width=int(new_width)
            height=int(new_height)
            return width,height
        except ValueError:
            print("Error: You can only write numbers like: 200")
            return None, None
        
    def load_and_resize(self, width, height):
        img = cv2.imread(self.src)
        if img is None:
            print("Error: Unable to read the image.")
            return None
        return cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)
        
    def resize_image(self, new_width, new_height):
        width, height = self.validate_size(new_width, new_height)
        if width is not None:
            resized_img = self.load_and_resize(width, height)
            if resized_img is not None:
                cv2.imwrite("resizedImage.jpg", resized_img)
                print("Image saved successfully in the current path")
                cv2.destroyAllWindows()

            
         
    def display_image(self, new_width, new_height):
        width, height = self.validate_size(new_width, new_height)
        if width is not None:
            resized_img = self.load_and_resize(width, height)
            if resized_img is not None:
                title = f"width={width} and height={height}"
                cv2.imshow("Resize Image Tool", resized_img)
                cv2.setWindowTitle("Resize Image Tool", title)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

       
            

       
            
   
    

        




         



