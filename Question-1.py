SkillSanta_Dict = {
    "name":"Sachin",
    "age":22,
    "salary":60000,
    "city":"New Delhi"
}

print ("initial values dictionary = ", SkillSanta_Dict) 
  
SkillSanta_Dict['location'] = SkillSanta_Dict['city'] 
del SkillSanta_Dict['city'] 

print ("final dictionary = ", SkillSanta_Dict)
