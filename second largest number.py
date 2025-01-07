def second_largest_number():
    input_list = (input("your number list here: ")).split()
    input_list = [int(num) for num in input_list]
    input_list.sort()
    print(input_list[-2])