# Project2_scripting-
## Report
### Discover subdomains, directories, and files
1. Import request library in order to send http request using python
- The http request will return a response object
2.	List all the subdomains to scan in a list
3.	Same for directories and file extension
4.	 Use for loop 
- get: send a request to the specific URL  
- status_code for validation:
i.	200 for success
ii.	404 for error 
### Extract href from html
1.	Open the file to read the html source 
-	The first argument of the open() function is the file name and the second argument specifies the mode in which the file is opened. In this case, the mode is 'r', which means the file is opened in read-only mode.
- 	Use file.read() in order to go over all the code
2.	Regular expression to extract all possible links in the href attribute of the html code:
- 	<a\s+ is for the tag and the space(s) after.
- 	(?:[^>]*?\s+)? is the non-capturing group to match characters before the end of the tag (>) and it’s optional because we can have as the first attribute the href one.
- 	href=(\”|\’) matches the string “href=” it is usually followed by quotes so we need to escape them (single or double) we use them in a register in order to store them.    
- 	([^\"\']*) matches all characters that are not quotes 
- 	\\1    refers to the register where we stored the quotations
- 	Concatenate everything to have the complete regular expression 
- 	Use it in python with the findall method 
3.	Use a list comprehension to extract the value of the href attribute from a list of<a> tags
4.	Remove duplicate 
### Challenges
1.	The first big problem is the lack of knowledge in the web development world. 
-	As a first-year bioinformatics student who is not so aware of the web world, this project is far away from my actual knowledge, but it’s okay; after a little explanation in class and many research, I was able to give somehow a final output regarding how to extract subdomains and directories.
2.	Using advanced python language 
-	As a CP1 student learning python is still under process, using important libraries such as the request one was a bit challenging, but with again, research and new discoveries this difficulty was overcome. 
3.	The regular expression
-	Too much detail in one regular expression; writing it took too much time to match everything; here personally I searched multiple sites to combine everything.  
4.	The GitHub part
-	GitHub is very new to me; I never used it before this course. The entire concept of implementing code on GitHub is still strange, to handle this task, I preferred writing the code and making all the changes in the .py file directly. In the end, I uploaded the final version of the file directly to the repository. The report was written as a read.me file.  

