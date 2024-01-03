stdata={}
list=['id','name','city']

for i in range(len(list)):
    v=input(f"enter your value for {list[i]}:")
    stdata[list[i]]=v
    
print(stdata)