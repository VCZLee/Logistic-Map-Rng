class LogisticRNG:
    def random(self, n, initial_value, list):
        import math as m
        if list == 1:
            loglist = []
            x = initial_value
            for i in range(0, n):
                x = 4 * x * (1 - x)
                loglist.append((2/m.pi)*m.asin(x ** 0.5))
            return loglist
        else:
            x = initial_value
            for i in range(0, n):
                x = 4 * x * (1 - x)
            return x

    def exact(self, n, initial_value):
        import math as m
        theta = (1 / m.pi) * m.asin(initial_value ** 0.5)
        x = m.sin((2 ** n) * theta * m.pi) ** 2
        return x

    def rng(self, number, seed, starting_point, skip):
        import math as m
        length = (int(number) * int(skip + 1)) + int(starting_point)
        loglist = []
        x = seed
        for i in range(0,length + 1):
            x = 4 * x * (1 - x)
            if i <= starting_point:
                pass
            else:
                if i % (skip + 1) == 0:
                    loglist.append((2 / m.pi) * m.asin(x ** 0.5))
        return loglist