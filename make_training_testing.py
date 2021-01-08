import random
import glob

files = glob.glob("all_words/*.txt")

a = [1,2,3,4,5,6,7]

# print(a[0:3])
for file in files:
    f = open(file, "r")
    arr = f.read().split("\n")
    f.close()
    l = len(arr)
    random.shuffle(arr)
    train = arr[0:int(l*0.8)]
    test = arr[int(l*0.8):]

    f_train = open("training/"+file,"w+")
    for w in train:
        f_train.write(w+"\n")
    f_train.close()

    f_test = open("testing/"+file,"w+")
    for w in test:
        f_test.write(w+"\n")
    f_test.close()

