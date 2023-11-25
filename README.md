# Regular Expressions
## Regular Expressions in Python

The re.I or re.IGNORECASE means ignore case sensitive
^ is the same as \A
$ is the same as \Z
\d means a digit
\D means no digit

### What can got in [...]
[aeiou] any lowercase vowel
[ aeiou] any space or any lowercase vowel
[A-Z] any upper case alphabetic
[A-Za-z] any alphabetic
[A-Za-z\]] any alphabetic or a ']' backslashed character
[A-Za-z\-] any alphabetic or a '-'
[-A-Za-z] any alphabetic or a '-' as the first character: special behaviour for '-' only
[^aeiou] not any lowercase vowel
[^A-Z] not any uppercase alphabetic
[\^A-Z] any uppercase alphabetic or a caret

### Counting in regular expressions
[abc] any one of 'a', 'b' or 'c'.
[abc]+ One or more 'a', 'b' or 'c'.
[abc]? Zero or one 'a', 'b' or 'c'.
[abc]* Zero or more 'a', 'b' or 'c'.
[abc]{6} Exactly 6 of 'a', 'b' or 'c'.
[abc]{5,7} 5,6 or 7 of 'a', 'b' or 'c'.
[abc]{5,} 5 or more of 'a', 'b' or 'c'.
[abc]{,7} 7 or fewer of 'a', 'b' or 'c'.

### What matches "["?
"[abcd]" matches any one of "a", "b", "c" or "d".

### What matches "[abcd]"?
[abcd] any one of "a", "b", "c", "d.
\[abcd\] [abcd] Generally speaking, if a character has a special meaning the preceding it with a backslsh turns off that specialness. So "[" is a special, but "\[" means "just and open square bracket". (Similarly, if we want to match a backslash we use "\\".)

### Backslash
[   ] used to hold sets of characters
\[  \] the real square brackets
d the letter "d"
\d any digit

### What does dot match?
.     "." matches any character except "\n".  "\n" matches the new line character.
\.    "\." matches just the dot.

### Special codes in regular expressions
\A    ^   Anchor start of line
\Z    $   Anchor end of line
\d        Any digit
\D        Any non-digit
.         Any character except newline