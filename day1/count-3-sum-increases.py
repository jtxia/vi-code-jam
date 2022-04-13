with open("input.txt","r") as f:
    lines = f.readlines()
    count = 0
    prev_sum = lines[1]
    for i in range(2,len(lines)):
        #TODO: up to lines[2]
        curr_sum = int(lines[i])+int(lines[i-1])+int(lines[i-2])
        
        # Detect an increase
        if curr_sum > prev_sum:
            increase = 1
            count = count + 1
        else : 
            increase = 0
        prev_sum = curr_sum
        print(i, ": ", curr_sum, increase)
    print(count)