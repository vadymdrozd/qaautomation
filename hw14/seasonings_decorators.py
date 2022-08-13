def cinnamon(cls):
    def wrapper():
        def add_cinnamon(self):
            return 30
        cls.add_cinnamon = add_cinnamon
        return cls
    return wrapper()


def vanilla(cls):
    def wrapper():
        def add_vanilla(self):
            return 25
        cls.add_vanilla = add_vanilla
        return cls
    return wrapper()


def milk(cls):
    def wrapper():
        def add_milk(self):
            return 15
        cls.add_milk = add_milk
        return cls
    return wrapper()
