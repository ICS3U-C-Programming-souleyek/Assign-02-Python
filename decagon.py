import math


def main():
    # Get side length from
    side = float(input("Enter the side length(mm): "))
    # calculate area and perimeter
    area = 5 / 2 * side**2 * math.sqrt(math.sqrt(5) * 2 + 5)
    perimeter = 10 * side

    # shows area and perimeter
    print("")
    print("Area = {} mm^2".format(area))
    print("Perimeter = {} mm".format(perimeter))


if __name__ == "__main__":
    main()
