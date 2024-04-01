#Kirtia Spence
#kirtia.spence59@myhunter.cuny.edu
#This program prints counting plurals

nouns = input("Enter nouns: ").split()
num_words = len(nouns)
plural_count = sum(1 for word in nouns if word.endswith('s'))

fraction_plural = plural_count/num_words if num_words else 0

print(f"Number of words:{num_words}\nFraction of plural nouns: {fraction_plural:2f}")
      
