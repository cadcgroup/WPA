def weightByT_i(T_i_21):
    T_i_32 = []
    weight_mi = []
    weight_xian = []
    D_List = []
    for i in range(10):
        T_i_32.append(T_i_21[i])
    for i in range(10,21):
        T_i_32.append(T_i_21[i])
        T_i_32.append(T_i_21[i])
    for i in range(32):
        temp = (T_i_32[i] - 1)*100
        D_List.append(temp)
    D_min = min(D_List)
    D_max = max(D_List) - D_min
    for i in range(32):
        D_List[i] -= D_min
        weight_mi.append(1/(D_List[i]+1))
        weight_xian.append(1-D_List[i]/D_max)
    weight_mi = np.array(weight_mi)
    weight_xian = np.array(weight_xian)
    return weight_mi, weight_xian

def weightByTi(Ti):
    Ti = np.array(Ti)
    Ti_Seq = np.zeros(21)
    Ti_sorted = np.flip(np.sort(Ti))
    weight = []
    for i in range(21):
        index_Ti = Ti.tolist().index(Ti_sorted[i])
        temp = 21/20 - (i+1)/20
        Ti_Seq[index_Ti] = temp if temp>0 else 0
    for i in range(10):
        weight.append(Ti_Seq[i])
    for i in range(10,21):
        weight.append(Ti_Seq[i])
        weight.append(Ti_Seq[i])
    weight = np.array(weight)
    return weight