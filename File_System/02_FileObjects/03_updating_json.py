# import json

# # step 1: real json

# with open("data.json",'r') as f:
#     data=json.load(f)
    

# # step 2: Modify the dictionary
# data["age"]=22

# # Step 3: Write back to the file

# with open("data.json",'w') as f:
#     json.dump(data,f,indent=4)
    
    
# #Adding new key

# data['city']="Bangalore"

# with open("data.json",'w') as f:
#     json.dump(data,f,indent=4)
    
    
# # with open('data.json','r+') as f:
# #     data=json.load(f)
# #     data['skills'].append


# import json
# with open('data.json','r') as f:
#     data=json.load(f)

# #create new user

# new_user={
#     "name":"khan",
#     "age":44,
#     "skills":[
#         "backchodi",
#         "masti"
#     ]
# }

# data.append(new_user)

# with open("data.json",'w') as f:
#     json.dump(data,f,indent=4)
    
    
import json
import os

file_path='data.json'

if not os.path.exists(file_path):
    with open(file_path,'w') as f:
        json.dump([],f) 
        
with open(file_path,'r+') as f:
    data=json.load(f)

new_user={
    "name":"khan3",
    "age":44,
    "skills":[
        "backchodi",
        "masti"
    ]
}

data.append(new_user)

with open(file_path,'w') as f:
    json.dump(data,f,indent=4)



#########################################

for user in data:
    if user['name']=='khan':
        user['age']=900
        updated=True
        
if updated:
    with open('data.json','w') as f:
        json.dump(data,f,indent=4)
        