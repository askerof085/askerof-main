def distance(word1, word2):
  if len(word1) != len(word2):
   return -1
  else:
   distance = 0
  for i in range(len(word1)):
   distance += abs(ord(word1[i]) - ord(word2[i]))
  return distance
print(distance('a', 'p'))