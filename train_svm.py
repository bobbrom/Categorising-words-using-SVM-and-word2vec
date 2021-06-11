from sklearn import svm
import glob
import pickle
import gensim.models.keyedvectors as word2vec
import time

wv = word2vec.KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)

files = glob.glob("training/*.txt")

catagories = [f.split("\\")[-1].replace(".txt","") for f in files]

print(catagories)
for cat in catagories:

    data = []
    labels = []

    i = 0
    oldPerc = -1
    oldT = time.time()

    clf = svm.SVC(kernel='linear')
    for file in files:
        f = open(file, "r")
        words = f.read().split("\n")

        f.close()
        if 'training\\'+cat+'.txt' == file:
            print(cat.upper())
            for w in words:
                try:
                    data.append(wv.get_vector(w))
                    labels.append(cat)
                except Exception as e:
                    a = 2
        else:
            print("NOT "+cat.upper())
            for w in words:
                try:
                    data.append(wv.get_vector(w))
                    labels.append("not_"+cat)
                except Exception as e:
                    a = 2

    clf.fit(data, labels)

    with open("svm_models/"+cat+".svm", "wb") as file:
        pickle.dump(clf, file)
    print(cat+".svm - Done")