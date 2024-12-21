from colorama import Fore, Style, init
import pandas as pd
import itertools
import numpy as np
from .protparam import *

init()  # Initialize colorama
list=[]
ans=''
result=[]

ind = {"W":0,"C":1,"M":2,"H":3,"Y":4,"F":5,"Q":5,"N":7,"I":8,"R":9,"D":10,"P":11,"T":12,"K":13,"E":14,"V":15,"S":16,"G":17,"A":18,"L":19}

matrix = np.array([
    [1.0, 24.68, 1.0, -1.88, -9.37, 1.0, 1.0, -9.37, 1.0, 58.28, 1.0, -1.88, -14.03, 1.0, -14.03, 1.0, 1.0, 13.34, 1.0, 24.68],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -6.54, -1.88, 1.0, 1.0, 1.0, -6.54, 1.0, 1.0, 44.94, 1.0, 33.6, 1.0, 44.94, 1.0],
    [24.68, 33.6, -1.88, 1.0, 44.94, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -6.54, 1.0, 33.6, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [24.68, 33.6, 58.28, 1.0, 13.34, 1.0, 1.0, 1.0, 13.34, 20.26, 1.0, 1.0, 1.0, 1.0, -6.54, 1.0, 1.0, 1.0, -7.49, 1.0],
    [1.0, 1.0, 24.68, 44.94, 13.34, 33.6, -6.54, 1.0, 1.0, -6.54, 1.0, 1.0, 1.0, 1.0, 1.0, -6.54, 1.0, -7.49, 1.0, 1.0],
    [1.0, 1.0, 1.0, -9.37, 1.0, 1.0, -6.54, -14.03, 1.0, 1.0, -6.54, 20.26, 13.34, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, -6.54, -6.54, 1.0, 1.0, 1.0, 20.26, -6.54, 1.0, 20.26, 1.0, 20.26, -6.54, 24.68, 20.26, 1.0, 20.26, 1.0, 1.0, 33.6],
    [13.34, 1.0, 1.0, 24.68, 1.0, 1.0, 1.0, 1.0, 1.0, 13.34, 1.0, 1.0, -14.03, 1.0, 1.0, 1.0, 1.0, -7.49, 1.0, 1.0],
    [1.0, 1.0, 1.0, 44.94, 1.0, 1.0, 1.0, 44.94, 1.0, 1.0, 1.0, 1.0, 1.0, -7.49, 20.26, 1.0, 1.0, -7.49, 1.0, 1.0],
    [1.0, 1.0, -6.54, 1.0, -15.91, 1.0, 1.0, 1.0, 1.0, 58.28, -6.54, -6.54, 1.0, 33.6, 1.0, 1.0, -20.26, 1.0, 1.0, 20.26],
    [1.0, 20.26, 1.0, 1.0, 24.68, 13.34, 20.26, 1.0, 1.0, 1.0, 1.0, -6.54, 1.0, 1.0, 20.26, 14.03, 1.0, 1.0, -7.49, 1.0],
    [1.0, 20.26, 44.94, -1.88, 13.34, 20.26, 20.26, -1.88, -1.88, 20.26, 1.0, 20.26, 1.0, -6.54, 20.26, 20.26, 44.94, 1.0, 20.26, 20.26],
    [-14.03, 33.6, -1.88, -6.54, -7.49, 1.0, 1.0, -7.49, 1.0, 1.0, -14.03, 1.0, 1.0, 1.0, 1.0, -7.49, 1.0, -7.49, 1.0, 1.0],
    [1.0, 1.0, 1.0, 24.68, 1.0, -14.03, 1.0, 24.68, -7.49, 1.0, -7.49, 1.0, 1.0, 1.0, 1.0, -1.88, 1.0, -7.49, 1.0, -7.49],
    [1.0, 1.0, 1.0, 1.0, -6.54, 1.0, 20.26, 1.0, 44.94, 1.0, 1.0, 18.38, 20.26, 1.0, 33.6, 1.0, 20.26, -6.54, 1.0, 1.0],
    [-7.49, -6.54, 1.0, 1.0, 1.0, 1.0, -6.54, 1.0, -7.49, 1.0, 1.0, 20.26, 1.0, -7.49, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 44.94, 1.0, 1.0, 1.0, 44.94, 1.0, 1.0, 44.94, 20.26, 20.26, 1.0, 1.0, 20.26, 1.0, 20.26, 1.0, 1.0, 1.0],
    [-9.37, 1.0, 1.0, -9.37, -7.49, 1.0, 1.0, -14.03, 1.0, -7.49, 1.0, 1.0, -7.49, -7.49, 1.0, -7.49, 1.0, 13.34, 1.0, 1.0],
    [-14.03, 1.0, 13.34, 1.0, 24.68, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 20.26, 1.0, 1.0, 1.0, 1.0, 1.0, -7.49, 1.0, 1.0],
    [13.34, 20.26, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 20.26, 1.0, 1.0, 1.0, 1.0, -7.49, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]])

