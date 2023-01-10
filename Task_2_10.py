class Translator:
    Dict1 = {}
    def add(self, eng, rus):
        if eng in self.Dict1:
            if rus not in self.Dict1[eng]:
                self.Dict1[eng].append(rus)
        else:
            self.Dict1[eng] = [rus]


    def remove(self, eng):
        del self.Dict1[eng]

    def translate(self, eng):
        print(*self.Dict1.get(eng))


tr = Translator()

tr.add('tree','дерево')
tr.add('car','машина')
tr.add('car','автомобиль')
tr.add('leaf','лист')
tr.add('river','река')
tr.add('go','идти')
tr.add('go','ехать')
tr.add('go','ходить')
tr.add('milk','молоко')

print(tr.Dict1)

tr.remove('car')
tr.translate('go')
print(tr.Dict1)