'''
Given a signed 32-bit integer integer, return integer with its digits reversed. If reversing integer causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Eintegerample 1:

Input: integer = 123
Output: 321
Eintegerample 2:

Input: integer = -123
Output: -321
Eintegerample 3:

Input: integer = 120
Output: 21
 

Constraints:

-231 <= integer <= 231 - 1
'''

# Answer = 0
# Get mod 10,100,1000 until the factor is less than integer
# Multiply the result with the same factor and add to soln

integer= 1534236469

if integer < (-2**31) or integer > (2**31 - 1):
    print('return zero')

negative_number = False
if integer < 0:
    negative_number = True
    integer = abs(integer)
divisor = 10
reversed_int = 0
while integer != 0:
    last_digit = integer % divisor # last_digit = 3, 2, 1
    integer = integer // divisor # integer = 123/10 = 12, 1, 0
    reversed_int = (reversed_int * divisor) + last_digit # reversed_int = (0 * 10) + 3 = 3, 32, 321

if negative_number:
    reversed_int = -abs(reversed_int)

print(reversed_int)