import eel
import sys

sys.path.append("..")
eel.init("front")

@eel.expose
def Saludar(numero):
    print("Hola mundo desde python")  
    print(f"El número es: {numero}")              
           # Expose this function to Javascript


eel.start("index.html",size=(800,800))


