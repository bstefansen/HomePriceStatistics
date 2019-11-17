# Filename: Stefansen_Homes.py
# Description: Program calculates statistics for an inputted data set
# Author: Blake Stefansen


# Defines functions
def prompt(cost):
    one_cost = 0
    while one_cost != -99:
        one_cost = float(input("Enter cost of one home or -99 to quit: "))
        cost.append(one_cost)
    cost.pop(-1)

def median(cost):
    middle = float(len(cost)) / 2
    middle2 = float(((len(cost)) / 2) - 1)
    if middle % 2 != 0:
        return round(cost[int(middle)], 1)
    else:
        median = round((((cost[int(middle)]) + (cost[int(middle2)])) / 2), 1)
        return median

def mean(cost):
    total = sum(cost)
    listtotal = len(cost)
    avg = total / listtotal
    avg = round(avg, 1)
    return avg

def ouput(cost):
    # Defines variables
    medianprice = str(median(cost))
    meanprice = str(mean(cost))
    minprice = str(min(cost))
    maxprice = str(max(cost))

    # Prints output
    print("*" * 35)
    print("Prices of homes in your area: ")
    print(str(cost))
    print("*" * 35)
    print("The median value is $ " + medianprice)
    print("The average sale price is $ " + meanprice)
    print("The minimum sale price is $ " + minprice)
    print("The maximum sale price is $ " + maxprice)
    print("*" * 35)
    print("Thank you for using this program")

def main():
    # Prompts the user
    cost = []
    prompt(cost)

    # Sorts the prices
    cost = sorted(cost)

    # Calls functions
    median(cost)
    mean(cost)
    ouput(cost)

# if started as the main module, call the main function
if __name__ == "__main__":
    main()