class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2

    def power(self, base, exponent):
        return base ** exponent

    def sqrt(self, num):
        if num < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return num ** 0.5

    def abs_value(self, num):
        return abs(num)

# Example usage:
calculator = Calculator()
result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(8, 2)
result_multiply = calculator.multiply(4, 6)
result_divide = calculator.divide(10, 2)
result_power = calculator.power(2, 3)
result_sqrt = calculator.sqrt(9)
result_abs_value = calculator.abs_value(-7)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
print("Exponentiation:", result_power)
print("Square Root:", result_sqrt)
print("Absolute Value:", result_abs_value)
