with open("input.txt","r") as f:
    lines = f.readlines()
    count = 0
    for i in range(1,len(lines)):
        diff = int(lines[i])-int(lines[i-1])
        
        # Detect an increase
        if diff > 0:
            #increase = 1
            count = count + 1
        #else : 
            #increase = 0
        #print(i, ": ", lines[i-1], increase)
    print(count)