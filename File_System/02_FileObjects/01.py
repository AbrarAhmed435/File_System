with open('password.txt','r') as f:
    f_content=f.readlines()
    print(f_content)


""" 
Other method

f.readline() #read one line
f.readlines() # read all lines as list

"""
##########################################
with open('password1.txt','w') as f:
    f.write("New password: 1234")



""" 
'w' mode creates the file if it doesn’t exist,
and overwrites if it does.
"""

#########################################

with open('password.txt','a') as f:
    f.write("\nAnother line Written")
    


######################################
f=open('password.txt','r')

print(f.name)

f.close()



