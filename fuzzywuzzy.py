def fuzzywuzzy(num): 

    if num%3==0 and num%5==0:
        print('fuzzy wuzzy')

    elif num%3==0:
        print('fuzzy')

    elif num%5==0:
        print('wuzzy')

    else:
        print(num)


number=int(input('enter number: '))

fuzzywuzzy(num=number)