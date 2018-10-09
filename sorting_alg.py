import timeit
import unittest


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


def radix_sort(num_list):
    pass

def heap_sort(num_list):
    pass

def quick_sort_partition(num_list,i,j):
    pivot = num_list[i]
    first = i
    i = i+1
    done = False
    while not done:
        while num_list[i] <= pivot and i <= j:
            i += 1
        while  num_list[j] >= pivot  and  j >= i :
            j -= 1
        if j < i:
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
       quick_sort_helper(num_list,i,p-1)
       quick_sort_helper(num_list,p+1,j)

def quick_sort(num_list):
    i = 0
    j = len(num_list) - 1
    quick_sort_helper(num_list,i,j)
    return num_list
        
def quick_sort_rand(num_list):
    pass

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

def main():
    unittest.main()
# def main(args):

    # num_list = read_data(args.filename)
    # run_time_list = []
    # for i in range(int(args.num_runs)):
    #     if args.algorithm == 'merge':
    #         start = timeit.default_timer()
    #         sorted_list = merge_sort(num_list)
    #         stop = timeit.default_timer()
    #         run_time = start - stop
    #     if args.algorithm == 'selection':
    #         start = timeit.default_timer()
    #         sorted_list = merge_sort(num_list)
    #         stop = timeit.default_timer()
    #         run_time = start - stop 
    #     run_time_list.append(run_time)

    
if __name__ == "__main__":
    import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--filename', action='store', help = '.txt input file' )
    # parser.add_argument('--algorithm', action= 'store', choices = ['merge', 'quick_rand', 'quick','radix'])
    # parser.add_argument('--num_runs', action= 'store')
    # args = parser.parse_args()
    # main(args)
    main()
