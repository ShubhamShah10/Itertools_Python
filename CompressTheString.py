# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s=map(int,list(raw_input()))
l=[(sum(1 for i in g),k) for k,g in groupby(s)]
print ' '.join(map(str,l))
