import csv, datetime


class Weather:
    def __init__(self, date, temperature, pressure, clouds, rains):
        self.date = date
        self.temperature = temperature
        self.pressure = pressure
        self.clouds = clouds
        self.rains = rains
        # self.day=self.date.split("-"), self.month, self.year

    def __it__(self, to_check):
        # return self.date,self.temperature,self.pressure,self.clouds,self.rains < to_check.date,to_check.temperature,to_check.pressure,to_check.rains
        return self.date < to_check.date

    def __str__(self):
        return f'{self.date} {self.temperature} {self.pressure} {self.clouds} {self.rains}'


def read_from(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file, dialect="excel",
                                fieldnames=["date", "temperature", "pressure", "clouds", "rains"])
        for line in reader:
            res = Weather(line["date"], line["temperature"], line["pressure"], line["clouds"], line["rains"])
            weather.append(res)


weather = []
read_from('Weather1.csv')
read_from('Weather2.csv')

for item in weather:
    print(item)

sort_res = sorted(weather)
for i in sort_res:
    print(i)