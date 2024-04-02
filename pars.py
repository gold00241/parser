def simple_test(ans):
    line = ""
    quest = ""
    q = ""
    var_answers = "АБВГДЕЖЗИКЛМНОПРСТУФХКЦЧШЩЭЮЯ"
    while True:
        line = ans.readline()

        if not line:
            break

        if line[0] in var_answers and line[1] == ")":
            q+="\n"+line[0]+line[1]
            
        if line[-2] == "*":
            q+="*"
    return q
        



a = open("sample.txt", "r",encoding = "utf-8")


g = simple_test(a)
print (g)
print("------------------------")
a.close()
a = open("sample.txt", "r",encoding = "utf-8")
for i in a:
    print(i)




