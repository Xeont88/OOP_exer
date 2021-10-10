class Counter:
    counter = 0

    def start_from(self, counter=0):
        self.counter = counter
        print('start from, self', self)

    def increment(self):
        self.counter += 1

    def reset(self):
        self.counter = 0

    def display(self):
        print('Текущее значение счетчика: =',
              self.counter)


c1 = Counter()
print('c1', c1)
c2 = Counter()
print('c2', c2)

Counter.counter = 10
print(c1.counter)
print(c2.counter)


