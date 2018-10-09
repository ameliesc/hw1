import timeit
import unittest
import random
import numpy as np

def read_data(filename):
    with open(filename) as f:

        array = []        
        for line in f: 
            array.extend([int(x) for x in line.split()])
    return array

def selection_sort(num_list):

    i = 1
    while i < len(num_list):
        largest = 0
        j = len(num_list) - i
        index = 0
        while j > 0:

                        
            if num_list[j] > largest:
                largest = num_list[j]
                index = j
            j = j -1
        j = 0
        if num_list[j] > largest:
            largest = num_list[j]
            index = j


        j = len(num_list) - i
        num_list[index] = num_list[j]
        num_list[j] = largest
        i = i+1
    return num_list

##################
### Radix sort ###
##################

def radix_sort(num_list):
   
    max_val = max(num_list)
    exp = 1
    
    while max_val/exp > 0:
        counting_sort(num_list,exp)
        exp *= 10

    return num_list
def counting_sort(num_list,exp1):
    b_array = [0] * len(num_list)  
    c_array = 10 * [0]
    for n in num_list:
        c_array[(n/exp1)%10] += 1
    for i in range(1,10):
        c_array[i] += c_array[i-1]

    i = len(num_list)-1
    while i>=0: 
        index = (num_list[i]/exp1) 
        b_array[ c_array[ (index)%10 ] - 1] = num_list[i] 
        c_array[ (index)%10 ] -= 1
        i -= 1

    for i in range(0,len(num_list)):
        num_list[i] = b_array[i]

################
### Heapsort ###
################        

def build_heap(A):
    i = (len(A)-1)//2
    #import pdb; pdb.set_trace()

    while i >= 0:
        heapify(A,i)
        i -=1


def heapify(array,i):
    #import pdb; pdb.set_trace
    if i > (len(array)-1)//2:
        return 0


    l = 2*i+1 #cause counting from 0
    r = 2*i+2


    if l <= len(array)-1 and array[l] > array[i]:
        largest = l
    else:
        largest = i
    if r <= len(array)-1 and array[r] > array[largest]:
        largest = r
    if largest != i:
        temp = array[i]
        array[i] = array[largest]
        array[largest] = temp
        heapify(array,largest)
    return array
        
def heap_sort(num_list):
    build_heap(num_list)
    i = len(num_list) -1
    while i >= 1:
        temp = num_list[i]
        num_list[i] = num_list[0]
        num_list[0] = temp
        num_list[:i] = heapify(num_list[:i],0)
        i -=1
    return num_list

#########################
### Quicksort  + rand ###
#########################

def quick_sort_partition_rand(num_list,i,j):
    pivot_index = random.randint(i,j)
    temp = num_list[i]
    num_list[i] = num_list[pivot_index]
    num_list[pivot_index] = temp
    return quick_sort_partition(num_list, i, j)

def quick_sort_helper_rand(num_list,i,j):
   if i<j:
       p  = quick_sort_partition_rand(num_list,i,j)
       quick_sort_helper_rand(num_list,i,p-1)
       quick_sort_helper_rand(num_list,p+1,j)

def quick_sort_rand(num_list):
    i = 0
    j = len(num_list) - 1
    quick_sort_helper_rand(num_list,i,j)
    return num_list



def quick_sort_partition(num_list,i,j):
    pivot = num_list[i]
    first = i
    i = i+1
    done = False
    while not done:
        while num_list[i] <= pivot and i <= j and i < len(num_list)-1:
            i += 1
        while  num_list[j] >= pivot  and  j >= i and j >first -1:
            j -= 1
        if j < i:
            done = True
        elif j == len(num_list) -1 and i == len(num_list) -1:
            done = True
        elif j == first and i == first :
            done = True
            
        else: 
            left_s = num_list[i]
            right_s = num_list[j]
            num_list[i] = right_s
            num_list[j] = left_s
            
    num_list[first] = num_list[j]
    num_list[j] = pivot
    return j

