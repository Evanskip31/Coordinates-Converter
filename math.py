import math

for k in range(0, 180, 9):
    #A = math.radians(k)
    B = math.tan(k)
    print("Tan of (",k,") is: ", B)
    
    
pi = math.pi
print(round(pi, 4))
print(180/pi)

print(math.degrees(math.atan(0.41667)))
print(math.atan(0.41667))

def return_24():
   
    return  8 + 6

print(return_24())

tanΘ = 17.5
tanΘ = str(tanΘ) + '°'
print(tanΘ)

x = math.radians(22.62)

print(13*math.cos(x))
