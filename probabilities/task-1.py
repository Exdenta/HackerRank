
input_str = "YTATBTATZ"

print(len(input_str))
unique_str = ''.join(set(input_str))
print(len(unique_str))

if len(input_str) == 1:
    print(input_str)
    print(1)
elif len(input_str) == 2:
    

exit(0)

letter_n = 97
n = 6
string = ""

T1 = string + chr(letter_n) + string
T2 = string + chr(letter_n + 1) + string
T3 = string + chr(letter_n + 2) + string

total_length = 0
for i in range(0, n):
    # total_length = total_length * 2 + 1
    string = string + chr(letter_n) + string
    letter_n = letter_n + 1

# string = ""
# for i in range(0, 26):
#     string = string + chr(97 + i)
# print(string)
# # print(ord('y')-97)
