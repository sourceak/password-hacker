# Password-Strength 
### Password-Strength operates by asking the user to input their chosen password. If the password is a commonly used one, the program informs the user of its rank in popularity. Conversely, if a unique password is provided, the program grants a distinctive checkmark as a symbol of its uniqueness and then proceeds to attempt at cracking it. If successful, it then communicates the number of "guesses" it took and the duration required to decrypt the password.

# Challenge
### The most challenging part of this project was finding the best way to iterate through potential passwords of varying lengths. Since the user could input a password of unknown length, it would have required an unknown number of nested loops. I solved this problem by learning about a module called itertools; it provides various functions to create complex iterators. I used itertools.product() to address my nested loop problem; it computes the Cartesian product of inputs. This solution was perfect as it enabled my code to iterate through all potential passwords of a given length until it cracked the user's password. Unfortunately, due to its memory-intensive nature, I optimized it to generate Cartesian products based on the user's input, such as lowercase letters, numbers, uppercase letters, or special characters. This optimization reduced runtime and allowed for the cracking of longer passwords.










