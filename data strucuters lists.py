def only_even_num():
    input_list = (input("your number list here: ")).split()
    input_list = [int(num) for num in input_list if int(num) % 2 == 0]
    input_list.sort()
    print(input_list)
only_even_num()