import wget

print("Enter the URL To download")
url = input() 

print ("Enter the file path in which you want to save the file")
path = input()

wget.download(url, path )
