import csv

class CSVReader:

    csv_data = []

    def __init__(self, filepath):

        with open(filepath) as files:
            csv_file = csv.reader(files, delimiter = ',')
            for row in csv_file:
               self.csv_data.append(row)
        pass


