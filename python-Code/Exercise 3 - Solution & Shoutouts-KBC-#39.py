questions = [["Which languagewase use to create Fb ?","Python","French","javaScript","PhP","None",4],
            ["Which languagewase use to create Fb ?","Python","French","javaScript","PhP","None",4],
            ["Which languagewase use to create Fb ?","Python","French","javaScript","PhP","None",4],
            ["Which languagewase use to create Fb ?","Python","French","javaScript","PhP","None",4],
            ["Which languagewase use to create Fb ?","Python","French","javaScript","PhP","None",4],
            ["Which languagewase use to create Fb ?","Python","French","javaScript","PhP","None",4],
            ["Which languagewase use to create Fb ?","Python","French","javaScript","PhP","None",4],
            ["Which languagewase use to create Fb ?","Python","French","javaScript","PhP","None",4],
            ["Which languagewase use to create Fb ?","Python","French","javaScript","PhP","None",4],
            ]
levels = [1000 ,2000, 4000,80000,16000,32000,64000,128000,2000000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f'\nQuestion for Rs: {levels[i]}')
    print(f'a. {question[1]}        b. {question[2]}')
    print(f'c. {question[3]}        d. {question[4]}')
    reply = int(input("Enter the answer ( 1to4 ): "))
    if(reply ==question[-1]):
        print(f"Coorect the answer , You have won Rs. {levels[i]}")
        if(i == 4):
            money =  2000
        elif(i==6):
            money = 8000
        elif(i==9):
            money = 2000000
    else:
        print("Wrong Answer!")
        break
print(f"Ab ya sb paisa lakr nilkalo {money}")