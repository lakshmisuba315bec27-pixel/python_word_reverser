sentence = "aaabbbcccddeeeffggg"
compressed = ""
count = 1
for i in range(len(sentence) - 1):
    if sentence[i] == sentence[i + 1]:
        count += 1
    else:
        compressed += sentence[i] + str(count)
        count = 1
compressed += sentence[-1] + str(count)
print(compressed)  
