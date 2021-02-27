import pickle

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)
    
def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

if __name__ == '__main__':
    test_dict = {'name': 'jason', 'age': 19, 'height': '5.5ft'}
    save_dict(test_dict, "06 Save a Dictionary/test_dict.pickle")
    recovered = load_dict("06 Save a Dictionary/test_dict.pickle")
    print(recovered)