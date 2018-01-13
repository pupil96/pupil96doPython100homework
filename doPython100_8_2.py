# 9*9
# 9+9
# 22*22
# 32*32
# 9+9+9
# 9*9*9
# 19*19

def my_9x9table():
	print("==============9x9===============")
	for row in range(1, 10):
		for column in range(1, row+1):
			print("%s*%s=%s\t" % (row, column, row * column), end="")
		print("")
	print("--------------------------------")


def my_9plus9table():
	print("==============9+9===============")
	for row in range(1, 10):
		for column in range(1, row+1):
			print("%s+%s=%s\t" % (row, column, row + column), end="")
		print("")
	print("--------------------------------")


def my_22x22table():
	print("==============22x22===============")
	for row in range(1, 23):
		for column in range(1, row + 1):
			print("%s*%s=%s   \t" % (row, column, row * column), end="")
		print("")
	print("--------------------------------")


def my_32x32table():
	print("==============32x32===============")
	for row in range(1, 33):
		for column in range(1, row + 1):
			print("%s*%s=%s   \t" % (row, column, row * column), end="")
		print("")
	print("--------------------------------")


def my_9p9p9table():
	print("==============9p9p9===============")
	for xpos in range(1, 10):
		for ypos in range(1, 10):
			for zpos in range(1, 10):
				print("%s+%s+%s=%s   \t" % (xpos, ypos, zpos, xpos + ypos + zpos), end="")
			print("")
		print("")
	print("--------------------------------")


def my_9x9x9table():
	print("==============9x9x9===============")
	for xpos in range(1, 10):
		for ypos in range(1, 10):
			for zpos in range(1, 10):
				print("%s*%s*%s=%s \t" % (xpos, ypos, zpos, xpos * ypos * zpos), end="")
			print("")
		print("")
	print("--------------------------------")


def my_19x19table():
	print("==============19x19===============")
	for row in range(1, 20):
		for column in range(1, row + 1):
			print("%s*%s=%s   \t" % (row, column, row * column), end="")
		print("")
	print("--------------------------------")


if __name__ == "__main__":
	print("1-my_9x9table, 2-my_9plus9table, 3-my_22x22table, 4-my_32x32table, 5-my_9p9p9table, 6-my_9x9x9table, 7-All")
	myChioce = input("(1,2,3,4,5,6,7)?>")
	if myChioce == "7":
		my_9x9table()
		my_9plus9table()
		my_22x22table()
		my_32x32table()
		my_9p9p9table()
		my_9x9x9table()
		my_19x19table()
