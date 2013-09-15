

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

    vector = 0

    def set(self, i):
        mask = 1 << i
        self.vector = self.vector | mask

    def unset(self, i):
        if (self.get(i)):
            mask = 1 << i
            self.vector = self.vector ^ mask
        # should I implement this using twos-complement negative numbers and an &?

    def get(self, i):
        mask = 1 << i
        masked = self.vector & mask
        return (bool) (masked >> i)

    def validate(self, i):
        if (i < 0):
            raise Exception
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
    MyBitVector.set(9999999999999999999999999999999999999999999999999999999999999989)
    print MyBitVector.get(9999999999999999999999999999999999999999999999999999999999999988)
    print MyBitVector.get(9999999999999999999999999999999999999999999999999999999999999989)
    print MyBitVector.get(9999999999999999999999999999999999999999999999999999999999999999)