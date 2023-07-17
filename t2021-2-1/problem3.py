def odd_sequence(n):
    odd_num = n / 2
    if n % 2 == 1:
        odd_num = (n + 1) / 2
    num_numbers = 2 * (odd_num - 1) + 1
    i = 0
    number_list = []
    while len(number_list) < num_numbers:
        i += 1
        if i % 2 == 1:
            number_list.append(i)
    print(number_list)