# |----Prot param algo---------|
# def score(epitopes):
#     list=pd.DataFrame(columns=['sequence','score'])
#     # print(epitopes)
#     for j,seq in enumerate(epitopes):
#         val=0
#         for i in range(len(seq)-1):
#             # print(ind[seq[i+1]],ind[seq[i]])
#             val += matrix[ind[seq[i+1]],ind[seq[i]]]
#         val = val*(10/len(seq))
#         list.loc[j]=[seq,val]
#     list=list.sort_values(by='score')
#     return list

# def cal():
#     list=[]
#     # assumption: epitopes size should be > 1
#     epitopes=["DEPPPPKSSRVTASAPSP","ISDDSDDEPPPPKSSRVT","DSDDKEEEGEEEEEEEEK","MTDPLAGAM","ITKCVPHCY","ASDPATSSV","AAAAMQILVSKELDG","AAGTWKTERVITSPQ","AGSLQYDADSGDSGR"]
#     index=0
#     def solve(ans,index):
#         if(index==len(epitopes)-1):
#             list.append(ans)
#             return
#         linkers = ['GSGS',"GTGS",'EAAAK', "AAY", "GPGPG"]
#         # linkers = ["GTGS", "GPGPG"]
#         epitope=epitopes[index]
#         for linker in linkers:
#             val=0
#             if len(ans)==0:
#                 val = matrix[ind[epitope[index]],ind[linker[-1]]]
#                 if(val<2):
#                     solve(ans+linker+epitope,index+1)
#             else:
#                 val = matrix[ind[epitope[index]],ind[linker[-1]]]+matrix[ind[linker[0]],ind[ans[-1]]]
#                 if(val<3):
#                     solve(ans+linker+epitope,index+1)
#     ans=""
#     solve(ans,0)
#     print(len(list))
# cal()
                    
# |---------------Permutation of Linkers--------------|


def link(epitopes,preferred_linkers,num):
    result=[]
    n=len(epitopes)
    ans=""   
    
    def combination(i,ans):
        if i>n:
            result.append(ans)
            return
        for j in range(num):
            if i==1:
                combination(i+1,ans+epitopes[i][0]+preferred_linkers[i][j][0]+epitopes[i][1])
            else:
                combination(i+1,ans+preferred_linkers[i][j][0]+epitopes[i][1])
        return
    combination(1,ans)
    return result

 
# # |-------------------Permutation of Epitopes----------------|
# def combination(arr,linker,vis,cnt,n):
#     global list,ans
#     if(n==cnt):
#         list.append(ans)
#         return
#     for i in range(n):
#         if(vis[i]==1):
#             continue
#         x = len(linker+arr[i])
#         # print(f"{Fore.RED}{linker}{Style.RESET_ALL}{Fore.BLUE}{arr[i]}{Style.RESET_ALL}")
#         ans+=linker+arr[i]
#         vis[i]=1
#         cnt+=1
#         combination(arr,linker,vis,cnt,n)
#         ans=ans[:-x]
#         vis[i]=0
#         cnt-=1
#     return

# def link(df,b_linker,ctl_linker,htl_linker):
#     b_cell_epitopes=df.B.values
#     ctl_epitopes=df.CTL.values
#     htl_epitopes=df.HTL.values
#     global list,ans,result
#     n_b, n_c, n_h =3,3,3
#     ans=''
#     list=[]
#     cnt=0
#     vis=[0]*3
#     combination(b_cell_epitopes,b_linker,vis,cnt,n_b)
#     list1=list
#     list=[]
#     ans=''
#     cnt=0
#     vis=[0]*3
#     combination(htl_epitopes,htl_linker,vis,cnt,n_h)
#     list2=list
#     list=[]
#     ans=''
#     cnt=0
#     vis=[0]*3
#     combination(ctl_epitopes,ctl_linker,vis,cnt,n_c)
#     list3=list
#     # Perform the cross join and concatenate the strings
#     result = [''.join(combination) for combination in itertools.product(list1, list2, list3)]
#     # Print the result
#     return result



# |-------Manual Testing------|
# df = pd.read_csv('epitopes.csv')
# b_cell_epitopes=df.B.values
# ctl_epitopes=df.CTL.values
# htl_epitopes=df.HTL.values

# b_score = score(b_cell_epitopes)
# c_score = score(ctl_epitopes)
# h_score = score(htl_epitopes)
# b=b_score['sequence']
# h=h_score['sequence']
# c=c_score['sequence']
# # print(b,c,h)
# result = link(b,h,c)

# for i, seq in enumerate(result):
#             # print(seq,fetch_instability(seq))
#             # print(seq)
#             x = fetch_instability(seq)
#             # print(x,seq)


# epitopes=["DEPPPPKSSRVTASAPSP","MTDPLAGAM","AAAAMQILVSKELDG","ISDDSDDEPPPPKSSRVT","ITKCVPHCY","AAGTWKTERVITSPQ","DSDDKEEEGEEEEEEEEK","ASDPATSSV","AGSLQYDADSGDSGR","IYSESPFYRPVLLLRDVQ",
#           "STDGSALPA","ANAAIFETLLTPEDC",'GSGS','EAAAK', "AAY", "GPGPG"]
# # print(type(matrix))
