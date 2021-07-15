class Stack:
 
    # Inicializa la pila
    def __init__(self, size):
        self.pila = [None] * size
        self.capacidad = size
        self.top = -1
    
    # Permite regresar el contenido de la pila como una lista mediante la función print()
    def __str__(self):
        return str(self.pila)

    # Función push() para añadir elementos a la pila
    def push(self, x):
        if self.is_full():
            print("Desbordamiento de pila.")
            exit(1)
        print("Se insertó", x, "en la pila.")
        self.top = self.top + 1
        self.pila[self.top] = x
 
    # Función pop() para eliminar el elemento superior de la pila
    def pop(self):
        if self.is_empty():
            print("Desbordamiento de pila.")
            exit(1)
        print("Eliminando", self.peek(), "de la pila.") 

    # Reduce tamaño de pila por 1
        top = self.pila[self.top]
        self.top = self.top - 1
        return top
    
    # Función peek() que regresa el valor del último elemento insertado a la pila
    def peek(self):
        if self.is_empty():
            exit(1)
        return self.pila[self.top]
 
    # Función size() que regresa como valor el tamaño de la pila
    def size(self):
        return self.top + 1
 
    # Función is_empty() para revisar si la pila está vacía
    def is_empty(self):
        return self.size() == 0
 
    # Función is_full() para revisar si la pila está llena
    def is_full(self):
        return self.size() == self.capacidad
 
 
if __name__ == '__main__':
 
    pila_ejemplo = Stack(6)
 
    pila_ejemplo.push('Ejemplo')    # Inserta elementos en la pila, función push()
    pila_ejemplo.push('de')
    pila_ejemplo.push('uso')
    pila_ejemplo.push('de')
    pila_ejemplo.push('una')
    pila_ejemplo.push('pila')

    print(pila_ejemplo.peek())      # Muestra cuál es el último elemento de la pila
                                    # en este caso el valor es la cadena 'pila'
    
    print(pila_ejemplo)             # Regresa el contenido de la pila en forma de lista 
                                    # en este caso, la frase 'Ejemplo de uso de una pila'

    pila_ejemplo.pop()              # Función pop() quita el último elemento de la pila
    pila_ejemplo.pop()
    pila_ejemplo.pop()
    pila_ejemplo.pop()
    pila_ejemplo.pop()
    pila_ejemplo.pop()

    pila_ejemplo.push('pila')       # Función push(), inserta elementos en la pila
    pila_ejemplo.push('una')        # En este caso en orden invertido
    pila_ejemplo.push('de')
    pila_ejemplo.push('uso')
    pila_ejemplo.push('de')
    pila_ejemplo.push('Ejemplo')

    print(pila_ejemplo.peek())      # Muestra cuál es el último elemento de la pila
                                    # en este caso el valor es la cadena 'Ejemplo'
    
    if pila_ejemplo.is_empty():     # Revisa si la pila está vacía, función is_empty()
        print('Pila vacía =', True)
    elif pila_ejemplo.is_full():    # Revisa si la pila está llena, función is_full()
        print('Pila llena =', True)
    else:                           # En caso de que la pila contenga elementos pero no esté ni llena ni vacía
        print('Pila llena/vacía =', False)

    print(pila_ejemplo)             # Regresa el contenido de la pila en forma de lista 
                                    # en este caso, la frase 'pila una de uso de Ejemplo'