#funcion para encontrar el elemento mayoritario presente en una lista
def findMajoritaryElement(nums):
    
    d = {}
    #recorrer la lista y almacenar la frecuencia de cada elemento en un diccionario
    for i in nums:
        d[i] = d.get(i, 0) + 1
        
        #devolver el elemento si su cuenta es mayor que n/2
        
    for key, value in d.items():
        if value > len(nums)/2:
            return key
        
        #devolver -1 si no hay un elemento mayoritario

    return -1
        
if __name__ == '__main__':
    """
    #suposicion de entrada valida (el elemento mayoritario esta presente)
    nums = [1,8,7,4,1,2,2,2,2,2,2]
    result = findMajoritaryElement(nums)
    if result != -1:
        print("El elemento mayoritario es", result)
    else:
        print("No hay elemento mayoritario")
    """
    
    #ponemos un array vacio para posteriormente preguntar al usuario cuantos numeros quiere ingresar y asi llenar el array
    nums = []
    
    #hacemos un input para preguntar cuantos numeros quiere ingresar el usuario
   
    n = int(input("Cuantos numeros quieres ingresar? "))
    
    #hacemos un for para llenar el array
    for i in range(n):
        num = int(input("Ingrese los numeros: "))
        nums.append(num)
        
    result = findMajoritaryElement(nums)
    if result != -1:
        print("El elemento mayoritario es", result)
    else:
        print("No hay elemento mayoritario")
   