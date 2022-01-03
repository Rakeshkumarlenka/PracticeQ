class Appsec():
    def appn(self):
        list1 = [6, 52, 74, 62]
        list2 = [85, 17, 81, 92]
        list2.extend(list1)
        return list2

app =Appsec()
print("new list is :",app.appn())