import re 
from nltk.corpus import stopwords
stop=stopwords.words('english')

def clean(t):
    t=t.lower()
    t=re.sub(r'[^a-zA-Z\s]','',t)
    t=re.sub(r'\s+',' ',t).strip()
    words=t.split()
    new=[word for word in words if word not in stop]
    return  ' '.join(new)


