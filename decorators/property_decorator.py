class Foo:
    def __init__(self, bar):
        self._bar = bar
        
    @property
    def bar(self):
        print("Get 'bar'")
        return self._bar
        
    @bar.setter
    def bar(self, value):
        print("Set 'bar'")
        self._bar = value
        
foo = Foo(42)

print(foo.bar)

foo.bar = 43
print(foo.bar)
