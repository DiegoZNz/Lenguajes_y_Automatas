from random import randrange

#funcion de utilidad para intercambiar elementos 'A[i]' y 'A[j]' de una lista 'A'

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

#función para barajar una lista 'A' 

def shuffle(A):
    #lista de lectura desde el indice mas bajo hasta el mas alto
    for i in range(len(A)):
        #genera un número aleatorio 'j' tal que 'i <= j < n'
        j = randrange(i, len(A))
        
        #intercambia el elemento actual con el elemento aleatorio generado
        swap(A, i, j)
        
if __name__ == '__main__':
    
    A = [1, 2, 3, 4, 5, 6]

    shuffle(A)
    
    #imprime la lista barajada
    print(A)
    