import pandas as pd

def segregate(df):
    b_list = []
    ctl_list = []
    htl_list = []
    
    for type, epitope in zip(df['Cell Type'],df['Epitope']):
        x = type.split('.')
        if x[0] == 'bCell':
            b_list.append(epitope)  
        elif x[0] == 'TC(B58)':
            ctl_list.append(epitope)
        elif x[0] == 'TC(A1)':
            ctl_list.append(epitope)
        elif x[0] == 'TH(IFN)':
            htl_list.append(epitope)
    
    # data = pd.DataFrame({
    #     'B': b_list,
    #     'CTL': ctl_list,
    #     'HTL': htl_list
    # })
    
    return b_list, ctl_list, htl_list
