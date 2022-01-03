class dict_problem:
    def __init__(self):
        self.title = "Dictionary problem"
        self.dict = {'name': 'poornima', 'age': 25, 'mobileno': 9739935941}

    def dict_addkey(self):
        print("")
        print("1.add item into dictionary")
        self.dict.update({"address": "Banaswadi"})
        print(self.dict)
