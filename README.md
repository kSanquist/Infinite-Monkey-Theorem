# Infinite-Monkey-Theorem

### What is the Infinite Monkey Theorem?
A theorem that if you had an infinite amount of monkeys and an infinite amount type writers typing letters at random, given an infinite amount of time, 
the monkeys would type the entire work of Hamlet.

### What does my program do?
Given an inputted word/phrase, the program generates chunks of a specified size consisting of randomly generated letters. It then checks if the 
word/phrase is contained within the chunk. When it detects the word/phrase it notes the time it took to find it and how many characters were produced
before the word/phrase was found.

### Probablity of word/phrase appearking
Assuming you are only considering letter characters, there is a 1/26 chance that the right letter will be generated and a 1/676 chance (26 * 26) that two letters will be generated consecutively in turn the probability of any word/phrase is: $$\frac{1} {26^n}$$ Where n is the length of the word/phrase
