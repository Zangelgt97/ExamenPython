import requests
payload = {'comentario': 'Está genial', 'estrellas': 5}
r = requests.post('https://miapi.com/comentarios/', json=payload)
    
class write_test:

    def leer_archivo(self):
                archivo = open("Ejercicio1-3/Clientes.txt")
                #i = 1  # contador de la linea
                x=0
                for linea in archivo:
                    linea = linea.rstrip() #(\\n) # La funcion rstrip("\\n") remieven el caracter del final de la linea
                    #print("linea #%1d:  %s" % (i, linea))
                    print(linea)
                    linea2=linea.replace(' ','')
                    sr=linea2.replace(',',' ')
                    print(sr)
                    linea3=sr.rsplit()
                    print(linea3)   
                    print(linea3[0])
                    print(linea3[1])
                    print(linea3[2])
                    print(linea3[3])
                    print(linea3[4])
                    x=x+1
                    y=str(x)
                    payload = {'id': "1", 'surname': linea3[1],'firstname':linea3[0]}
                    r = requests.post('http://localhost:8080/Examen2Employee/NewEmployee', json=payload)
                    payload = {'id': "1", 'code': y,'name':linea3[2]}
                    r = requests.post('http://localhost:8080/Examen2Country/NewCountry', json=payload)
                    payload = {'id': "1", 'code': y,'name':linea3[3]}
                    r = requests.post('http://localhost:8080/Examen2Language/NewLanguage', json=payload)
                    payload = {'id': "1", 'name': linea3[4]}
                    r = requests.post('http://localhost:8080/Examen2Airport/NewAirport', json=payload)
                    print(y)
                   
                    
                archivo.close()
    #Cursor=Conectar.cursor()
    def Apy_rest(self):
        print("Enviando Formulario")



usuario1=write_test()
usuario1.leer_archivo()
usuario1.Apy_rest()