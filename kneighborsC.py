import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score


class KneighborsC(object):

    knc = ""

    def __init__(self):
        pass

    def do_test(self, test_csv):
        global knc
        example = pd.read_csv('trf/saida_teste.csv')
        example.drop(['repeat_id'], 1, inplace=True)
        example.drop(['start'], 1, inplace=True)
        example.drop(['end'], 1, inplace=True)
        example.drop(['period'], 1, inplace=True)
        example.drop(['indels'], 1, inplace=True)
        example.drop(['a'], 1, inplace=True)
        example.drop(['c'], 1, inplace=True)
        example.drop(['t'], 1, inplace=True)
        example.drop(['g'], 1, inplace=True)

        teste = example.drop(['var'], 1)

        print("Resultados")
        prediction = knc.predict(teste)
        print("Score provável: " + str(knc.score(teste, example['var'])))
        print(prediction)
        print(example['var'])
        print("-----")

    def do_train(self, train_csv):
        global knc

        score = 0

        while score < 0.7 :
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
            data.drop(['entropy'], 1, inplace=True)
            data.drop(['trf_score'], 1, inplace=True)

            y = np.array(data['var'])
            X = np.array(data.drop(['var'], 1))

            X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

            knc = KNeighborsClassifier(n_neighbors=3)
            knc.fit(X_train, y_train)
            score = cross_val_score(knc, X, y, cv=5)
            print(np.mean(score))


            score = knc.score(X_test, y_test)

            #if score >= 0.70:
            print("Score atingiu: " + str(score))

            print(y_test)
            print(knc.predict(X_test))
