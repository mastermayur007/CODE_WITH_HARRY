import os

def CreateIfNotExit(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}") 
if __name__=="__main__":                
    files=os.listdir()
    files.remove('arrenge_file.py')
    print(files)  
    CreateIfNotExit('Images')
    CreateIfNotExit('Docs')
    CreateIfNotExit('Media')
    CreateIfNotExit('Others')
    imgExts=['.png','.jpg','.jpeg']
    images=[file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    docExts=['.txt','.docx','.doc','.pdf']
    docs=[file for file in files if os.path.splitext(file)[1].lower() in docExts]
    mediaExits=['.mp4','.mp3','.flv']
    medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaExits]     
    others=[]
    for file in files:
       ext=os.path.splitext(file)[1].lower()
       if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExits) and os.path.isfile(file):
        others.append(file)
    print(others) 
    move('Images',images)
    move('Docs',docs)
    move('Media',medias)
    move('Others',others)  

                 
