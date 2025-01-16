import os

#fetch the names from names.txt and store in a list
names=[]
with open(r'.\files\mail-merge\input\names\names.txt','r') as f:
    data=f.read()
    names=data.split('\n')

path=r'.\files\mail-merge\output' #set the directory.
for name in names:
    file_name=f'letter_{name}.txt'
    file_path=os.path.join(path,file_name) #add file name with the directory
    
    with open(r'.\files\mail-merge\input\letter\starting_letter.txt','r') as f:
        content=f.read()
        content=content.replace('[name]',name) #strings are immutable
        with open(file_path,'w') as file:
            file.write(content)


