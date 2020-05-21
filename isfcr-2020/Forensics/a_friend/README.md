# A Friend
## Forensics Challenge

### Overview:
The zip file extracts to give a '.docx' file with something written in it"
```
hello my friend

everything is fine. 
```
Changin the bacground to any colour other than white there was some other text hiddenin white font, and it read:
```
hello my friend

everything is fine. 


cant talk right, everyone’s watching me, i hid my location, come help me 
```

So this gave me a hint that something was hidden in the file.
Tried using binwalk, but the output resulted in a zlib file which i dit know what to do with.
opening up ghex and inspecing the raw hex data of the docx file the png header `89 50 4E 47 0D 0A 1A 0A 00 00`
clearly shows that a png is hiding in the file.
This png file can be extracted with:
```
binwalk -D "png image:png" a_friend.zip
```
But i dint know this feature of binwalk and deleted out all the hex values before the png header using ghex
The png file gave the flag.

### Flag
flag{help_im_stuck_at_the_pet_store}
