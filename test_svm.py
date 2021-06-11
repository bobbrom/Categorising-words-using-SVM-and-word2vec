from sklearn import svm
import glob
import gensim.models.keyedvectors as word2vec
import pickle
import time

wv = word2vec.KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)
print("Model Loaded")
files = glob.glob("testing/*.txt")


results = dict()

catagories = [f.split("\\")[-1].replace(".txt","") for f in files]
for cat in catagories:
    print(cat)

    TP = 0
    FP = 0
    TN = 0
    FN = 0

    clf = pickle.load(open("svm_models/"+cat+".svm", "rb"))
    for file in files:
        if 'testing\\'+cat+'.txt' == file:
            label = cat
        else:
            label = "not_"+cat
        f = open(file,"r")
        words = f.read().split("\n")

        i = 0
        oldPerc = -1
        oldT = time.time()

        for word in words:
            try:
                p = clf.predict([wv.get_vector(word)])
            except Exception as e:
                continue
            if(label == cat):
                if(p == label):
                    TP += 1
                else:
                    FP += 1
            else:
                if(p == label):
                    TN += 1
                else:
                    FN += 1

            # perc = int((100 / len(words)) * i)
            # if (perc != oldPerc):
            #     t = time.time()
            #     print(str(perc) + "%", "-", str(t - oldT), "ETA:", str((t - oldT) * (100 - perc)))
            #     oldT = t
            #     oldPerc = perc
            i += 1
    d = dict()
    d["TP"] = TP
    d["FP"] = FP
    d["TN"] = TN
    d["FN"] = FN
    results[cat] =  d

for key in results.keys():
    print("---"+key+"---")
    for r in results[key].keys():
        print(r+" :",results[key][r])