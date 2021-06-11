from sklearn.decomposition import PCA
import gensim.models.keyedvectors as word2vec
from matplotlib import pyplot

def createPCA(model, labelSets,groups="a"):
    # Create X
    i = 0
    all_data = []
    for labels in labelSets:
        data = []
        all_labels = list(model.index_to_key)
        newLabels = []
        for label in labels:
            if label in all_labels:
                data.append(model[label.lower()])
                newLabels.append(label)
        labelSets[i] = newLabels
        all_data.append(data)
        i = i + 1

    markers = ["o", "s", "P", "*", "+", "x", "d", "2"]
    pca = PCA(n_components=2)

    i = 0
    for data in all_data:
        result = pca.fit_transform(data)
        pyplot.legend(loc='upper right')
        pyplot.scatter(result[:, 0], result[:, 1], marker=(markers[i]), label=(groups[i]))
        if len(labelSets[i]) < 35:
            for j, word in enumerate(labelSets[i]):
                pyplot.annotate(word, xy=(result[j, 0], result[j, 1]))
        i += 1
    pyplot.show()

model = word2vec.KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)
print("Model Loaded")
words = [["man","woman","king","queen","gentleman","lady"]]


createPCA(model, words)

print(m)