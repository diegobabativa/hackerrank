string = input("Please, type the String \n");
vowels = ['A', 'E', 'I', 'O', 'U'];

strl = len(string)
kevin = int(sum(strl-i for i in range(strl) if string[i] in vowels))
Stuart = int(strl*(strl+1)/2 - kevin)

if kevin > Stuart:
    print('Kevin', kevin)
elif kevin < Stuart:
    print('Stuart', Stuart)
else:
    print('Draw')
    
