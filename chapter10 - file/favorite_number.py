import json
favorite_number = input("what's your favorite number?")
with open('fn.json', 'r+', encoding='utf-8') as f:
    json.dump(favorite_number, f)
    
with open('fn.json', 'r', encoding='utf-8') as f:
    print(json.load(f))
    