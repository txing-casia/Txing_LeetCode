try:

    A_origin= 'a,,1,"b,"""'
    num_list=A_origin.split(',')
    num=len(num_list)
    for i in range(len(num_list)):
        if "" == num_list[i]:
            num-=1

    A=A_origin
    flag_yh=0

    if ',' in A_origin and '"' in A_origin:
        for i in range(len(A_origin)):
            if A[i+flag_yh] == '"':
                A=A[0:i+flag_yh]+'"'+A[i+flag_yh:]
                flag_yh+=1
        A = '"' + A + '"'



        # print(A)

        print(num)
        for temp in num_list:
            if temp == "":
                print("--")
            else:
                print(temp)

    print(A)
except:
    pass



