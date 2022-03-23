# Ideas

This file holds ideas for new sample problems to be completed using DALPy.

## Sparse2D

### Description

You are tasked with adding a new 2D array data structure to DALPy. However, this data structure will be efficient at representing sparse 2D arrays. That is, arrays that are primarily made up of zeros.

### Starter Kit

You have to implement this as a Python class that supports the following functionality:
* Initialize `Sparse2D` to have particular dimensions.
* Get the value at a row, column index.
* Set the value at a row, column index.
* Multiply each element in it by a scalar.
* Add another `Sparse2D` to it.
* Right multiply another `Sparse2D` with it.

## FastMultiply2D

### Description

You are tasked with adding a new 2D array data structure to DALPy. However, this data structure will be efficient at representing sparse 2D arrays as well as multiplying them.

### Starter Kit

You have to implement this as a Python class that supports the following functionality:
* Initialize `FastMultiply2D` to have particular dimensions.
* Get the value at a row, column index.
* Set the value at a row, column index.
* Multiply each element in it by a scalar.
* Add another `FastMultiply2D` to it.
* Right multiply another `FastMultiply2D` with it.

## OrderedHashTable

### Description

You are tasked with building a new hash table to `DALPy`. You will build upon the standard chaining hash table so that when its keys are returned, they are in the order in which they were inserted. 

### Starter Kit

You have to implement this as a Python class that supports the following functionality:
* Initialize `OrderedHashTable`.
* Insert a new key, value pair.
* Get the value associated with a key.
* Delete a key, value pair.
* Check if the `OrderedHashTable` contains a particular key.
* Get the keys of the `OrderedHashTable` in the order in which they were inserted.

*Note:* If a key was removed, then reinserted, it should be placed at the end (i.e. not in its original place).
