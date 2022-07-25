## Shell Exercises
#### 1.  Display a report showing the full name of all the users currently connected, and the number of processes belonging to each of them.   
#### 2.  Find recursively in a directory all ".c" files having more than 500 lines. Stop after finding 2 such files.
#### 3.  Find recursively in a directory, all the files with the extension ".log" and sort their lines (replace the original file with the sorted content).	 
#### 4.  Find recursively in a given directory all the symbolic links, and report those that point to files/directories that no longer exist.  
#### 5.  Write a script that receives dangerous program names as command line arguments. The script will monitor all the processes in the system, and whenever a program known to be dangerous is run, the script will kill it and display a message.	
#### 6.  Find recursively in a directory, all the files that have write permissions for everyone. Display their names, and the permissions before and after removing the write permission for everybody.
#### 7.  Write a script that receives words as command line arguments, and searches those words in a text file. If one of them is not found, the execution of the program is suspended.
#### 8.  Write a script that for every command line argument that is a file, will:
   - compute the average line length if it's a text file
   - remove all the empty lines for C source files
   - compute the total number of comments if it's a shell file   
#### 9. Write a script that for every command line argument that is a directory, will:
   - list all the text file, including subdirectories
   - remove empty lines for all shell files, not including subdirectories
   - compute the total size for binary files, including subdirectories
   - logs all the results in the 'results.txt' file
#### 10. Write a script that reads a number N1 and then filenames, ignoring input that is not a filename, until the string "stop" is read. For each filename, the script will check if the file contains N1 lines, and adds the names of the files that do to the 'sol.txt' file. At the end, print the contents of 'sol.txt'.
