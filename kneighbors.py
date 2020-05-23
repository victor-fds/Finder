import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

class Kneighbors(object):

    def __init__(self):
        pass

    def do_kneighbors(self, train_csv):
        data = pd.read_csv(train_csv)

        # utiliza apenas consensus_size, copy_nro e purity
        data.drop(['repeat_id'], 1, inplace=True)
        data.drop(['start'], 1, inplace=True)
        data.drop(['end'], 1, inplace=True)
        data.drop(['period'], 1, inplace=True)
        data.drop(['indels'], 1, inplace=True)
        data.drop(['a'], 1, inplace=True)
        data.drop(['c'], 1, inplace=True)
        data.drop(['t'], 1, inplace=True)
        data.drop(['g'], 1, inplace=True)
        #data.drop(['entropy'], 1, inplace=True)
        # data.drop(['trf_score'], 1, inplace=True)


        y = np.array(data['trf_score'])
        X = np.array(data.drop(['trf_score'], 1))

        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75)

        KNR = KNeighborsRegressor(n_neighbors=2, algorithm='auto')
        KNR.fit(X_train, y_train)

        print(KNR.score(X_test, y_test))

        print(y_test)
        print(KNR.predict(X_test))
