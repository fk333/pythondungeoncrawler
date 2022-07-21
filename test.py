str1 = "the cat sat on the mat. My cat is called frank. cats are cute!"
wh = str1.replace("cat", "dog").upper().index("dog")
print(wh)