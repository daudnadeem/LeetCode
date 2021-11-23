# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

roman_map ={
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

"MCMXCIV"

def roman_to_int(r_num):
    summ = 0
    for s in range(len(r_num)-1,-1,-1):
        num = roman_map[r_num[s]]
        if 3*num < summ:
            summ = summ-num
        else:
            summ = summ + num
        print(summ)
    return summ
    


# print(roman_to_int("MCMXCIV"))

def romanToInt(s):
    # N == Length of S 
    # N == 7
	N = len(s)
    # Iterations are now 6?
	i = N-1
    # Output is where we append the final result
	output = 0
	while i>=0:
		x = i+1
		print(f'conditional: {i} < {x}')
		if i < N-1 and roman_map[s[i]] < roman_map[s[i+1]]:
			output -= roman_map[s[i]]
		else:
			print(f'I CAME HERE in ITERATION: {i}')
			output += roman_map[s[i]]
		print(f'iteration: {i}, roman_num: {s} summ == {output}')
		i -= 1
	return output

# print(romanToInt("MCMXCIV"))
# print(roman_to_int(1))
# print(roman_to_int(1000))

# THIS ONES MINE!
def roman_to_INT(rome="MCMXCIV"):
    rslt = 0
    N = len(rome)
    rome = rome[::-1]
    for i in range(len(rome)):
        if i < N-1 and roman_map[rome[i]] < roman_map[rome[i+1]]:
            rslt -= roman_map[rome[i]]
        else:
            rslt += roman_map[rome[i]]
    print(rslt)
    return rslt

        # print(roman_map[ech])

roman_to_INT("III")