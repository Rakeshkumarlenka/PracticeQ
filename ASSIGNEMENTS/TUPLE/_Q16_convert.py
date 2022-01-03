#convert a tuple to a dictionary

class Tuple_probs:
    def convert(self):
        my_tuple = ('a', 1, 'b', 2)

        my_dict = {}
        for i in range(0, len(my_tuple), 2):
            my_dict[my_tuple[i]] = my_tuple[i + 1]
        print(my_dict)

res = Tuple_probs()
res.convert()