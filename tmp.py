source = 'tmp.txt'

class Test:
    def __init__(self):
        self._variable = ''

    @property
    def variable(self):
        with open(source, 'r') as f:
            self._variable = f.read()
        return self._variable

    @variable.setter
    def variable(self, value):
        self._variable = self._variable + value
        with open(source, 'w') as f:
            f.write(self._variable)


t = Test()
t.variable = 'mama'
with open(source) as f:
    print(f.read())

t.variable = 'tata'
with open(source) as f:
    print(f.read())
