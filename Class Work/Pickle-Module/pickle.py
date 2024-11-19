import pickle
with open("molu.pickle", "rb") as file:
    lodded_data = pickle.load(file)

    print("Decentrelization data : ",lodded_data)