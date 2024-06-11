import threading
import time
from controladores.comunicacion import Comunicacion

class Hilo(threading.Thread):
    def __init__(self, ventanaPrincipal):
        threading.Thread.__init__(self)
        self.ventanaPrincipal = ventanaPrincipal
        self.comunicacion = Comunicacion(ventanaPrincipal)

    def run(self):
        while True:
            clientes = self.comunicacion.consultar_cliente("", "", "", "", "")
            servicios = self.comunicacion.consultar_todo("", "", "", "")
            
            with open('datos_clientes_servicios.txt', 'w') as archivo:
                archivo.write("Clientes:\n")
                for cliente in clientes:
                    archivo.write(f"{cliente}\n")
                archivo.write("Servicios:\n")
                for servicio in servicios:
                    archivo.write(f"{servicio}\n")
                    
            time.sleep(60)
    
    

