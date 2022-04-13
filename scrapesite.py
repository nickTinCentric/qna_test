##import packages - need to insall these if you do not have them in your environment
from urllib import request
# from bs4 import BeautifulSoup

#set URL
#this is using a demo.aspx site that i found on the web
myurl = 'https://asa24.nci.nih.gov/2013/demo.aspx'

#connect to url
response = request.urlopen(myurl)
#confirm connection
type(response)



#collect elements from site's code
html = response.read().decode('utf8')
type(html)

#confirm elements
print()
print(html[:500])

## output file
## writing to local folder, change path if needed
outfile1 = 'aspxsite.html'
#open a file
fout = open(outfile1, 'a')
#write the lines from the scrapped site and close file
fout.writelines(html)
fout.close()


## added this bit to also output to .docx file
## docx package willneed to be installed in the python environment

# import docx

# #initiate docuement into variable
# mydoc = docx.Document()

# #add the scraped code into the document
# mydoc.add_paragraph(html)

# #save the docx file, this too is going to local environment path, change path if needed
# mydoc.save('test.docx')