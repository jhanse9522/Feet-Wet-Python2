head_neck_pain = {"crown headache": ["sternocleidomastoid", "splenius capitus"], "frontal headache": ["sternocleidomastoid", "semispinalis capitus", "zygomaticus", "levator labii", "frontalis"], "temple headache": ["trapezius", "sternocleidomastoid", "temporalis", "splenius cervicus", "suboccipitals", "semispinalis capitus"]}

upper_extremity_pain = {"front of shoulder": ["infraspinatus", "anterior deltoid", "scalenes", "supraspinatus", "pectoralis major", "pectoralis minor", "biceps", "lattisimus dorsi", "coracobrachialis"], "side of shoulder": ["infraspinatus", "scalenes", "lateral deltoid", "supraspinatus"], "upper back": ["scalenes", "levator scapulae", "supraspinatus", "trapezius", "rhomboids", "lattisimus dorsi", "deep spinal muscles", "superficial spinal muscles", "serratus posterior superior", "infraspinatus", "serratus anterior"], "back of shoulder": ["scalenes", "levator scapulae", "posterior deltoid", "supraspinatus", "teres major", "teres minor", "subscapularis", "serratus posterior superior", "lattisimus dorsi", "triceps", "trapezius", "superficial spinal muscles"]}

print("\n")
print("Note: Keys in trigger point dictionaries represent pain locations; Values represent potential associated trigger point source areas to treat.\n")

print("Looping through keys in head_neck_pain trigger point dictionary now...\n")

for pair in enumerate(head_neck_pain):
	print(pair)
print("\n")


print("Looping through keys in upper_extremity_pain trigger point dictionary now...\n")

for pair in enumerate(upper_extremity_pain):
	print(pair)

print("_______________________________________________________________________________________________________")

#how would you craft a reference look up loop for a dictionary (meaning a sequence created for the express purpose of reaching into the value of the key value pair?)

print("Printing reference lookup by values method...\n")

for v in head_neck_pain.values():
	print(v)
print("\n")

print("_______________________________________________________________________________________________________")

print("Printing reference look up by dicty[key]...\n")

for key in head_neck_pain:
	print(head_neck_pain[key])
print("\n")

print("_______________________________________________________________________________________________________")
print("\n")

print("Printing reference lookup by items method which returns key/value pair...\n")

for k, v in head_neck_pain.items():
	print(k,v)

print("\n")

print("_______________________________________________________________________________________________________")
print("\n")


print("Here's my upper_extremity_pain dictionary for the head and neck. It's still a work in progress!\n")
print("\n")

for key, value in upper_extremity_pain.items():
	print("pain felt in the: ||", key, "|| can be coming from any of the following areas: \n",
		"*****", ",".join(value))
	print("\n")
print("\n")
print("_______________________________________________________________________________________________________")

print("\n")

just_keys = upper_extremity_pain.keys()

shoulder_only = []
count = 0

print("Checking dictionary for shoulder specific pattern keys now...\n")
print("\n")

for key in just_keys:
		if "shoulder" in key:
			shoulder_only.append(key)
			print("appending key to new list of subkeys...")
			print("added key is: ", key)
			count += 1
			print("total accepted key count is " + str(count) + "\n")

		else:
			print("rejected! this key does not contain the word shoulder!!\n\n")
print("Shoulder pain keys (and corresponding tp patterns) related to the head and neck found in this list include the following:\n")
print(shoulder_only, "there are a total of:", count, "keys\n")
print("__________________________________________________________________________________________________________")

for key in shoulder_only:  #now that we filtered for the data we want in the original dict (the "shoulder_only" keys), what we are after now are the values tied to the filtered data and we do it through a reference look up (in directly (the way range(len(word)) works, etc...
	print(key, "correlates with the following possible soft tissue culprits where trigger points may be located:")
	print("\t|||", ", ".join(upper_extremity_pain[key])) 
	print("\n") # note on this line, this is a reference look up being used to access another data container. key from shoulder_only list is being used to access and then used to look up the value in the upper_extremity_pain dictionary. We don't need to know what those values are. That's the point. Doing stuff with stuff we don't know about by using stuff we do.




