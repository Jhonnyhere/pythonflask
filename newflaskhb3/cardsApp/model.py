import json

def load_db():
    with open('detail.json') as f:
        return json.load(f)

def save_db():
    with open('detail.json','w') as detail:
        return json.dump(db,detail)

db = load_db()        

