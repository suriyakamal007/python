n=str(input())
if n=='a' or n=='e' or n=='i' or n=='o' or n=='u' or n=='A' or n=='E' or n=='I' or n=='O' or n=='U':
  print("Alphabet")
elif n.isalpha():
  print("Consonant")
else:
    print("invalid")
