class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        #starting with na empty jar
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        #adding n cookies to the jar
        self._size+=n
        if self._size > self.capacity:
            raise ValueError  

    def withdraw(self, n):
        if n > self._size:
            raise ValueError
        self._size-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

my_jar = Jar()

#should output 5 cookies
my_jar.deposit(5)
print(str(my_jar))

#should output 3 cookies
my_jar.withdraw(1)
print(str(my_jar))

print(my_jar.size)
print(my_jar.capacity)

