# basic-tfidf

A straightforward use of scikit-learn TfidfVectorizer to determine important word phrases in a particular document of a corpus.

If necessary, install the following:

```
pip install --user numpy scipy
pip install -U scikit-learn
```
Now, download the repository, and place the corpus as separate .txt files in the same folder.  Name the document whose important phrases you care about as "script.txt"

Then, in a terminal, enter the python environment and call:

```
from important_words import scores
scores(50)
```
