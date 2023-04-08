import csv

"""




"""


def read_money():
    try:
        with open("money.txt", "r") as f:
            money = f.readlines()[-1].rstrip().strip('\n').split(':')[-1].lstrip().rstrip()
            return money
    except FileNotFoundError:
        print("Money file not found.")
    except IOError:
        print("Error Reading File")


def write_money(value, _type="money"):
    """
    :param value: value of money or bet
    :param _type: either "money" or "bet", default: "money"
    :return:
    """
    try:
        with open("money.txt", "a") as f:
            f.writelines([f"\n{_type}: {value}"])
    except IOError:
        print("Error writing to money file.")
    except FileNotFoundError:
        print("Money file not found.")

if __name__ == "__main__":
    read_money()
