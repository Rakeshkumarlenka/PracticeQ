# unzip a list of tuples into individual lists.

class Tuple_probs:
    def unzip(self):
        my_list = [(1, 2), ('a', 'b'), (True, False)]
        new_list = []
        for i in my_list:
            new_list.append(list(i))
        print(*new_list)

res = Tuple_probs()
res.unzip()