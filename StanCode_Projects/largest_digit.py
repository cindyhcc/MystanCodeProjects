"""
File: largest_digit.py
Name: Cindy Huang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: number of digits given
	:return:
	"""
	if n < 0:
		n *= -1
	return find_largest_digit_helper(n, 0)


# 製造helper
def find_largest_digit_helper(n, current_n):
	if n == 0:
		return current_n
	else:
		temp = n % 10
		if temp > current_n:
			current_n = temp
		return find_largest_digit_helper(n//10, current_n)


if __name__ == '__main__':
	main()
