import csv

class Reader:
    def __init__(self, name, surname, r_num):
        self._name = name
        self._surname = surname
        self._r_num = r_num

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, val):
        self._surname = val

    @property
    def specialization(self):
        return self.r_num

    @specialization.setter
    def specialization(self, val):
        self._r_num = val

    def __str__(self):
        return self._name + " " + self._surname + "\n\t" + self._r_num

    def __str__(self):
        return f'{self._name}, {self._surname}, {self._r_num}'

    def __repr__(self):
        return self.__str__()

class Booking(Reader):
    def __init__(self, r_num, author,title,janre):
        Reader.__init__(self, r_num)
        self._author = author
        self._title=title
        self._janre=janre

with open ('reader.csv','r') as reader:
    csv_reader = csv.DictReader(reader)
   # next(csv_reader)

    with open('res.csv','w') as w_reader:
        fieldnames = ['name','surname','r_num']
        csv_writer = csv.DictWriter(w_reader, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)

with open ('booking.csv','r') as books:
    csv_reader = csv.reader(books)
    for line in books:
        print (line[2])


