import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.usuario import Usuario
from controladores.validaciones import Validaciones
from tkinter import messagebox
from vistas.tabla import Tabla
from vistas.tabla2 import Tabla2

class Interfaz:

    def __init__(self):
        titulos = ['identificador','Nombre Servicio','Cedula','Descripcion','Valor']
        columnas = ['id','nombre','cedula','descripcion','valor']
        data = []

        titulos2 = ['identificador','Nombre','Apellido','Cedula','Telefono','Correo']
        columnas2 = ['id','nombre','apellido','cedula','telefono','correo']
        data2 = []

        self.ventanaPrincipal = tk.Tk()
        #self.ventanaPrincipal.resizable(0, 0)
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.tabla = Tabla(self.ventanaPrincipal,titulos, columnas, data)
        self.tabla2 = Tabla2(self.ventanaPrincipal,titulos2,columnas2,data2)

    def validar_entrada(self, valor, etiqueta_error):
        mensaje_error = Validaciones.validarLetrasNumeros(valor)
        if mensaje_error:
            etiqueta_error.config(text=mensaje_error)
        else:
            etiqueta_error.config(text="")

    def accion_guardar_boton(self, nombre, apellido, cedula, telefono, correo,  nombre_error, apellido_error, cedula_error, telefono_error, correo_error):
        # Validaciones
        nombre_msg = Validaciones.validarLetrasNumeros(nombre)
        apellido_msg = Validaciones.validarLetrasNumeros(apellido)
        cedula_msg = Validaciones.validarLetrasNumeros(cedula)
        telefono_msg = Validaciones.validarLetrasNumeros(telefono)
        correo_msg =Validaciones.validarLetrasNumeros(correo)
        
        if nombre_msg or apellido_msg or cedula_msg or telefono_msg or correo_msg:
            nombre_error.config(text=nombre_msg or "")
            apellido_error.config(text=apellido_msg or "")
            cedula_error.config(text=cedula_msg or "")
            telefono_error.config(text=telefono_msg or "")
            correo_error.config(text=correo_msg or "")
            # Mostrar un mensaje de error general si algún campo no es válido
            messagebox.showwarning("Error", "Por favor, complete todos los campos correctamente.")
        else:
            self.comunicacion.guardar(nombre , apellido, cedula, telefono, correo)
            nombre_error.config(text="")
            apellido_error.config(text="")
            cedula_error.config(text="")
            telefono_error.config(text="")
            correo_error.config(text ="")
            # Mostrar un mensaje de éxito
            messagebox.showwarning("Éxito", "Los datos han sido guardados correctamente.")
            self.limpiar_cajas()
            self.accion_consultar_todo_clientes(self.entryNombre.get(),self.entryApellido.get(),self.entryCedula.get(), self.entryTelefono.get(), self.entryCorreo.get())
            
    
    def accion_guardar_servicio(self, nombre_servicio, cedula_servicio, descripcion_servicio, valor_servicio, nombre_servicio_error, cedula_servicio_error, descripcion_servicio_error, valor_servicio_error):
        # Validaciones
        nombre_servicio_msg = Validaciones.validarLetrasNumeros(nombre_servicio)
        cedula_servicio_msg = Validaciones.validarLetrasNumeros(cedula_servicio)
        descripcion_servicio_msg = Validaciones.validarLetrasNumeros(descripcion_servicio)
        valor_servicio_msg = Validaciones.validarLetrasNumeros(valor_servicio)
        
        
        if nombre_servicio_msg or cedula_servicio_msg or descripcion_servicio_msg or valor_servicio_msg:
            nombre_servicio_error.config(text=nombre_servicio_msg or "")
            cedula_servicio_error.config(text=cedula_servicio_msg or "")
            descripcion_servicio_error.config(text=descripcion_servicio_msg or "")
            valor_servicio_error.config(text=valor_servicio_msg or "")
            
            # Mostrar un mensaje de error general si algún campo no es válido
            messagebox.showwarning("Error", "Por favor, complete todos los campos correctamente.")
        else:
            self.comunicacion.guardar_servicio(nombre_servicio , cedula_servicio, descripcion_servicio, valor_servicio)
            nombre_servicio_error.config(text="")
            cedula_servicio_error.config(text="")
            descripcion_servicio_error.config(text="")
            valor_servicio_error.config(text="")
        
            # Mostrar un mensaje de éxito
            messagebox.showwarning("Éxito", "Los datos han sido guardados correctamente.")
            self.limpiar_cajas_servicio()
            self.accion_consultar_todo(self.entryNombre_servicio.get(), self.entryCedula_servicio.get(), self.entryDescripcion_servicio.get(), self.entryValor_servicio.get())
            



    def accion_actualizar_cliente(self, id ,nombre, apellido, cedula, telefono, correo):

        if id =='':
            self.comunicacion.guardar(id, nombre, apellido, cedula, telefono, correo)
        
        else:
            self.comunicacion.actualizar_cliente(id, nombre, apellido, cedula, telefono, correo)
            self.limpiar_cajas()
            self.accion_consultar_todo_clientes(self.entryNombre.get(), self.entryApellido.get(), self.entryCedula.get(), self.entryTelefono.get(), self.entryCorreo.get())





    def accion_actualizar(self, id ,nombre_servicio, cedula_servicio, descripcion_servicio, valor_servicio):

        if id =='':
            self.comunicacion.guardar_servicio(id, nombre_servicio, cedula_servicio, descripcion_servicio, valor_servicio)
        
        else:
            self.comunicacion.actualizar(id, nombre_servicio, cedula_servicio, descripcion_servicio, valor_servicio)
            self.limpiar_cajas_servicio()
            self.accion_consultar_todo(self.entryNombre_servicio.get(), self.entryCedula_servicio.get(), self.entryDescripcion_servicio.get(), self.entryValor_servicio.get())

        

    def accion_consultar_boton(self, labelConsultaMarca, labelConsultaVelocidad, labelConsultacedula_msg, labelConsultatelefono_msg, id):
        resultado = self.comunicacion.consultar(id)
        labelConsultaMarca.config(text=resultado.get('marca'))
        labelConsultaVelocidad.config(text=resultado.get('velocidad'))
        labelConsultacedula_msg.config(text=resultado.get('cedula_msg'))
        labelConsultatelefono_msg.config(text=resultado.get('telefono_msg'))
    
    def accion_consultar_todo(self, nombre_servicio, cedula_servicio, descripcion_servicio, valor_servicio):
        resultado = self.comunicacion.consultar_todo(nombre_servicio, cedula_servicio, descripcion_servicio, valor_servicio)
        data= []
        for elemento in resultado:
            data.append((elemento.get('id'),elemento.get('nombre'), elemento.get('cedula'),elemento.get('descripcion'),elemento.get('valor')))
        self.tabla.refrescar(data)
        self.limpiar_cajas_servicio()

        print(resultado)
        print(type(resultado))

    def accion_consultar_todo_clientes(self, nombre, apellido, cedula, telefono, correo):
        resultado = self.comunicacion.consultar_cliente(nombre, apellido, cedula, telefono, correo)
        data= []
        for elemento in resultado:
            data.append((elemento.get('id'),elemento.get('nombre'), elemento.get('apellido'),elemento.get('cedula'),elemento.get('telefono'),elemento.get('correo')))
        self.tabla2.refrescar(data)
        self.limpiar_cajas()


    def limpiar_cajas(self):
        self.entryNombre.delete(0,tk.END)
        self.entryApellido.delete(0,tk.END)
        self.entryCedula.delete(0,tk.END)
        self.entryTelefono.delete(0,tk.END)
        self.entryCorreo.delete(0,tk.END)

    def limpiar_cajas_servicio(self):
        self.entryNombre_servicio.delete(0,tk.END)
        self.entryCedula_servicio.delete(0,tk.END)
        self.entryDescripcion_servicio.delete(0,tk.END)
        self.entryValor_servicio.delete(0,tk.END)
        self.entryidconsulta.delete(0,tk.END)


    def mostrar_interfaz(self):
        usuario = Usuario(self.ventanaPrincipal)

