

def start_tests():
    print("-----List tests-----")

    nums = [1, 2, 3, 4, 5, 6]

    ################################
    # read from the list
    ################################
    print(nums[0])
    print(nums[1])

    ###############################
    # add elements to the list
    ###############################
    nums.append(9)
    print(nums)

    ###############################
    # for loop
    ###############################
    for index in nums:
        print(index)

    ###############################
    # for loop from 0 to 20
    ###############################
    for index in range(0, 21):
        print(index)


def test1():
    print("Test 1")
    prices = [123, 3, 23, 6475, 58, 89, 45, 34, 87,
              34, -12, 23, 123, -23, -123, 0, 123, 0, -29, 10]

    ################################
    # print the number that are lower than 50
    # count how many prices are lower than 50
    ################################
    lower_50 = 0
    for index in prices:
        if index < 50:
            print(index)
            lower_50 = lower_50 + 1
    print(f"The number of elements lower than 50: {lower_50}")

    ################################################################
    # the sum of all the prices
    # the sum of all prices greater than zero
    # the number of prices with zero value (it should not exist)
    ################################################################

    sum_all = 0
    sum_greater_zero = 0
    number_of_zeros = 0
    ################################################################
    # sum of all
    ################################################################
    for index in prices:
        sum_all = sum_all + index
    print(f"The sum of all is {sum_all}")

    ################################################################
    # number greater than zero
    ################################################################
    if index > 0:
        sum_greater_zero = sum_greater_zero + 1
        print(f"The number greater than zero is {sum_greater_zero}")

        ################################################################
        # number of zeros
        ################################################################
    if index == 0:
        number_of_zeros = number_of_zeros + 1
        print(f"The number of zeros is {number_of_zeros}")


def test2():
    print("------------Test 2------------")

    users = [
        {
            "gender": "F",
            "name": "Louis",
            "color": "Green"
        },
        {
            "gender": "M",
            "name": "Manuel",
            "color": "Gray"
        },
        {
            "gender": "F",
            "name": "Rossy",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Renny",
            "color": "pink"
        },
        {
            "gender": "M",
            "name": "Roman",
            "color": "Purple"
        },
        {
            "gender": "m",
            "name": "John",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Susan",
            "color": "Black"
        }
    ]

    ################################################
    # get the name of the user (from the dictionary)
    # how many users in list
    # print the name of the users who likes pink or
    #   Pink or PINK
    ################################################
    print(len(users))
    for user in users:
        print(user["name"])

        if user["color"].lower() == "pink":
            print(user["name"])

    print(" Users how like pink")
    for user in users:
        if user["color"].lower() == "pink":
            print(user["name"])


def test3():
    print("------------Test 3----------")
    prices = [123, 3, 23, 6475, 58, 89, 45, 34, 87,
              34, -12, 23, 123, -23, -123, 0, 123, 0, -29, 10]

########################################################################
# Find the most expensive product price
# solution = prices[0]
# for loop in prices
# if price is greater than your solution
# your solution is equal to your price
#
# outside the loop, print the result
########################################################################
    most_expensive = prices[0]

    for num in prices:
        if (most_expensive is None or num > most_expensive):
            most_expensive = num

    print('Maximum value:', most_expensive)


start_tests()
test1()
test2()
test3()
