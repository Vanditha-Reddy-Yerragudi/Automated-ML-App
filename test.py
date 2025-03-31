import pickle
filename = 'finalized_model.sav'
xnew = [[0003,Europa,FALSE,A/0/S,TRAPPIST-1e,33,FALSE,0,1283,371,3329,193,Solam Susent,FALSE]]
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict(xnew)
print(result)