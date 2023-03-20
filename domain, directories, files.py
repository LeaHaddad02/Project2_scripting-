import requests
#Enter the target domain name
target_domain = input("enter the url for the target domain name: ")
#List of subdomains to scan
subdomains=[]
with open("subdomains_dictionary.json", "r") as file:
    for line in file:
        subdomains.append(line)
#List of directories to scan
directories=[]
with open("dirs_dictionary.json", "r") as file:
    for line2 in file:
        directories.append(line2)
#List of file extensions to scan
file_extensions = [".txt", ".php", ".html", ".js", ".css", ".jpg", ".png", ".pdf"]
#Loop through the subdomains
for i in subdomains:
    #adding the 'f'for formatted strings
    url = f"http://{i}.{target_domain}"
    response = requests.get(url)
    #validating the subdomain 
    if response.status_code == 200:
        with open("subdomains_output.bat", "w") as f:
            print(f"Subdomain found: {url}", file=f)
    #Loop through the directories
    for j in directories:
        url = f"http://{target_domain}{j}"
        response = requests.get(url)
        #validating the directory
        if response.status_code == 200:
            with open("directories_output.bat", "w") as f:
                print(f"Directory found: {url}",file=f)
        #Loop through the file extensions
        for k in file_extensions:
            url = f"http://{target_domain}/{j}/file{k}"
            response = requests.get(url)
            #validating the extension
            if response.status_code == 200:
                with open("files_output.bat", "w") as f:
                    print(f"File found: {url}", file=f)


