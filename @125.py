# Palindrome or not

s = "mad am"

NewS = ""

for ch in s:
    if ch.isalnum():
        NewS += ch.lower()

i = 0
j = len(NewS) - 1

while i < j:

    if NewS[i] != NewS[j]:
        print(False)
        break

    i += 1
    j -= 1
else:
    print(True)
