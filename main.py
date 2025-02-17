from lists_based_problems.binary_search import LocateCard


# arr_size = int(input("Enter the size of a list:"))
# arr = []
# for i in range(arr_size):
#     element = int(input(f"Enter list element {i+1} : "))
#     arr.append(element)

# query = int(input("Enter the number (card) that you want to search :"))
# arrange_desc_obj = ArrangeInAscendingOrder(arr,query)
# desc_array = arrange_desc_obj.arrnage_in_ascending_order()
# print(f"Sorted array in descending order : {desc_array}")

# test = {
#         'input':{
#             'cards':[13,11,10,7,4,3,1,0],
#             'query':1
#         },
#         'output':6
#     }
test = {
        'input':{
            'cards':[2,32,16,4,64,8,256,128],
            'query':1
        },
        'output':6
    }
locate_card_obj = LocateCard(test)
locate_card_obj.locate_card()

# test_cases_for_binary_search = []
# test_cases_for_binary_search.append(
#     {
#         'input':{
#             'cards':[13,11,10,7,4,3,1,0],
#             'query':1
#         },
#         'output':6
#     }
# )
