import json
data=[
    {
    "name": "Abrar",
    "age": 21,
    "skills": ["Python", "FastAPI"]
}
]


# write json

with open("data.json",'w') as f:
    json.dump(data,f,indent=4)
    
    
# Read JSON

with open('data.json','r') as f:
    content=json.load(f)
    print(content)