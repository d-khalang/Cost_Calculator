def counting(mlist):
    if "=" in mlist:
        splitted_list = mlist.strip().split("=")
        #print(splitted_list)
        mlist = splitted_list[-1]
        #print(mlist)
        value = float(mlist)
    else:
        try:
            splitted_list = mlist.strip().split("+")
            new_list = [float(n) for n in splitted_list]
            value = sum(new_list)
        except ValueError:
            value = "exception"
    return value



def CostCalculation(file_name):
    doc = open(file_name, "r")
    sum = 0
    for line in doc:
        #print("the doc: ", line)
        #print(line.lstrip()[0:7])
        if line.lstrip()[0:7].lower() != "refund":
            if ":" in line:
                sline = line.split(":")[1].strip()
                #print(sline)
                try:
                    print("the numbet is: ", float(sline))
                    sum += float(sline)
                except:
                    #sline.strip().split()
                    #print("not a number: ", sline ) #new string line
                    if "+" in sline:
                        value = counting(sline)
                        print("counted number is: ",value)  
                        if value != "exception":
                            sum += value   
                    else:
                        print("exception: ", sline)     
        else:
            print(line)
            sline = line.split(":")[1].strip()
                #print(sline)

            print("the refund is: ", float(sline))
            sum -= float(sline)
        print("till now sum is: ", sum)
                
    return sum            
            
        #print(line)
    #print(doc.readline())





print(CostCalculation("costs.txt"))