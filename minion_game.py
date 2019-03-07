string = input("Please, type the String \n");
vowels = ['A', 'E', 'I', 'O', 'U'];
kevin_vowel_list = [];
stuart_cons_list = [];

if len(string)>0 and len(string)<=10000000:
    for i in range(0,len(string)):
        for pivote in range(i+1,len(string)+1):
            if string[i:pivote][0] in vowels:
                kevin_vowel_list.append(string[i:pivote])
            else:
                stuart_cons_list.append(string[i:pivote])

kevin_counter=len(kevin_vowel_list)
stuart_counter=len(stuart_cons_list)

if kevin_counter>stuart_counter:
        print('Kevin', kevin_counter)
elif kevin_counter<stuart_counter:
        print('Stuart', stuart_counter)
else:
        print('Draw')
