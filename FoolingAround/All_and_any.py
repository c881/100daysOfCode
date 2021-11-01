def valid_rgb(rgb):
	"""Recive Rgb tupple.
	Check if all values are int between 0 and 255.
	:return bool"""
	return all(int(val) == val and 0 <= val <= 255 for val in rgb)

# print(valid_rgb((25, 5, 255)))
# print(valid_rgb((250, 255, 257)))
# print(valid_rgb((25, 5.3, 255)))

"""any() return True if any of the iterables are True"""

# https://www.linkedin.com/learning/8-things-you-must-know-in-python/solution-any-and-all?autoAdvance=true&autoSkip=false&autoplay=true&resume=false

import string

def contains_panctuation(input_str):
	"""Return True if input_str contains panctuation.
		False if not."""
	return any(char in string.punctuation for char in input_str)

print(contains_panctuation('Little rabit'))
print(contains_panctuation('Little rabit.'))