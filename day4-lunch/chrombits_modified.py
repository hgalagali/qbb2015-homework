import numpy
import copy

class ChromosomeLocationBitArrays(object):

    def __init__(self, dicts=None, fname=None):
        if dicts is not None:
            arrays=dicts
        else:
            arrays = {}
        if fname is not None:
            for line in open(fname):
                fields = line.split()
                name = fields[0]
                size = int(fields[1])
                arrays[name]=numpy.zeros(size, dtype=bool) 
        self.arrays = arrays

    
    def set_bits_from_file(self, fname):
        for line in open(fname):
            fields = line.split()
            chrom = fields[0]
            start = int(fields[1])
            end = int(fields[2])
            self.arrays[chrom][start:end] = 1
        
    def intersect(self, arrays2):
        rval={}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] & arrays2.arrays[chrom]
        return ChromosomeLocationBitArrays(dicts=rval)
    
    def union(self, arrays2):
        rval={}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] | arrays2.arrays[chrom]
        return ChromosomeLocationBitArrays(dicts=rval)
    
    def complement(self):
        rval={}
        for chrom in self.arrays:
            rval[chrom]= ~self.arrays[chrom]
        return ChromosomeLocationBitArrays(dicts=rval)
        
    def copy(self):
        return ChromosomeLocationBitArrays(dicts=copy.deepcopy(self.arrays))
        
    def make_tuples(self):
        tuple_list=[]
        for chrom, value in self.arrays.iteritems():
            for i in range(0, len(value)-1, 1):
                if value[i]==0 and value[i+1]==1:
                    start=i+1
                if value[i]==1 and value[i+1]==0:
                    stop=i
                    tuple_list.append((chrom, start, stop))
        return tuple_list
                
        
