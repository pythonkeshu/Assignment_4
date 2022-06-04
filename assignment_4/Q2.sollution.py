#Q2 sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
#  output =[3, 6, 9, 12, 15, 18, 21]


def sum_of_list():
    given_list = map(int, input("Enter the list followed by space: ").split(" "))
    
    result = list(map(lambda i : i * 3 , given_list ))
    print(result)
if __name__ == "__main__":
    sum_of_list()
