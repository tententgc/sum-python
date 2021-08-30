class person:
    def __init__(self):
        self.fname = ""
        self.lanme = ""
        self.country = "Thailand"

    # def __init__(self, fname, lname, country):
    #     self.fname = fname
    #     self.lanme = lname
    #     self.country = country


class person2:
    def __init__(self, fname=None , lname=None, country="thailand"):
        self.fname = fname
        self.lname = lname
        self.country = country

    def __str__(self):
        return "fname:{} lname: {} country: {}  ".format(self.fname, self.lname, self.country)


if __name__ == "__main__":
    # p1 =person()
    # print(p1.fname)
    # print(p1.country)
    # p2 = person ("tentne", 'tgc',"thailand")
    # print(p2)

    p1 = person2()
    print(p1.fname)
    print(p1.country)

    p2 = person2(fname="peter")
    print(p2.fname,  p2.country)

    p3 = person2("peter", "perker")
    print(p3)

    p4 = person2(lname="tgc",fname= "tentne", country="USA")
    print(p4)