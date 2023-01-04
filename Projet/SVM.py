
import pickle

with open(r'C:\Users\Pc\Desktop\mysite\src2\training\trainSVM.model','rb') as f :
     classifier=pickle.load(f)

with open(r'C:\Users\Pc\Desktop\mysite\src2\training\vectSVM.pickle','rb') as l :
     vectorizer=pickle.load(l)




def test_to_category(txt):

    categories = {'b' : 'business',
                  't' : 'science and technology',
                  'e' : 'entertainment',
                  'm' : 'health'}
    pridicter = classifier.predict(vectorizer.transform([txt]))
    return categories[pridicter[0]]


import sys
output = (sys.argv[1])
print(test_to_category(output))
