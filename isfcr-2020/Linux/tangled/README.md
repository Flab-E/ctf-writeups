# Tagled
## Linux Challenge

### Solution:
Upon extracting the conents of the zip file given we se a directory called '2' which further leads to other directories.
There are also hidden direstories as we go towards the last directory
The following linux command can be used to list all directories in a directory including hidden ones:
```
ls -la
```
In this method I had to manually inspect each directory.

Another method i stumbled upon was to just type in `cd` to the first directory '2' and just press on `TAB` key
until nothing more pops up on the screen.
That way we get:
```
cd 2/ctf\{\}/.50/.many/.challenges/.50/.LE55/.T1ME/
```

Finally we arrive at an executable hidden python file called '.flag'. Convert it to executable format with:
```
chmod +x .flag
./.flag
```

### Flag:
ctf{50_MANY_CHALLENGES_50_LE55_T1ME}

