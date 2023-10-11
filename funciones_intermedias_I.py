#1
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#actualizar valores:

#cambio del valor de 10 en x a 15:
x[1][0] = 15
print(x)

#cambio el apellido del primer estudiante de Jordan  Bryant:
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)

#cambio en el directorio Messi por Andres:
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)

#cambio el valor 20 por 30 en z:
z[0]['y'] = 30
print(z)

#2

def iterateDictionary(some_list):
    for diccionario in some_list:
        output = ""
        for clave, valor in diccionario.items():
            output += f"{clave} - {valor}, "
        print(output[:-2])  # Esto elimina la coma y el espacio extra al final

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(estudiantes)

#3

def iterateDictionary2(key_name, some_list):
    for diccionario in some_list:
        if key_name in diccionario:
            print(diccionario[key_name])

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

#4
def printInfo(some_dict):
    for clave, lista in some_dict.items():
        print(len(lista), clave.upper())
        for elemento in lista:
            print(elemento)

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)



