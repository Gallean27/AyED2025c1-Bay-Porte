# mazo.py
from modules.ListaDobleEnlazada import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada
from modules.carta import Carta 
class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

     
################


class Mazo:
    def __init__(self): # construcctor de la clase Mazo
        self.mazo = ListaDobleEnlazada() #
        self.carta = self
    def __len__(self): # devuekvo la cantidad de cartas que hay en el mazo
        return self.mazo.tamanio
    def poner_carta_abajo(self, nueva_carta):
        if type(nueva_carta) != Carta:
            raise TypeError("El elemento a agregar debe ser una carta")
        self.mazo.agregar_al_final(nueva_carta) # agrega una carta abajo
    def poner_carta_arriba(self, nueva_carta):
        if type(nueva_carta) != Carta:
            raise TypeError("El elemento a agregar debe ser una carta")
        self.mazo.agregar_al_inicio(nueva_carta) # agrego carta arriba

   # @property
    #def mazo(self):
    #    return self.mazo
    #@mazo.setter
    #def mazo(self, mazo_nuevo):
    #    self.mazo = mazo_nuevo
    def sacar_carta_arriba(self,mostrar=False):
        if self.mazo.esta_vacia():
            raise DequeEmptyError("El mazo está vacío")
        mazo = self.mazo.extraer(0) # extrae la carta de la cabeza
        if mostrar:
                mazo.visible = True
        return mazo  

    def sacar_carta_abajo(self):
        if self.mazo.estavacia():
            raise DequeEmptyError ("El mazo está vacío") 
        return self.mazo.extraer()  
    
    
    def esta_vacio(self):
        return self.__mazo.esta_vacia()

@property
def cabeza (self):
    if self.mazo.cabeza:
        return self.mazo.cabeza.dato
    return None

@property
def cola (self):
 return self.mazo.cola
