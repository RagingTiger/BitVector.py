#!/usr/bin/python

import time

class BitVector:
    """A bit vector (or bitmap or bit array) that allows for the efficient storage of data.
    Bit vectors don't always make sense to use, but there are some common threads where they 
    can be useful. Note that any number of these can be untrue and a bit vector may still be 
    useful.

    There are no dupilcates in your data.
    There is a known bound to the range of your elements.
    There is no additional data tied to the element outside of it's simple value.

    Some examples:
    Sorting a set of phone numbers: 
    	Loop through the input set, marking 1s in the bit vector as you go.
    	Run through the bit vector, outputting the index as you hit 1s.

    A bloom filter:
    	Establish a size for your bit vector and define a number of hash functions.
    	To set a value: Run it through all hash functions, modulo the size of the bit vector. 
                        Set the bit at the index of each result to 1.
    	To check for a value: Run it through all hash functions, modulo the size of the bit 
                                vector. Check the bit at the index of each result. If any are 
                                0, this result has never been set. If all are 1, this result 
                                was _likely_ set (may be a false positive).

    """

    # maximum index we're allowing. it starts getting slow after this
    MAX_INT = 9999999999

    # the internal integer that represents our bitmap
    vector = 0

    # a dictionary of powers of 2 to their bit-shifted representation. good kickstart to bitshifting.
    # speed_table = {}

    # a temporary variable to store our current mask
    # temp_mask = 0

    # def __init__(self, speed_table_max_key=8):
    #     if speed_table_max_key > 0:
    #         speed_table = {2**k:(1 << (2**k)) for k in range(3, speed_table_max_key)}

    def set(self, i):
        self.validate(i)
        mask = self.mask(i)
        self.vector = self.vector | mask

    def unset(self, i):
        self.validate(i)
        if self.get(i):
            mask = self.mask(i)
            self.vector = self.vector ^ mask
        # should I implement this using twos-complement negative numbers and an &?

    def get(self, i):
        self.validate(i)
        mask = self.mask(i)
        masked = self.vector & mask
        return (bool) (masked >> i)

    def mask(self, i):
        self.validate(i)

        # base = 1
        # if len(self.speed_table) > 0:
        #     (i, base) = self._speed_table_lookup(i)
        mask = 1 << i
        # self.temp_mask = 1 << i
        return mask

    # def _speed_table_lookup(self, i):
    #     key = 0
    #     value = 1
    #     for k, v in self.speed_table.iteritems():
    #         if i <= k:
    #             key = k
    #             value = v
    #         else:
    #             break
    #     return (i - key, value)

    def validate(self, i):
        if i < 0:
            raise IndexError("Index must be positive");

        if i > self.MAX_INT:
            raise IndexError("Index cannot exceed system's maxint: " + str(self.MAX_INT))
        # exception for too large int

    def __iter__(self):
        return self

    def next(self):
        # @todo fill in
        # make sure to raise a StopIteration if there's no more to iterate.
        pass


if __name__ == "__main__":
    MyBitVector = BitVector()
    print MyBitVector.get(10)
    print MyBitVector.get(3)
    MyBitVector.set(10)
    MyBitVector.set(24)
    MyBitVector.set(2524732)
    MyBitVector.unset(24)
    MyBitVector.unset(6)
    print MyBitVector.get(10)
    print MyBitVector.get(24)
    print MyBitVector.get(3)
    print MyBitVector.get(6)
    print MyBitVector.get(2524731)
    print MyBitVector.get(2524732)
    print MyBitVector.get(2524733)
    MyBitVector.set(9999999998)
    print MyBitVector.get(9999999997)
    print MyBitVector.get(9999999998)
    print MyBitVector.get(9999999999)