import json

def load_data():
    with open('info.json') as imp:
        return json.load(imp)

def save_data():
        with open('info.json' , 'w') as save:
            return json.dump(data,save)
       
data = load_data()        
save = save_data()