from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import pickle
iris = load_iris()

x = iris.data
y = iris.target
#print(x.shape)
#print(y.shape)
#print(y.shape)

#instantiating k meains algorithm
#instantiating k meains algorithm
knn = KNeighborsClassifier(n_neighbors=1)
#print(knn)
knn.fit(x,y)
model = pickle.dump(knn)
saved_model = pickle.loads(model)
#n = input("Enter a number: ")
a = float(saved_model.predict([[1,3,4,5]]))
print(a)
