#!/Volumes/numerous/usr/local/homebrew/bin//python3

def sum_of_evens(nums):
	# There are smarter ways of doing this but I
	# want to practice the fundamentals of python syntax
	
	acc = 0;
	for i in nums:
		if i % 2 == 0:
# 			print(i)
			acc += i

	print(acc)

sum_of_evens([1,2,3,4,5,6,7])
