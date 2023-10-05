def remove_duplicates():
    numbers = [17, 13, 5, 10, 37, 11, 13, 17, 12, 5, 13]
    numbers2 = []
    for number in numbers:
        if number not in numbers2:
            numbers2 = numbers2.append(number)

        print(numbers2)


remove_duplicates()
