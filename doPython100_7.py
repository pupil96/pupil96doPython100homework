# 打印特殊的字符图案，排成x字


def my_print_x1():
	a = 176
	b = 219
	print(chr(b), chr(a), chr(a), chr(a), chr(b))
	print(chr(a), chr(b), chr(a), chr(b), chr(a))
	print(chr(a), chr(a), chr(b), chr(a), chr(a))
	print(chr(a), chr(b), chr(a), chr(b), chr(a))
	print(chr(b), chr(a), chr(a), chr(a), chr(b))


def my_print_x2(ivar_xy=8):
	a = 176
	b = 219
	row = ivar_xy
	column = ivar_xy
	for i in range(row):
		for j in range(column):
			if i == j:
				print(chr(b), end=" ")
			elif (i+j) == (ivar_xy - 1):
				print(chr(b), end=" ")
			else:
				print(chr(a), end=" ")
		print()


if __name__ == "__main__":
	my_print_x1()
	my_print_x2()
	my_print_x2(15)
