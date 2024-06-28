def main():

    total = 0
    x = 0
    for x in range(0,5):
        num1 = int(input('Enter next value: '))
        total += num1
    print(total)


    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
