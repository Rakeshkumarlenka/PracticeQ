# replace last value of tuples in a list

class Tuple_probs:
    def replace(self):
        my_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

        new_list = [i[:len(i) - 1] + (100,) for i in my_list]
        print(new_list)

res = Tuple_probs()
res.replace()