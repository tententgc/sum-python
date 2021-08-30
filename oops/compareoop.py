import math


def demo_tuple():
    p12 = "joe", 'gomex', 12
    print(p12)
    print(p12[2])


def demo_dictionary():
    p12 = {"fname": "joe", "lname": "gomez", "number": 12}
    print(p12)
    print(p12['lname'])


class player:
    pass


class player2:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.number = 0


class player3:
    def __init__(self,  fname, lanme, number):
        self.fname = fname
        self.lname = lanme
        self.number = number


def demo_simple_player_class():
    p12 = player
    p12.fname = "joe"
    p12.lname = "Gomez"
    p12.number = 12
    print(p12.lname)


def demo_simple_player2_class():
    p12 = player2()
    p12.fname = "joe"
    p12.lname = "Gomez"
    p12.number = 12
    print(p12.lname)


def demo_simple_player3_class():
    p12 = player3("joe", "gomez", 12)
    print(p12.fname)


if __name__ == "__main__":
    demo_simple_player_class()

demo_simple_player3_class()
