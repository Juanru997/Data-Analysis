# Xinyu Gu  xg764
def words_for_numbers(n):
    lenth=len(n)
    dic1={
        "0":"zero",
        "1":"one",
        "2":"two",
        "3":"three",
        "4":"four",
        "5":"five",
        "6":"six",
        "7":"seven",
        "8":"eight",
        "9":"nine"
        }
    dic2={
        "10":"ten",
        "11":"eleven",
        "12":"twelve",
        "13":"thirteen",
        "14":"fourteen",
        "15":"fifteen",
        "16":"sixteen",
        "17":"seventeen",
        "18":"eighteen",
        "19":"nineteen",
        }
    dic3={
        "2":"twenty",
        "3":"thirty",
        "4":"fourty",
        "5":"fifty",
        "6":"sixty",
        "7":"seventy",
        "8":"eighty",
        "9":"ninety"
        }
    if lenth==1:
        print(dic1[n])
    elif lenth==2:
        if n[0]=="1":# "1*"
            print(dic2[n])
        elif n[1]=="0": # "*0"
            print(dic3[n[0]])
        else:
            print(dic3[n[0]],dic1[n[1]])
    elif lenth==3:
        if n[1]=="1":# "*1*"
            print(dic1[n[0]],"hundred",dic2[n[1:]])
        elif n[2]=="0" and n[1]!="0":# "**0"
            print(dic1[n[0]],"hundred",dic3[n[1]])
        elif n[2]==n[1]=="0":# "*00"
            print(dic1[n[0]],"hundred")
        elif n[1]=="0" and n[2]!="0": # "*0*"
            print(dic1[n[0]],"hundred and",dic1[n[2]])
        else:
            print(dic1[n[0]],"hundred",dic3[n[1]],dic1[n[2]])
def main():
    n=input("Enter a number between 0 and 999: ")
    words_for_numbers(n)
main()
    



















        
        

        
