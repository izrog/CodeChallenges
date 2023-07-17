# izrog
# We want to create a function that will add numbers together when called in succession.
# add(1)(2) # equals 3
# add(1)(2)(3)  6
# add(1)(2)(3)(4)  10
# add(1)(2)(3)(4)(5)  15

class add(int):
    def __call__(self, n):
        return add(self + n)