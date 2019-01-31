list = [1,"five",7,"hello",10, 6, "towns", 90, "a stitch in time", "hello there", 9, "new year", 222, "conga, conga, conga"]
len_list = len(list)
print(len_list)
count = 0
total = 0
total_str = str(total)

for i in range(0, len_list):
	print(list[i])
	count +=1
	print("count: " + str(count))
	print("value of i: " + str(i) + "\n")
	total_str += str(list[i])
	print("In Process Total: grab and concatenate each value as a growing string total: " + total_str + "\n")

print(list[i] + "\n")
print("Final Total: completely grown conga line of elements in a list as one grown string:" + total_str)


	