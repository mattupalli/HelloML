from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import pickle
iris = load_iris()

x = iris.data
y = iris.target

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(x,y)

filename = 'saved_model.pkl'
pickle.dump(knn,open(filename,'wb'))