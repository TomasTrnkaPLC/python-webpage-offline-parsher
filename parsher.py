# importing the libraries
from bs4 import BeautifulSoup
import requests
import pickle
import os.path
directory = 'C:/way to output file'
filename = "vystup.txt"
file_path = os.path.join(directory, filename)
print (file_path)
my_list = list()

for path, dirs, files in os.walk(r"C:/waytofiles in directory/"):
    for f in files:
        html_files = os.path.join(path, f)
        print(html_files)
       
        # Parse the html content
        soup = BeautifulSoup(open(html_files, encoding="utf-8"), "lxml")
        for link in soup.select('a[href^=mailto]'): 
            print("Inner Text: {}".format(link.text))
            my_list.append(format(link.text))
            
  
newEmails = list(filter(lambda x : x != 'infoma@infoma.sk', my_list))
print (newEmails)         
file = open(file_path, 'w') #write to file

for line in newEmails:
     file.write(line+"\n")
file.close() #close file          
            
            