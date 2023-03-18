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
