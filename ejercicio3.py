# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:21:44 2022

@author: erick
"""

from ejercicio2 import Cuenta  ##De esa forma heredamos desde otra clase, recuerden que heredan atributos y metodos 
#pero tambien esta misma clase puede tener sus propios atributos y metodos, es decir la calse CuentaJoven es una sub clase de Cuenta
class CuentaJoven(Cuenta):
    
    #Declarando el metodo constructor , su objetivo es inicializar los atributos 
    def __init__(self,titular,cantidad=0,bonificacion=0):
        ##Utilizamos la Funcion super() para hacer referencia al padre
        super().__init__(titular,cantidad)
        self.bonificacion=bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion
    
    #declarando el método mostrar
    def mostrar(self):
        return "Cuenta Joven\n"+"Titular:"+self.titular.mostrar()+" - Cantidad:"+str(self.cantidad)+ "- Bonificación:"+str(self.bonificacion)+"%"
   
    def esTitularValido(self):
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()
    
    def retirar(self,cantidad):
        if not self.esTitularValido():
            print ("No puesdes retirar el dinero. titular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)
    