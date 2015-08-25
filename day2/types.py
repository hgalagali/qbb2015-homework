#!/usr/bin/env python

# integer
i=10000

i_as_f = float (i)

#float
f=0.356

f_as_i = int (f)

# String
s="String"

#Boolean
t=True
fa=False

#List
l=[1,2,3]
l.append(7)

#Tuple
tu=(1, "foo", 5.0)

#Dictionary
d1={"key1":"value1", "key2":"value2"}
d2=dict(key1="value1", key2="value2")
d3=dict([("key1","value1"), ("key2", "value2")])

for value in (i, f, s, t, fa, l, tu, d1, d2, d3):
    print value, type(value)