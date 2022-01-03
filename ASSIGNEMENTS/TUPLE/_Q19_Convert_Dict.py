#convert a list of tuples into a dictionary

class Tuple_probs:
    def convert_dic(self):
        my_list = [('a', 1), ('b', 2), ('a', 5)]
        my_dict = {}
        for i in my_list:
            my_dict.setdefault(i[0], []).append(i[1])
        print(my_dict)

res = Tuple_probs()
res.convert_dic()