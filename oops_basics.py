'''
find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.
'''
# class BinarySearch:
#     def __init__(self,cards):
#         self.cards = cards
#     def find_positions(self):
#         pass

# def main():
#     cards = [13, 11, 10, 7, 4, 3, 1, 0]
#     bs = BinarySearch(cards)
#     print(bs.find_positions())


class Second:

    def __init__(self,mainobj):
        super().__init__()
        self.m1=1
        self.m1=1
        self.m1=1
        self.m1=1
        self.mainobj = mainobj()

    def changessss(self):
        print("123123123",self.mainobj.name,self.mainobj.last_name)
        return self.main.name,self.main.last_name

class MainClass():

    def __init__(self):
        self.name = None
        self.last_name = None
    

    def Change_name(self):
        print("self name",self.name)
        self.name = "John"
        print("self name",self.name)
        print("self.last_name",self.last_name)
        

    def change_last_name(self):
        print("lkast_name",self.last_name)
        self.last_name = "Doe"
        print("lkast_name",self.last_name)
    
    def print_name(self):
        self.Change_name()
        self.change_last_name()
        print("name is",self.name)
        print("latname is",self.last_name)
        return self.name,self.last_name




obj = MainClass()




name1,name2 = obj.print_name()
print("name1",name1)
print("name2",name2)