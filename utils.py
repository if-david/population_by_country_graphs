def get_population(filtered_data):
    population_dict = {}
    for key in filtered_data[0].keys():
        # print(filtered_data[0][key])
        if key.endswith('Population'):
            population_year = key.split(' ')[0]
            population = filtered_data[0][key]
            population_dict[population_year] = int(population)
    # print (population_dict)
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values
    

#Filtro de entrada
def population_by_country(data, filter_type):
    if filter_type == 'Rank':
        try: 
            position = int(input("Ingresa el valor que deseas imprimir? (1 - 234): "))
            filtered_data = [rank for rank in data if int(rank['Rank']) == position]
        except:
            print('Debes ingresar un número (entre 1 y 234)')
            exit()
        return filtered_data    
    elif filter_type == 'Country':
        try:
            country_name = input("Ingresa el país que deseas filtrar: ")
            filtered_data = [country for country in data if country['Country'] == country_name]
            if len(filtered_data) == 0:
                raise ValueError('No se encontraron países con ese nombre')
        except ValueError as error:
            print(str(error))
            exit()
        return filtered_data    
    else:
        print("Ingresa un tipo de filtro válido")
        
        exit()
