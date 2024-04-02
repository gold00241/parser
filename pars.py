def simple_test(ans):
    line = ""
    itog = ""
    var_answers = "АБВГДЕЖЗИКЛМНОПРСТУФХКЦЧШЩЭЮЯ"
    while True:
        line = ans.readline()

        if not line:
            break

        if line[0] in var_answers and line[1] == ")":
            itog+="\n"+line[0]+line[1]
            
        if line[-2] == "*":
            itog+="*"
    return itog


def vstavka_slova_predlozhenia(ans):
    itog = ""
    while True:
        line = ans.readline()

        if not line:
            break

        for simv in range(len(line)-2):
            if line[0] == "[" and line[-1] == "]":
                itog+=line[simv+1]
    return itog


def sootv(ans):

    itog = {}
    simv = 0

    while True:
        first_word = ""
        second_word = ""
        line = ans.readline()

        if not line:
            break

        if "==" in line:
            for simv in range(len(line)):
                if line[simv]=="=":
                    simv+=2
                    break
                first_word+=line[simv]

            if line[-1] == "\n":
                for simv1 in range(simv,len(line)-1):
                    second_word+=line[simv1]
            else:
                for simv1 in range(simv,len(line)):
                    second_word+=line[simv1]
                
            
            itog[first_word] = second_word
        
    return itog
                
                    
                    

    





##a = open("example_simple.txt", "r",encoding = "utf-8")
##g = simple_test(a)
##print (g)
##print("------------------------")
##a.close()
##
##
##a = open("example_vstavka.txt", "r",encoding = "utf-8")
##b=vstavka_slova_predlozhenia(a)
##print(b)
##a.close()
##print("------------------------")
##a = open("example_sootv.txt", "r",encoding = "utf-8")
##c = sootv(a)
##print(c.items())

test = open("full_test.txt","r",encoding = "utf-8")
quest = open("quest.txt","w+",encoding = "utf-8")
k=0
line = ""


while True:
    line = test.readline()

    if not line:
        break

    
    if (type(line[0]) == int and line[1] == ")"):
        open("quest.txt","w").close()
        

    quest = open("quest.txt","w+",encoding = "utf-8")
    quest.write(line)
        
            
        
        
    



