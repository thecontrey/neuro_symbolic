"""
Minimal PDL-style baseline skeleton.
The paper reports aggregate PDL results; this script shows the intended
feature-based classifier interface without raw confidential documents.
"""
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score

def train_pdl_classifier(X, y):
    clf = LogisticRegression(max_iter=1000, multi_class="auto", penalty="l2")
    cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    scores = cross_val_score(clf, X, y, cv=cv, scoring="accuracy")
    clf.fit(X, y)
    return clf, scores
