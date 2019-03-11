def merge_the_tools(string, k):

 # your code goes here

    subsequences  = int(len(string)/k)
    t_i = ''

    for i in range(0,len(string)):
        if i == 0:
            t_i = string[i:i+1]
        if (i+1)%k==0:
            if (not string[i:i+1] in t_i):
                t_i += string[i:i+1]
            print(t_i)
            t_i=''
            continue
        if (not string[i:i+1] in t_i):
            t_i += string[i:i+1]

string, k = input(), int(input())
merge_the_tools(string, k)
