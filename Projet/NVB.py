
import pickle



with open(r'C:\Users\Pc\Desktop\mysite\src2\training\trainNVB.model','rb') as f :
     classifier=pickle.load(f)

with open(r'C:\Users\Pc\Desktop\mysite\src2\training\vectNVB.pickle','rb') as l :
     vectorizer=pickle.load(l)


def test_to_category(title):

    categories = {'b' : 'business',
                  't' : 'science and technology',
                  'e' : 'entertainment',
                  'm' : 'health'}
    pridicter = classifier.predict(vectorizer.transform([title]))
    return categories[pridicter[0]]


import sys
output = (sys.argv[1])
print(test_to_category(output))
