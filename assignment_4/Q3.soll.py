# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
def squares_of_list():
    given_list = map(int, input("Enter the list followed by space: ").split(" "))
    result = list(map(lambda i : i ** 2,given_list))
    print(result)
if __name__ == "__main__":
    squares_of_list()