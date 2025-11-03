import os
print(os.getcwd())

os.chdir('/home/abrar/Desktop/') ## change directory 

print(os.getcwd())

print(os.listdir()) #list folders


#creating folder 

os.mkdir("Created_via_Python")

#creating deep folders(sub directories)

os.makedirs("layer1/layer2/layer3")

#Deleting directory

os.rmdir("dltthis")

os.removedirs('layer1/layer2/layer3')

