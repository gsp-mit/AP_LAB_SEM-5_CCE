lis=[]
n=int(input('enter no of entries'))

def enter_details():
    name=input('EnterName: ')
    regno=input('Enter regno: ')
    branch=input('Enter Branch: ')
    gpa=input('Enter Gpa: ')
    
    t=(f'{regno}',f'{name}',f'{branch}',f'{gpa}')
    lis.append(t)

for i in range(n):
    enter_details()
    
def search():    
    r=int(input('enter reg no to be searched for: '))
    for i in lis:
        if int(i[0])==r:
            print(i)

def filter_by_gpa():
    with open('endsem_prac.txt','a') as f:
        f.write('Regno Name Branch Gpa')
        f.write('\n')
    for i in lis:
        if float(i[3])>=7.5:
            with open('endsem.txt','a') as f:#change filename acc to your file
                for j in i:
                    f.write(j)
                    f.write(' ')
                f.write('\n')
def asc_sort():
        lis.sort(key=lambda x:int(x[0]))
        #or by bubble sort
        # new_ele = 0
        # lenl = len(lis)  
        # for k in range(0, lenl):  
        #     for l in range(0, lenl-k-1):  
        #         if (lis[l][new_ele] > lis[l + 1][new_ele]):  
        #             temp = lis[l]  
        #             lis[l]= lis[l + 1]  
        #             lis[l + 1]= temp  
        print(lis)                            
