import math



print("\n\n!!! This Project tells us the RGB,CMY,HSI values from the given image which is divided into 9 parts. !!!")

def RGB_to_normalised_RGB(a,b,c):
     
     s1=a/255
     s2=b/255
     s3=c/255
     return s1,s2,s3
     #print(f"The normalised RGB color values are:({s1:.2f},{s2:.2f},{s3:.2f})")
def RGB_to_CMY(a,b,c):
    
    c1=1-a/255
    c2=1-b/255
    c3=1-c/255
    return c1,c2,c3
    #print(f"The CMY values are: ({c1:.2f},{c2:.2f},{c3:.2f})")

def RGB_to_HSI(a,b,c):
    
    I=round((a+b+c)/3,3)
    S=1-3*min(a,b,c)/(a+b+c)
    
    #For caculation of H value

    #For numerator calculation  
    n=((a-b) + (a-c))/2

    #For denominator calculation
    d=math.sqrt((a-b)**2 + (a-c)*(b-c))

    #Actual value calculation
    if d!=0:
        o=math.degrees(math.acos(n/d))
    else:
        o=0

    #now check value on the condition
    if c<=b:
        H=o
    else:
        H=360-o
    l=chr(176)
    #print(f"{H:.3f}{l},{S:.3f},{I:.3f}")
    return H,S,I,l



"""
    
# ------ main ------

print("Welcome to color conversion with RGB to CMY and HSI ")
print("Must Remember!")
print("Each component (R, G, B) typically ranges from 0 to 255 (in 8-bit representation).")

print("Please provide us the RGB values")
v1=int(input("Enter RED(R) value: "))
v2=int(input("Enter Green(G) value: "))
v3=int(input("Enter Blue(B) value: "))

R,G,B=RGB_to_normalisedRGB(v1,v2,v3)
RGB_to_CMY(v1,v2,v3)
H,S,I=RGB_to_HSI(R,G,B)
"""
