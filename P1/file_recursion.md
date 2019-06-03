### Design Choice
The code first builds a list with all files and directories, then separates files and 
directories, then creates a new list with files, and then searches this list accoring 
to search criteria.

### Runtime Complexity for file recursion code

n = number of files + directories
 - Create file + directory list: O(n)
 - Separate into file- and directory list: O(n)
 - search through file list: O(n)

Overall complexity: O(n)

### Space complexity
O(n)
