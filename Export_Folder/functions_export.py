def multiple_values(sold, returns):
    return sold, returns

def recursive_func(n):
    print(n)
    if n == 1:
        print("only one is left in this recursive function")
        return
    return recursive_func(n - 1)

chai_types = ['light', 'kadak', 'strong', 'kadak', 'sweet', 'kadak']
only_kadak = list(filter(lambda chai: chai == 'kadak', chai_types))

'''def built_in_funct(somevalue="some value"):
    """Built-in functions documentation link."""
    return somevalue, "something"
'''

# Move any code you want to run only when testing THIS file here:
'''if __name__ == "__main__":
    sold, remainig = multiple_values(100, 30)
    print(f"Sold : {sold}")
    print(f"Remaining : {remainig}")

    recursive_func(4)
    print(built_in_funct.__doc__)'''