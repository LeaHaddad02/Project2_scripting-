import re
# read content from the html code 
with open('index.html', 'r') as file:
    html_contents = file.read()
#regular expression 
a_tags = re.findall(r'<a\s+(?:[^>]*?\s+)?href=(\"|\')([^\"\']*)\\1', html_contents)
#extract the value of href attribute in a list 
hrefs = [tag[1] for tag in a_tags]
#Store unique href values in a set in order to remove duplicates 
unique_hrefs = set(hrefs)
