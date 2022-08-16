## 🐱‍💻 Assembly Exercises
#### 1.  Given a character string S, obtain the string D containing all special characters (!@#$%^&*) of the string S:
   - S: '+', '4', '2', 'a', '@', '3', '$', '*'
   - D: '@','$','*'
#### 2. A file name is given (defined in the data segment). Create a file with the given name, then read numbers from the keyboard and write only the numbers divisible by 7 to file, until the value '0' is read from the keyboard.
#### 3. Given the word A and the byte B, compute the doubleword C:
   - the bits 0-3 of C have the value 1
   - the bits 4-7 of C are the same as the bits 0-3 of A
   - the bits 8-13 of C have the value 0
   - the bits 14-23 of C are the same as the bits 4-13 of A
   - the bits 24-29 of C are the same as the bits 2-7 of B
   - the bits 30-31 have the value 1
#### 4. Write an asm program that reads a number from the standard input and computes its factorial recursively.
#### 5. An array of words is given. Write an asm program in order to obtain an array of doublewords, where each doubleword will contain each nibble unpacked on a byte (each nibble will be preceded by a 0 digit), arranged in an ascending order within the doubleword.
#### 6. Compute the following unsigned value: x-(a*a+b)/(a+c/a), where: a,c- byte; b - doubleword; x - qword.
#### 7. Compute the following unsigned value: (b+b)+(c-a)+d, where: a - byte, b - word, c - double word, d - qword.
#### 8. Write an asm program that reads a string of numbers from the standard input, given in the base 10 as signed numbers (a string of characters is read from the keyboard and a string of numbers must be stored in the memory).
#### 9. Write an asm program that reads from a file, transforms any decimals from 0-9 by adding 1 to each of them, then writes the modified content to another file, until finding a period:
   - input file: Ana are 4 mere, 2 mure si 9 pere.
   - output file: Ana are 5 mere, 3 mure si 0 pere.
