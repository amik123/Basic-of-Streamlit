collection=[{'name':'Amik','age':22,'place':'kathmandu'},
            {'name':'aakash','age':16,'place':'kathmandu'},
            {'name':'Kamal','age':24,'place':'pokhara'},
            {'name':'rajiv','age':17,'place':'pokhara'},]

def check(person):
    if person['age']>20:
        return person

filtered_data=list(filter(check,collection))
print(filtered_data)