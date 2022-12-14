# importing the module
import pywhatkit
import random
 
a = "https://www.youtube.com/watch?v=oZQhKgvUyYE"
b = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
c = []
c.append(a)
c.append(b)
try:
   

  pywhatkit.playonyt(c[random.randint(0,1)])
  print("Playing...")
 
except:
   
  # printing the error message
  print("Network Error Occurred")