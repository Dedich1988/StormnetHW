import sys


class StreamData:
    def create(self, fields, lst_values):

        self.FIELDS = fields
        self.lst_in = lst_values

        if len(self.FIELDS) != len(self.lst_in):
            return False
        else:
            self.dict1 = {x: y for x, y in zip(self.FIELDS, self.lst_in)}
            return True




class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res



sr = StreamReader()
data, result = sr.readlines()