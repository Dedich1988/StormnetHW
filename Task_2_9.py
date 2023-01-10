lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 12 1200']

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for x in data:
            self.lst_data.append(dict(zip(self.FIELDS,x.split())))


    def select(self, a, b):
        self.lst_data[a: b+1]

data = DataBase()
data.insert(lst_in)
print(data.lst_data)


