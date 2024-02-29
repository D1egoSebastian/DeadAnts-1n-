#codigo normal

def antsfunction(ants):
    if ants is None:
        ants = ants.replace('ant', '') #replace "ant" for a empty chain cus we need the dead ants

    if ants is None or ants.strip() == '':
        return 0
    else:
        #count the "a" "n" "t" occurrences
        ants_a = ants.count('a')
        ants_n = ants.count('n')
        ants_t = ants.count('t')
        antss = ants.count('ant')
        

        count = max(ants_a, ants_n, ants_t) - antss   #find the maximum occurence between a, n . t
        #rest "ant" because we need the dead parts of an ant not the entire body
        return count

antsProblem = "...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t"
answer = antsfunction(antsProblem)

print("the number of dead ants is: " + str(answer))
