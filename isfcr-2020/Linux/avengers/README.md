# Avengers Assemble
## Linuc Challemge

### Overview
This challenge gave me 2 '.out' files. Each have an assembly dump of a function.
The question asked was to find the address where the following operation occurs:
```
 X = address(Y*4 + Z) 
	where X, Y and Z are all 64-bit GPR's
```
The flag which was the last 4 digits of the address had to be enclosed in 'ctf{}'.
I found the given operaton in 'f1.out' file
```
	0x0000000000000797 <+36>:    movslq %ebx,%rax
	0x000000000000079a <+39>:    lea	0x0(%rbp,%rax,4),%rdi
	0x000000000000079f <+44>:    lea	0x4(%rbp,%rax,4),%rsi

```
Looks like `0x000000000000079a` is the right one.

### Flag:
ctf{079a}

