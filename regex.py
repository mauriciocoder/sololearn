import re

## match tries to find occurrence in the beginning of string
pattern = r'pamspam'
text = 'spamspamspam'
if re.match(pattern, text):
    print('Matched!!!')
else:
    print('Does not match!!!')

'''
The function re.search finds a match of a pattern anywhere in the string.
The function re.findall returns a list of all substrings that match a pattern.
'''
match = re.search(pattern, text)
if match:
    print(f'Search for {pattern} in {text} brings results!!!')
    print(match.group())  # search result
    print(match.start())  # occurence's start index
    print(match.end())  # occurence's end index
    print(match.span())  # tuple os occurence's index

else:
    print('Search does not bring result!!!')

pattern = r'sp'
print(re.findall(pattern, text))

# You can also perform a substitution
result = re.sub('spam', 'success', 'spamspamspam', 1)  # change 'spam' to 'success' on string 'spamspamspam' just one time
print(result)


## Metacharacters
'''
The first metacharacter we will look at is . (dot). 
This matches any character, other than a new line.
'''
pattern = r'gr.y'
if re.match(pattern, 'gray'):
    print('Matches gray')
if re.match(pattern, 'grey'):
    print('Matches grey')
if re.match(pattern, 'blue'):
    print('Matches blue')

print('#############################')

'''
The next two metacharacters are ^ and $.
These match the start and end of a string, respectively.
'''
pattern = '^gr.y$'
if re.match(pattern, 'gray'):
    print('Matched gray')
if re.match(pattern, 'grey'):
    print('Matched grey')
if re.match(pattern, 'stingray'):
    print('Matched stingray')

print('#############################')

## Character Classes
'''
Character classes provide a way to match only one of a specific set of characters.
A character class is created by putting the characters it matches inside square brackets.
'''

pattern = r'[aeiou]'
if re.search(pattern, 'Tio Mau'):
    print(re.findall(pattern, 'Tio Mau'))
if re.search(pattern, 'rythm'):
    print('Matched Rythm!')

'''
The class [a-z] matches any lowercase alphabetic character.
The class [G-P] matches any uppercase character from G to P.
The class [0-9] matches any digit. 
Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.
'''

pattern = r'[0-9]'
if re.search(pattern, 'daskjdha20sajlkd'):
    print(re.findall(pattern, 'daskjdha20sajlkd'))

'''
Place a ^ at the start of a character class to invert it. 
This causes it to match any character other than the ones included. 
Other metacharacters such as $ and ., have no meaning within character classes. 
The metacharacter ^ has no meaning unless it is the first character in a class.
'''

pattern = r'[^A-Z]'
if re.search(pattern, 'ASDSGSDFEFSAS'):
    print('Matches!')
else:
    print('Does not match!!!')

'''
The metacharacter * means "zero or more repetitions of the previous thing". 
It tries to match as many repetitions as possible. 
The "previous thing" can be a single character, a class, or a group of characters in parentheses.
'''
pattern = r'(spam)*'
print(re.search(pattern, 'spamspamadabaspam'))

'''
The metacharacter + means "one or more repetitions"
'''
pattern = r'(spam)+'
print(re.search(pattern, 'spamspamadabaspam'))

'''
The metacharacter ? means "zero or one repetition"
'''
pattern = r'adaba(spam)?'
print(re.search(pattern, 'adabaspamspamadabaspam'))

'''
The regex {x,y} means "between x and y repetitions of something". 
Hence {0,1} is the same thing as ?.
'''
pattern = r'x(spam){2, 3}x'
text = 'xspamx'
print(re.findall(pattern, text))
text = 'xspamspamx'
print(re.findall(pattern, text))
