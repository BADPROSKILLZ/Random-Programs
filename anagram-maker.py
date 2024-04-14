def makeAnagrams(start: str, end: str, anagrams: list[str]) -> None:
    if(len(end) == 0):
        anagrams.append(start + end)
    else:
        for i in range(len(end)):
            newStart = start + end[i]
            newEnd = end[:i] + end[i+1:]
            makeAnagrams(newStart, newEnd, anagrams)

anagrams = []
start = ""
end = input("Enter a word: ")
makeAnagrams(start, end, anagrams)

# Removing duplicates
unique_anagrams = []
for word in anagrams:
    if word not in unique_anagrams:
        unique_anagrams.append(word)
anagrams = unique_anagrams
print(anagrams)