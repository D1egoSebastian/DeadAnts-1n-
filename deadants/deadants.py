def antsfunction(ants):
    a_counter = 0
    n_counter = 0
    t_counter = 0
    ant_counter = 0
   
    for i in range(len(ants)):
        if ants[i] == 'a' and (i >= len(ants) - 2 or ants[i+1:i+3] != 'nt'):
            a_counter += 1
      
        elif ants[i] == 'n' and (i >= len(ants) - 2 or ants[i+1:i+3] != 'ta'):
            n_counter += 1
    
        elif ants[i] == 't' and (i >= len(ants) - 1 or ants[i+1] != 'a'):
            t_counter += 1
      
        elif i < len(ants) - 2 and ants[i:i+3] == 'ant':
           ant_counter += 1
      

    count = max(a_counter, n_counter, t_counter) - ant_counter
    return count

antsProblem = "...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t"
answer = antsfunction(antsProblem)

print("the number of dead ants is: " , answer)