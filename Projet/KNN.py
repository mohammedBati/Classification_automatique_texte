
import pickle

with open(r'C:\Users\Pc\Desktop\mysite\src2\training\trainKNN.model','rb') as f :
     classifier=pickle.load(f)

with open(r'C:\Users\Pc\Desktop\mysite\src2\training\vectKNN.pickle','rb') as l :
     vectorizer=pickle.load(l)

def test_to_category(txt):
    '''f=open(title,"r")
    l=f.read()
    f.close()
    '''

    categories = {'b' : 'business',
                  't' : 'science and technology',
                  'e' : 'entertainment',
                  'm' : 'health'}
    ve=vectorizer.transform([txt])
    pridicter = classifier.predict(ve)
    return categories[pridicter[0]]

import sys
output = (sys.argv[1])
print(test_to_category(output))
