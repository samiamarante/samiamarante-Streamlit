from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import pickle

iris = datasets.load_iris(as_frame=True)
X = iris['data']
y = iris['target']
log_reg = LogisticRegression().fit(X,y)

with open('iris_model.pkl', 'wb') as f: 
    pickle.dump(log_reg, f)