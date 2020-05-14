# B==P B==P
## Linux challenge
---
### Challenge description:
So the challenge gives us some ecoded text in a text file (flag.txt). 
The text is very very long. But it ends with "==" which tells us that its base64 encoded.
Since its so big, it must have been encoded multiple times.
You can use python to decode it until it cant be decoded anymore. or u could just brute force through command line,
which is what i did. I found out that it was encoded 30 times using:
```
echo "$( < flag.txt)"
```

### flag:
ctf{BA5E64_15_50_BA5ELE55}

