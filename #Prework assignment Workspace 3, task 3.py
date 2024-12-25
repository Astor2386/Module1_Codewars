#Prework assignment Workspace 3, task 3
def multiply_numbers(a, b):
        """This function multiplies two numbers and returns the result. 
        Parameters: a (int or float): 
        The first number to be multiplied. b (int or float): 
        The second number to be multiplied.
        Returns: int or float: The product of 'a' and 'b'."""
        
        return a * b 
    # Example usage for multiply_numbers
result_product = multiply_numbers(3, 2) 
print("Product of 3 and 2 is: " + 
str(result_product))

def sum_list(numbers):
        """This function sums all numbers in the given list and returns the total.
        Parameters:
        numbers (list): A list containing numbers (int or float) to be summed.
        Returns:
        int or float: The sum of all numbers in the list."""

        total = 0 
        for number in numbers: 
                total += number
        return total
# # Example usage for sum_list
list_numbers = [3, 4, 6, 2]
result_sum = sum_list(list_numbers) 
print("Sum of the list [3, 4, 6, 2] is: " + 
str(result_sum))