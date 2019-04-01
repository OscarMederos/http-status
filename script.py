import requests

# Read the domains file and create an empty array
files = open('domains.txt')
domains = []

# Fill the array with the contents of the first column of the domains file
for line in files:
    columns = line.split()
    domains.append("https://" + columns[0])

# For every url in domains perform an HTTP GET & print url + success or failed
for url in domains:
    try:
        response = requests.get(url)
        print(url + " Success")
    except:
        print(url + " Failed")
