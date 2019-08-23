from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
iris = load_iris()

x = iris.data
y = iris.target
#print(x.shape)
#print(y.shape)
#print(y.shape)

#instantiating k meains algorithm
knn = KNeighborsClassifier(n_neighbors=1)
#print(knn)
knn.fit(x,y)
n = input("Enter a number: ")
a = float(knn.predict([[3,4,5,n]]))
if a==2:
    print("iris")
elif a==1:
    print("iris again")
else:
    print("no iris")

