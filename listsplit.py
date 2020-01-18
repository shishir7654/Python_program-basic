def Split(mix):
    even_list =[]
    odd_list =[]
    for i in mix:
        if (i%2==0):
            even_list.append(i)
        else:
            odd_list.append(i)
    print("Even_lists:",even_list)
    print("odd_lists:",odd_list)

mix = [2,3,4,5,6,7,8,9,44,55,66]
Split(mix)
