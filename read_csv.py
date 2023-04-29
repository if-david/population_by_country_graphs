import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    # print(header)
    data = []
    data = [{key: value for key, value in zip(header, row)} for row in reader]
    return data



'''
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    # print(header)
    data = []
    for row in reader:
      iterable = zip(header, row)
      # print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      # print(country_dict)
      data.append(country_dict)
    return data
'''