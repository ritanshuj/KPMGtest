

def keyvalue (dicts, key):
    flag= True

    for item,valu in dicts.items():
        if item==key and type(valu) is not dict:
            print(valu)
            flag=False
            
            
        else:
            
            keyvalue(valu,key)
        

       
    if flag:
        print("key not found")
 
testDict={"a":{"b":{"c":"d"}}}


keyvalue(testDict,"a")