def quick_sort_helper(num_list,i,j):
   if i<j:
       p  = quick_sort_partition(num_list,i,j)
       if j - p+1  <  p-1 - i:
           quick_sort_helper(num_list,p+1,j)
           quick_sort_helper(num_list,i,p-1)
       elif  j - p+1  >  p-1 - i:
           quick_sort_helper(num_list,i,p-1)
           quick_sort_helper(num_list,p+1,j)
       else:
           quick_sort_helper(num_list,p+1,j)
           quick_sort_helper(num_list,i,p-1)

def quick_sort(num_list):
    i = 0
    j = len(num_list) - 1
    quick_sort_helper(num_list,i,j)
    return num_list
        
##################
### Merge Sort ###
##################
def merge_sort(num_list):
    
    l = len(num_list)
    
    if l>1:
        num_list_left = num_list[: l//2]
        num_list_right = num_list[l//2 : ]
        merge_sort(num_list_left)
        merge_sort(num_list_right)

        
        i=0
        j=0
        k=0
        while i < len(num_list_left) and j < len(num_list_right):
            if num_list_left[i] < num_list_right[j]:
                num_list[k]=num_list_left[i]
                i=i+1
            else:
                num_list[k]=num_list_right[j]
                j=j+1
            k=k+1

        while i < len(num_list_left):
            num_list[k]=num_list_left[i]
            i=i+1
            k=k+1

        while j < len(num_list_right):
            num_list[k]=num_list_right[j]
            j=j+1
            k=k+1

    return num_list

class MyTest(unittest.TestCase):

    def test_sorting(self):
        num_list = read_data("./hw1_data/testing_file.txt")
        self.assertEqual(merge_sort(num_list), [1,2,3,4,5,6,7,7,8,9])
        num_list = read_data("./hw1_data/testing_file.txt")
        self.assertEqual(selection_sort(num_list), [1,2,3,4,5,6,7,7,8,9])
        num_list = read_data("./hw1_data/testing_file.txt")
        self.assertEqual(quick_sort(num_list), [1,2,3,4,5,6,7,7,8,9])
        num_list = read_data("./hw1_data/testing_file.txt")
        self.assertEqual(quick_sort_rand(num_list), [1,2,3,4,5,6,7,7,8,9])
        #num_list = read_data("./hw1_data/testing_file.txt")
        #self.assertEqual(counting_sort(num_list), [1,2,3,4,5,6,7,7,8,9])
        num_list = read_data("./hw1_data/testing_file2.txt")
        self.assertEqual(radix_sort(num_list), [3,12,34,404,450,500])
        num_list = read_data("./hw1_data/testing_file.txt")
        self.assertEqual(heap_sort(num_list), [1,2,3,4,5,6,7,7,8,9])

def main_testing():
    unittest.main()


def main(args):

    num_list = read_data(args.filename)
    run_time_list = []
    for i in range(0,int(args.num_runs)):
        if args.algorithm == 'merge':
            start = timeit.default_timer()
            sorted_list = merge_sort(num_list)
            stop = timeit.default_timer()
            run_time = stop - start
        if args.algorithm == 'selection':
            start = timeit.default_timer()
            sorted_list = merge_sort(num_list)
            stop = timeit.default_timer()
            run_time = stop - start
        if args.algorithm == 'quick_rand':
            start = timeit.default_timer()
            sorted_list = quick_sort_rand(num_list)
            stop = timeit.default_timer()
            run_time = stop - start
        if args.algorithm == 'quick':
            start = timeit.default_timer()
            sorted_list = quick_sort(num_list)
            stop = timeit.default_timer()
            run_time = stop - start
        if args.algorithm == 'radix':
            start = timeit.default_timer()
            sorted_list = radix_sort(num_list)
            stop = timeit.default_timer()
            run_time = stop - start
        if args.algorithm == 'heap':
            start = timeit.default_timer()
            sorted_list = heap_sort(num_list)
            stop = timeit.default_timer()
            run_time = stop - start 
        run_time_list.append(run_time)
    print("The average run time for %s sort is: " % args.algorithm, np.average(np.asarray(run_time_list)))

    
if __name__ == "__main__":
    #main_testion()
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', action='store', help = 'path to .txt input file' )
    parser.add_argument('--algorithm', action= 'store', choices = ['selection', 'merge', 'quick_rand', 'quick','radix', 'heap'])
    parser.add_argument('--num_runs', action= 'store')
    args = parser.parse_args()
    main(args)
 
