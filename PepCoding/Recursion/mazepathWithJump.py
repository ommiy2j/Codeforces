def mazepath(sr,sc,dr,dc,path):
    if sr==dr and sc==dc:
        print(path)
        return
    for i in range(1,(dc-sc)+1):
        mazepath(sr,sc+i,dr,dc,path+"h"+str(i))
    for i in range(1,(dr-sr)+1):
        mazepath(sr+i,sc,dr,dc,path+"v"+str(i))
    for i in range(1,((dr-sr)+1 and (dc-sc)+1)):
        mazepath(sr+i,sc+i,dr,dc,path+"d"+str(i))
        
        
n=int(input())
m=int(input())
mazepath(1,1,n,m,path="")