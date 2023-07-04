def count_vowels(s):

    vowel_list = ['a','e','i','o','u']

    cnt = 0

    for char in s:

        if char in vowel_list:

            cnt += 1
    
    return cnt



print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3