#Espacios de texto y entardas de texto crear usuario
        labelNombre = tk.Label(self.ventanaPrincipal, text="Nombre")
        self.entryNombre = tk.Entry(self.ventanaPrincipal, textvariable=usuario.nombre)
        labelApellido = tk.Label(self.ventanaPrincipal, text="Apellido")
        self.entryApellido = tk.Entry(self.ventanaPrincipal, textvariable=usuario.apellido)
        labelCedula = tk.Label(self.ventanaPrincipal, text="Cedula")
        self.entryCedula = tk.Entry(self.ventanaPrincipal, textvariable=usuario.cedula)
        labelTelefono = tk.Label(self.ventanaPrincipal, text="Telefono")
        self.entryTelefono = tk.Entry(self.ventanaPrincipal, textvariable=usuario.telefono)
        labelCorreo = tk.Label(self.ventanaPrincipal, text="Correo")
        self.entryCorreo = tk.Entry(self.ventanaPrincipal,textvariable=usuario.correo)


#Espacios de texto y entradas de texto crear servicio
        labelNombre_servicio = tk.Label(self.ventanaPrincipal, text="Nombre Servicio")
        self.entryNombre_servicio = tk.Entry(self.ventanaPrincipal, textvariable=usuario.nombre_servicio)
        labelCedula_servicio = tk.Label(self.ventanaPrincipal, text="Cedula Cliente")
        self.entryCedula_servicio = tk.Entry(self.ventanaPrincipal, textvariable=usuario.cedula_servicio)
        labelDescripcion_servicio = tk.Label(self.ventanaPrincipal, text="Descripcion")
        self.entryDescripcion_servicio = tk.Entry(self.ventanaPrincipal, textvariable=usuario.descripcion_servicio)
        labelValor_servicio = tk.Label(self.ventanaPrincipal, text="Valor")
        self.entryValor_servicio = tk.Entry(self.ventanaPrincipal, textvariable=usuario.valor_servicio)


        label_idconsulta = tk.Label(self.ventanaPrincipal,text="ID")
        self.entryidconsulta = tk.Entry(self.ventanaPrincipal, fg ="red")

        label_idconsulta2 = tk.Label(self.ventanaPrincipal,text="ID")
        self.entryidconsulta2 = tk.Entry(self.ventanaPrincipal, fg ="red")



        label_info1 =tk.Label(self.ventanaPrincipal,text= "Crear Usuario", fg ="red", font= ("arial",15))
        label_info2 =tk.Label(self.ventanaPrincipal,text= "Crear Servicio", fg ="red", font= ("arial",15))
        label_info3 =tk.Label(self.ventanaPrincipal,text= "Tabla Servicios", fg ="red", font= ("arial",15))
        label_info4 =tk.Label(self.ventanaPrincipal,text= "Tabla Clientes", fg ="red", font= ("arial",15))

        

        #Etiquetas de error
        nombre_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        nombre_error.place(x=260, y=40)
        apellido_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        apellido_error.place(x=260, y=80)
        cedula_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        cedula_error.place(x=260, y=120)
        telefono_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        telefono_error.place(x=260, y=160)
        correo_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        correo_error.place(x=260, y=200)

        nombre_servicio_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        nombre_servicio_error.place(x=980, y=40)
        cedula_servicio_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        cedula_servicio_error.place(x=980, y=80)
        descripcion_servicio_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        descripcion_servicio_error.place(x=980, y=120)
        valor_servicio_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        valor_servicio_error.place(x=980, y=160)

        #Comandos con el teclado
        self.entryNombre.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryNombre.get(), nombre_error))
        self.entryApellido.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryApellido.get(), apellido_error))
        self.entryCedula.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryCedula.get(), cedula_error))
        self.entryTelefono.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryTelefono.get(), telefono_error))
        self.entryCorreo.bind("<KeyRelease>",lambda event: self.validar_entrada(self.entryCorreo.get(),correo_error))

        self.entryNombre_servicio.bind("<KeyRelease>",lambda event: self.validar_entrada(self.entryNombre_servicio.get(),nombre_servicio_error))
        self.entryCedula_servicio.bind("<KeyRelease>",lambda event: self.validar_entrada(self.entryCedula_servicio.get(),cedula_servicio_error))
        self.entryDescripcion_servicio.bind("<KeyRelease>",lambda event: self.validar_entrada(self.entryDescripcion_servicio.get(),descripcion_servicio_error))
        self.entryValor_servicio.bind("<KeyRelease>",lambda event: self.validar_entrada(self.entryValor_servicio.get(),valor_servicio_error))

        boton_guardar = tk.Button(self.ventanaPrincipal, text="Guardar Cliente", command=lambda: 
        self.accion_guardar_boton(self.entryNombre.get(), self.entryApellido.get(), self.entryCedula.get(), self.entryTelefono.get(),self.entryCorreo.get(), nombre_error, apellido_error, cedula_error, telefono_error, correo_error))
        
        boton_guardar_servicio = tk.Button(self.ventanaPrincipal,text = "Guardar Servicio", command=lambda:
        self.accion_guardar_servicio(self.entryNombre_servicio.get(), self.entryCedula_servicio.get(), self.entryDescripcion_servicio.get(),self.entryValor_servicio.get(), nombre_servicio_error, cedula_servicio_error, descripcion_servicio_error,valor_servicio_error))
        
        boton_consultar = tk.Button(self.ventanaPrincipal, text="Consultar", command=lambda:
        self.accion_consultar_todo(self.entryNombre_servicio.get(), self.entryCedula_servicio.get(), self.entryDescripcion_servicio.get(), self.entryValor_servicio.get()))

        boton_consultar_cliente = tk.Button(self.ventanaPrincipal, text="Consultar", command=lambda:
        self.accion_consultar_todo_clientes(self.entryNombre.get(),self.entryApellido.get(),self.entryCedula.get(), self.entryTelefono.get(), self.entryCorreo.get()))

        boton_actualizar = tk.Button(self.ventanaPrincipal, text="Actualizar", command=lambda: 
        self.accion_actualizar(self.entryidconsulta.get(),self.entryNombre_servicio.get(), self.entryCedula_servicio.get(), self.entryDescripcion_servicio.get(), self.entryValor_servicio.get()))

        boton_actualizar_cliente = tk.Button(self.ventanaPrincipal, text="Actualizar", command=lambda: 
        self.accion_actualizar_cliente(self.entryidconsulta2.get(),self.entryNombre.get(), self.entryApellido.get(), self.entryCedula.get(), self.entryTelefono.get(), self.entryCorreo.get()))


        boton_limpiar = tk.Button(self.ventanaPrincipal, text="Limpiar", command=lambda:self.limpiar_cajas())
        boton_limpiar_servicio = tk.Button(self.ventanaPrincipal, text="Limpiar", command=lambda:self.limpiar_cajas_servicio())
    
        self.ventanaPrincipal.title("Ventana Principal")
        self.ventanaPrincipal.state('zoomed')

        #Coordenadas de las entradas y texto principal
        labelNombre.place(x=20, y=40)
        self.entryNombre.place(x=120, y=40)
        labelApellido.place(x=20, y=80)
        self.entryApellido.place(x=120, y=80)
        labelCedula.place(x=20, y=120)
        self.entryCedula.place(x=120, y=120)
        labelTelefono.place(x=20, y=160)
        self.entryTelefono.place(x=120, y=160)
        labelCorreo.place(x=20,y=200)
        self.entryCorreo.place(x=120,y=200)

        #Coordenadas de las entradas y texto del servicio
        labelNombre_servicio.place(x=750, y=40)
        self.entryNombre_servicio.place(x=850, y=40)
        labelCedula_servicio.place(x=750, y=80)
        self.entryCedula_servicio.place(x=850, y=80)
        labelDescripcion_servicio.place(x=750, y=120)
        self.entryDescripcion_servicio.place(x=850, y=120)
        labelValor_servicio.place(x=750, y=160)
        self.entryValor_servicio.place(x=850, y=160)
        

        boton_guardar.place(x=130, y=230)
        boton_guardar_servicio.place(x=860,y=200)
        boton_consultar.place(x=875, y=260)
        boton_actualizar.place(x=1230, y=70)
        boton_limpiar.place(x=150,y=260)
        boton_limpiar_servicio.place(x=875,y=230)
        boton_consultar_cliente.place(x=145,y=290)
        boton_actualizar_cliente.place(x=480,y=70)
        

        label_idconsulta.place(x=1150, y=40)
        self.entryidconsulta.place(x=1200,y=40)
        label_idconsulta2.place(x=410, y=40)
        self.entryidconsulta2.place(x=450,y=40)

        label_info1.place(x=70,y=10)
        label_info2.place(x=800,y=10)
        label_info3.place(x=1000,y=360)
        label_info4.place(x=210,y=360)

        self.tabla.tabla.place(x=850,y=400,width=480)
        self.tabla2.tabla.place(x=60,y=400,width=530)

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                self.entryidconsulta.delete(0,tk.END)
                self.entryidconsulta.insert(0,str(valores[0]))
                self.entryNombre_servicio.delete(0,tk.END)
                self.entryNombre_servicio.insert(0, str(valores[1]))
                self.entryCedula_servicio.delete(0,tk.END)
                self.entryCedula_servicio.insert(0, str(valores[2]))
                self.entryDescripcion_servicio.delete(0,tk.END)
                self.entryDescripcion_servicio.insert(0, str(valores[3]))
                self.entryValor_servicio.delete(0,tk.END)
                self.entryValor_servicio.insert(0, str(valores[4]))


        def seleccionar_elemento1(_):
            for i in self.tabla2.tabla.selection():
                valores = self.tabla2.tabla.item(i)['values']
                self.entryidconsulta2.delete(0,tk.END)
                self.entryidconsulta2.insert(0,str(valores[0]))
                self.entryNombre.delete(0,tk.END)
                self.entryNombre.insert(0, str(valores[1]))
                self.entryApellido.delete(0,tk.END)
                self.entryApellido.insert(0, str(valores[2]))
                self.entryCedula.delete(0,tk.END)
                self.entryCedula.insert(0, str(valores[3]))
                self.entryTelefono.delete(0,tk.END)
                self.entryTelefono.insert(0, str(valores[4]))
                self.entryCorreo.delete(0,tk.END)
                self.entryCorreo.insert(0, str(valores[5]))
                
                

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        def borrar_elemento1(_):
            for i in self.tabla2.tabla.selection():
                self.comunicacion.eliminar_cliente(self.tabla2.tabla.item(i)['values'][0])
                self.tabla2.tabla.delete(i)


    
        self.tabla.tabla.bind('<<TreeviewSelect>>',seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>',borrar_elemento)
        self.tabla2.tabla.bind('<<TreeviewSelect>>',seleccionar_elemento1)
        self.tabla2.tabla.bind('<Delete>',borrar_elemento1)

        


        self.accion_consultar_todo_clientes(self.entryNombre.get(),self.entryApellido.get(),self.entryCedula.get(), self.entryTelefono.get(), self.entryCorreo.get())
        self.accion_consultar_todo(self.entryNombre_servicio.get(), self.entryCedula_servicio.get(), self.entryDescripcion_servicio.get(), self.entryValor_servicio.get())
        self.ventanaPrincipal.mainloop()

