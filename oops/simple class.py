class player:
     def __init__(self):
         self.fname = ""
         self.lname = ""
         self.number = ""
class player2:
    def __init__(self,fname,lname,number):
        self.fname = fname
        self.lname = lname
        self.number = number


if __name__ == "__main__":
    p1 =player()
    p1.fname ='louis'
    p1.lname = 'buapakong'
    p1.number = 10 #

    p2 =player()
    p2.fname ="alex"
    p2.lname = "jjffjds"
    p2.number = 2

    p1a = player2("tenten","tgcc",1)
    p2a = player2("penguin","ppkkw",1)
    
    print(p1a.fname)
    print(p2.fname) 