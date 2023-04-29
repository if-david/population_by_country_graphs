import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('python 102\\40_population_graph\\data.csv')
  filter_type = input("¿Qué tipo de filtro deseas utilizar? ('Rank' o 'Country'): ")

  result = utils.population_by_country(data, filter_type)
  # print(result)
  labels, values = utils.get_population(result)
  # print(labels, values)
    
  charts.generate_bar_chart(labels, values)


if __name__ == '__main__':
  run()