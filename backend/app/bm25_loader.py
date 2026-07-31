import pickle

def load_bm25():

    with open("data/bm25.pkl", "rb") as f:
        return pickle.load(f)