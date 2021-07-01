import numpy as np
from Graphs import view
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
import warnings
import mysql.connector
from sklearn.metrics import precision_score
from DBconn import DBConnection
import sys
from sklearn import metrics




def evaluation():
    try:
        trainset = []
        mydb = DBConnection.getConnection()
        cursor = mydb.cursor()
        cursor.execute("select * from m_dataset")
        row = cursor.fetchall()
        # print("row",row)
        y_train = []
        trainset.clear()
        y_train.clear()
        for r in row:
            x_train = []
            x_train.clear()
            x_train.append(int(r[0]))
            x_train.append(int(r[1]))
            x_train.append(int(r[3]))
            x_train.append(int(r[4]))
            y_train.append(r[6])
            trainset.append(x_train)
        print("[INFO] Processing")
        datainput = np.array(trainset)
        y = np.array(y_train)
        x_train, x_test, y_train, y_test = train_test_split(datainput, y, test_size=0.3)
        del_query = "DELETE FROM performance WHERE Algorithm = 'Gaussian'"
        cursor.execute(del_query)
        query2 = "INSERT INTO  performance  VALUES (%s,%s,%s,%s,%s)"
        classify5 = GaussianNB()
        classify5.fit(x_train, y_train)
        predicted5 = classify5.predict(x_test)
        gnb = metrics.accuracy_score(y_test, predicted5) * 100
        print("The accuracy score using the GaussianNB is ->")
        print(metrics.accuracy_score(y_test, predicted5))

        precision=metrics.precision_score(y_test, predicted5, average='weighted', pos_label='1')
        print("Precision score of GaussianNB IS ->")
        print(metrics.precision_score(y_test, predicted5, average='weighted', pos_label='1'))

        recall=metrics.recall_score(y_test, predicted5, average='weighted', pos_label='1')
        print("Recall score of GaussianNB  IS ->")
        print(metrics.recall_score(y_test, predicted5, average='weighted', pos_label='1'))

        f1_score=metrics.f1_score(y_test, predicted5, average='micro', pos_label='1')
        print("F1 score of Gaussian IS ->")
        print(metrics.f1_score(y_test, predicted5, average='micro', pos_label='1'))
        print('---------------------------------------------- ')
        val1 =(str("Gaussian"),float(gnb),float(precision), float(recall), float(f1_score))
        cursor.execute(query2, val1)

        del_query = "DELETE FROM performance WHERE Algorithm = 'DTC'"
        cursor.execute(del_query)
        classify6 = DecisionTreeClassifier()
        classify6.fit(x_train, y_train)
        predicted6 = classify6.predict(x_test)
        dt = metrics.accuracy_score(y_test, predicted6) * 100
        print("The accuracy score using the DecisionTreeClassifier is ->")
        print(metrics.accuracy_score(y_test, predicted6))

        precision=metrics.precision_score(y_test,predicted6,average='micro' ,pos_label='1')
        print("Precision score of DecisionTreeClassifier IS ->")
        print(metrics.precision_score(y_test,predicted6,average='micro' ,pos_label='1'))

        recall=metrics.recall_score(y_test, predicted6,average='micro', pos_label='1')
        print("Recall score of DecisionTreeClassifier IS ->")
        print(metrics.recall_score(y_test, predicted6,average='micro', pos_label='1'))

        f1_score=metrics.f1_score(y_test, predicted6, average='micro',pos_label='1')
        print("F1 score of DecisionTreeClassifier IS ->")
        print(metrics.f1_score(y_test, predicted6, average='micro',pos_label='1'))
        print('---------------------------------------------- ')
        val2 = (str("DTC"),float(dt),float(precision), float(recall), float(f1_score))
        cursor.execute(query2, val2)

        print("[INFO] SVM Processing")
        del_query = "DELETE FROM performance WHERE Algorithm = 'SVM'"
        cursor.execute(del_query)
        classify6 = LinearSVC()
        classify6.fit(x_train, y_train)
        predicted6 = classify6.predict(x_test)
        svm = metrics.accuracy_score(y_test, predicted6) * 100
        print("The accuracy score using the SVM is ->")
        print(metrics.accuracy_score(y_test, predicted6))

        precision = metrics.precision_score(y_test, predicted6, average='micro', pos_label='1')
        print("Precision score of SVM IS ->")
        print(metrics.precision_score(y_test, predicted6, average='micro', pos_label='1'))

        recall = metrics.recall_score(y_test, predicted6, average='micro', pos_label='1')
        print("Recall score of SVM IS ->")
        print(metrics.recall_score(y_test, predicted6, average='micro', pos_label='1'))

        f1_score = metrics.f1_score(y_test, predicted6, average='micro', pos_label='1')
        print("F1 score of  SVM IS ->")
        print(metrics.f1_score(y_test, predicted6, average='micro', pos_label='1'))
        print('---------------------------------------------- ')
        val3 = (str("SVM"),str(svm),str(precision),str(recall),str(f1_score))
        cursor.execute(query2,val3)
        mydb.commit()
        cursor.close()
        mydb.close()

        list = []
        list.clear()
        list.append(gnb)
        list.append(dt)
        list.append(svm)

        view(list)
    except Exception as e:
        print("error"+e.args[1])
        tb = sys.exc_info()[2]
        print("no",tb.tb_lineno)






