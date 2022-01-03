# to remove an empty tuple(s) from a list of tuples

class Tuple_probs:
    def empty_tup(self):
        my_list = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
        new_list = [i for i in my_list if i]
        print(new_list)

res = Tuple_probs()
res.empty_tup()