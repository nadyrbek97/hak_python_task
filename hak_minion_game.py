vow = 'AEOIU'

z = 0
counter_one = 0
counter_two = 0
def minion_game(word) :
    global z, counter_one, counter_two
    def recursion_fnc(st) :
        global z, counter_one, counter_two    

        if(z == 0) :
            counter_one += 1
        else:
            counter_two += 1
        if( st + 1 < len(word)):
            recursion_fnc(st+1);
    for i in range(0, len(word)) :
        recursion_fnc(i)
        if( word[i] in vow):
            z = 0
        else:
            z = 1
    
word = str(input())
minion_game(word)
if counter_one > counter_two:
    print ("Stuart " + str(counter_one))
else:
    print ("Kevin " + str(counter_two))
