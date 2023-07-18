def describe_city(city, country='USA'):
    print(city + " is in " + country)
    
describe_city('New York')

# ---
def make_album(sname, aname, num=None):
    if num:
        return {'singer':sname, 'album':aname, 'num':num}
    else:
        return {'singer':sname, 'album':aname}
    
print(make_album('a','b',12))

# 8-9
unprint_messages = ['a','b','c']

def show_messages(messages):
    for message in messages:
        print(message)
        
show_messages(unprint_messages)