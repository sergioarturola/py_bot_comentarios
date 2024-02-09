
 
import keyboard
import time
import random
print("esperando 6 segundos")
lista = ["practicando con py", "keyboard", "vamos por los 700"]
time.sleep(6)
for i in range(55):
    palabra = random.choice(lista)
    keyboard.write(palabra) 
    keyboard.press_and_release('enter')
    time.sleep(6)

print("Fin")
  

