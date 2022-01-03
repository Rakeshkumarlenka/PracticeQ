# count the elements in a list until an element is a tuple

class Tuple_probs:
    def count_tup(self):
        my_list = [1, 2, 3, (4,), 5, 6]
        counter = 0
        for i in my_list:
            if not isinstance(i, tuple):
                counter += 1
            else:
                break
        print(counter)

res = Tuple_probs()
res.count_tup()