# 100
## Linux challenge

### Overview:
we are given 3 files:
	p1.py
	p2.py
	key

Key: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

The challenge asks us to use the key as input for p1.py and use the resultant output as input for p2.py.
Futher use the output as input fr p1.py again.
We were asked to repeate this 100 times and the final output to be submitted as flag enclosed in ctf{}.

### Samble Shell Script:
```
#!/bin/bash

for i in {1..100}
do
	tail -n 1 flag | python3 p1.py | python3 p2.py >> flag
done

echo "ctf{""$(tail -n 1 flag)""}" > final_flag.txt
cat final_flag.txt
``` 

what this script does is, say our key is stored in a file called 'flag'.
Upon execution 'flag file has all the outputs of every iteration.
The final output (flag) is stored in 'final_flag.txt'

### 'flag' file output:
```
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
b2cc4ea0f9d7efafc567a2fe8e760722e86bd974
50f2abdfd5601da8fed4e3a221524340a7fb9f34
.
.
.
eaea75644132331b6237a138f119388ac5088380
718089881444cd3df847ae9a578f847c91eb383e
63468bb870ac10ef968ae42c7d8af189b441671a
```

### Final Flag:
ctf{63468bb870ac10ef968ae42c7d8af189b441671a}

