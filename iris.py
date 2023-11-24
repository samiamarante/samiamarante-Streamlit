from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import pickle
iris = datasets.load_iris(as_frame=True)
X = iris['data']
y = iris['target']
print(y)
log_reg = LogisticRegression()
log_reg.fit(X,y)

with open('iris_model.pkl', 'wb') as f:  # open a text file
    pickle.dump(log_reg, f) # serialize the list