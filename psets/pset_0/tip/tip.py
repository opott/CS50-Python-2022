def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # remove the $ sign and convert to float
    d = d.removeprefix("$")
    d = float(d)
    return d


def percent_to_float(p):
    # remove the % sign and convert to float
    p = p.removesuffix("%")
    p = float(p)
    p = p / 100
    return p


main()