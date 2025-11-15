import cv2
import numpy as np
import AV_image_conversion_RGB_CMY_HSI  as kop
import AV_display_image_with_RGB as dop


img=cv2.imread("picture.jpeg")
rows,cols,_=img.shape
print(f"\nTotal Rows and Total Columns in our image: {rows,cols}")

"""
cv2.namedWindow("AV image", cv2.WINDOW_NORMAL)
cv2.imshow("AV image", img)
cv2.waitKey(0)
"""


print("------------------------------------------------------------------------------------------------------------\n")
yt=["First","Second","Third","Fourth","Fivth","Sixth","Seventh","Eight","Ninth"]
bot=0

def AV_main(yt,b):


   # Cropped image
   grid_height = rows // 9
   for i in range(9):
        r_start = i * grid_height
        r_end = (i + 1) * grid_height if i < 8 else rows
        cut_img = img[r_start:r_end, : ]

    #Display the cropped image
        cv2.namedWindow(f"Cut image ({i+1})", cv2.WINDOW_NORMAL)
        cv2.imshow(f"Cut image ({i+1})", cut_img)

 
    # Convert BGR to RGB
        rgb_cropped = cv2.cvtColor(cut_img, cv2.COLOR_BGR2RGB)

    # Display RGB values of each pixel
        #print("RGB values of cropped image:")
        #print(rgb_cropped)  # This prints the full array
       
        d=[]
        
        for j in range (5):
            
            d.append(rgb_cropped[j,j].tolist())
        
        #print(d)

        q1=sum([p[0] for p in d])//5
        q2=sum([p[1] for p in d])//5
        q3=sum([p[2] for p in d])//5
        
        print(f"Average value of RGB in {yt[b]} Grid: {q1,q2,q3} \n")
        
        R,G,B=kop.RGB_to_normalised_RGB(q1,q2,q3)
        print(f"Normalized RGB value is : ({R:.3f},{G:.3f},{B:.3f})")
        
        C,M,Y=kop.RGB_to_CMY(q1,q2,q3)
        print(f"CMY values of ({R:.3f},{G:.3f},{B:.3f}) is: ({C:.3f},{M:.3f},{Y:.3f}) ")
        
        H,S,I,l =kop.RGB_to_HSI(q1,q2,q3)
       
        print(f"HSI value of ({R:.3f},{G:.3f},{B:.3f}) is: ({H:.3f}{l},{S:.3f},{I:.3f})\n\n")
        print("-----------------------------------------------------------------")
        b+=1
        dop.RGB_img_show(int(q1), int(q2), int(q3))

        print()
        
AV_main(yt,bot)
        
#input("Press Enter to close the code:")

