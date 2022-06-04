# Q1.Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# sample input: 10
# sample output: 35


def add():
    given_number = int(input("Enter the number : "))
    result = lambda given_number:given_number + 25
    print("output after adding 25 to the given number is : ",end = " ")
    print(result(given_number))
    

        
if __name__ == "__main__":
    add()


   
