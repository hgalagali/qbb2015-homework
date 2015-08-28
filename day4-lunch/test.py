#!/usr/bin/env python

import chrombits_modified
import sys

arr = chrombits_modified.ChromosomeLocationBitArrays(fname=sys.argv[1])

A=arr.copy()
B=arr.copy()

A.set_bits_from_file(fname=sys.argv[2])
B.set_bits_from_file(fname=sys.argv[3])


A_and_not_B = A.intersect(B.complement())

tuple_list = A_and_not_B.make_tuples()

print tuple_list