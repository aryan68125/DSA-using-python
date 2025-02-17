class ArrangeInAscendingOrder:
    def __init__(self,arr):
        self.arr = arr
    def arrnage_in_ascending_order(self):
        self.arr.sort(reverse=True)
        return self.arr
'''
List of possible variations that we might encounter:
1. The number query occurs somewhere in the middle of the list cards.
2. query is the first element in cards.
3. query is the last element in cards.
4. The list cards contains just one element, which is query.
5. The list cards does not contain number query.
6. the card list is empty.
7. The list cards contains repeating numbers
8. The number query occurs at more than one position in cards
'''
class LocateCard(ArrangeInAscendingOrder):
    def __init__(self,input):
        super().__init__(input['input']['cards'])
        self.arr = input['input']['cards']
        self.query = input['input']['query']
    '''
    This method will perform binary search to locate cards
    on the basis of query input provided by the user
    '''
    def locate_card(self):
        desc_array = self.arrnage_in_ascending_order()
        print(f"desc_array ==> {desc_array}, query ==> {self.query}")
        