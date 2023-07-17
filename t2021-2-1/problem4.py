def multiples_dict(num_list):
    base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res_dict = dict()
    for b in base:
        for n in num_list:
            if n % b == 0:
                if b in res_dict:
                    res_dict[b] = res_dict[b] + 1
                else:
                    res_dict[b] = 1
    print(res_dict)

