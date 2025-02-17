
class UserChoiceHandler:
    def __init__(self,input,choice):
        self.input = input
        self.choice = choice
        print("Choices : ")
        print("Enter 1 to search cards")
    def choice_handler(self):
        if self.choice == 1:
            print("Performing search on cards :")
            print("Choices : ")
            print("Enter 1 for if you want to input your own data")
            print("Enter 2 if just want to bench mark his feature using pre-defined test cases")
            choice = int(input("Enter your choice : "))
            if choice == 1:
                arr_size = int(input("Enter the size of a list:"))
            arr = []
            for i in range(arr_size):
                element = int(input(f"Enter list element {i+1} : "))
                arr.append(element)

            query = int(input("Enter the number (card) that you want to search :"))
            input = {
                'input':{
                    'cards':arr,
                    'query':query
                }
            }
            locate_card_obj = LocateCard(input)
            locate_card_obj.locate_card()