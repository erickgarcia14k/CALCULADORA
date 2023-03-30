class Persona():

    def __init__(self,nombre="",edad=0,dni=""):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    def validar_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(self.__dni)!=9:
            print("DNI incorrecto 1")
            self.__dni = ""
        else:
            letra = self.__dni[8]
            num = int(self.__dni[:8])
            if letra.upper() != letras[num % 23]:
                print("DNI incorrecto 2")
                self.__dni = ""

    @dni.setter
    def dni(self,dni):
        self.__dni=dni
        self.validar_dni()
      
    @edad.setter
    def edad(self,edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad=0
        else:
            self.__edad=edad
    
    
    def mostrar(self):
        return "Nombre:"+self.nombre+" - Edad:"+str(self.edad)+" - DNI:"+self.dni

    def esMayorDeEdad(self):
        return self.edad>=18
    
persona1=Persona()
persona1.nombre
persona1.edad
persona1.dni
#finalizando de imprimir lo qe se encuentra en e método constructor
persona2=Persona("Juan",5,"") 
persona2.nombre='Alberti'
persona2.edad=-1
persona2.dni="ASDEBFRNE"
print(persona2._Persona__nombre)  ##de esta forma Accedemos a la variable privada de nombre dentro de getter
print(persona2._Persona__edad)
print(persona2._Persona__dni)

##
persona3=Persona()
persona3.nombre='Eduardo'
persona3.edad=-1

##Recuerda se debe ir corriendo uno por uno de las lineas y al final el metodo  a llamar
persona4=Persona()
persona4.nombre="Pinocho"
persona4.edad=23
persona4.dni="ASDEBFRNEA"
persona4.mostrar() ##Regresa todos los datos
persona4.esMayorDeEdad()  ##Devuelve el método

