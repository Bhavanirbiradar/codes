def count(s):
    vowels="aeiouAEIOU"
    vowel_count = consonent_count = 0
    for i in s:
        if i.isalpha():
            if i in vowels:
                vowel_count+=1
            else:
                consonent_count+=1
    return (vowel_count, consonent_count)
if __name__ == "__main__":
    s = input("enter a string")
    vowels, consonants = count(s)
    print(f"Vowels: {vowels}, Consonants: {consonants}")