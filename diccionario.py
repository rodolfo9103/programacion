def traducir(diccionario):


    input_usuario = input('Ingrese una frase: ')

    while input_usuario != 'Quit':
        traduccion = []
        for palabra in input_usuario.split():
            if palabra in diccionario.keys():
                traduccion.append(diccionario[palabra])
            else:
                traduccion.append('__')

        print(' '.join(traduccion))
        input_usuario = input('Ingrese una frase: ')

es_en = {'estrella':'star', 'es':'is', 'nombre':'name', 'rojo':'red', 'azul':'blue', 'anarrillo':'yellow', 'nergo':'black',
'brujo':'witcher', 'mago':'witzar', 'cielo':'sky', 'computadora':'computer', 'casa':'house', 'ratos':'mouse', 'ciudad':'city', 
'llamar':'call', 'universidad':'universty', 'edad':'age', 'cuarto':'room', 'perro':'dog', 'gato':'cat' }

traducir(es_en)