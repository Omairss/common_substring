# Inbox Analysis

## Approach
The core algorithm is based on the longest subsequence algorithm based on dynamic programming. 
However, since the goal is to extract templates and partial string matches in templates aren't very useful, 
I decided to run the algorithm on tokens instead of characters. This should boost effiency significantly.
Last, the templates are extracted from files in a pairwise manner, 
hierarchically, allowing a time complexity of O(log(len(files)). (as in merge sort)

## How To Run
Please run the following on your terminal:
$ cd <path_to_project>/common_substring
$ pip install -r requirements.txt 
$ cd src
$ python template_finder.py file1.txt file3.txt


## Time complexity

### Time complexity of methods
longest_common_subsequence = O(len(tokens_in_text1) * len(tokens_in_text2)
get_template = O(log(n))

### Time complexity of modules
Overall Time Complexity
O(max(len(tokens_in_file) * number_of_files)


## How to run
$ cd common_substring/src/

$ python template_finder.py -h
usage: template_finder.py [-h] <filenames> [<filenames> ...]

Get common template across files

positional arguments:
  <filenames>  Add files in /data as the input. Ex <filename1.txt>
               <filename2.txt> ..

optional arguments:
  -h, --help   show this help message and exit


### Example
python template_finder.py file1.txt file2.txt file3.txt
Final Result:
 < html > < head > < title > Your Order Info < /title > < /head > < body onload= `` `` > < span > Product Information : < /span > < /body > < /html >
 
python template_finder.py file1.txt file3.txt
Final Result:
 < html > < head > < title > Your Order Info < /title > < /head > < body onload= `` handle_load `` > < span > Product Information : < /span > < div > < span > Product Name : < /span > < span > Price : $ < /span > < span > Discount : - $ < /span > < /div > < div > < span > Product Name : shirt < /span > < span > Price : $ 15.00 < /span > < /div > < /body > < /html >
