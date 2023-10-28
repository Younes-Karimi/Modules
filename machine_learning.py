__author__ = "Younes Karimi"
__email__ = "younes@psu.edu"
__description__ = "This file contains basic machine learning functions and metric calculators"

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC
import numpy as np
from sklearn import svm
import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings(action='ignore', category=ConvergenceWarning)

def metrics_calc(tn, fp, fn, tp):
    cm = [int(tn), int(fp), int(fn), int(tp)]
    recall = 0.0 if (tp+fn == 0) else float(format(tp/(tp+fn), '.4f'))
    tpr = recall
    tnr = 0.0 if (tn+fp == 0) else float(format(tn/(tn+fp), '.4f'))
    fpr = 0.0 if (fp+tn == 0) else float(format(fp/(fp+tn), '.4f'))
    fnr = 0.0 if (fn+tp == 0) else float(format(fn/(fn+tp), '.4f'))
    accuracy = float(format((tp+tn)/(tn+fp+fn+tp), '.4f'))
    precision = 0.0 if (tp+fp == 0) else float(format(tp/(tp+fp), '.4f'))
    f1 = 0.0 if (precision+recall == 0.0) else \
                float(format((2*precision*recall)/(precision+recall), '.4f'))
    print('tn, fp, fn, tp: ', cm)
    print('tpr: ', tpr)
    print('tnr: ', tnr)
    print('fpr: ', fpr)
    print('fnr: ', fnr)
    print('accuracy: ', accuracy)
    print('precision: ', precision)
    print('recall: ', recall)
    print('f1: ', f1)
    return cm, tpr, tnr, fpr, fnr, accuracy, precision, recall, f1

def classifier(features, labels, n_splits=10, model=None, clf=None, random_state=0):
  X = np.array(features)
  y = np.array(labels)
  gtn, gfp, gfn, gtp = 0, 0, 0, 0
  skf = StratifiedKFold(n_splits=n_splits)
  if clf is None:
    if model == 'rbf':
      clf = svm.SVC(kernel='rbf', C=1, random_state=random_state)
    else:
      clf = LinearSVC(random_state=random_state, tol=1e-5, max_iter=1000)
  for train_index, test_index in skf.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    clf.fit(X_train, y_train)
    pred_classes = clf.predict(X_test)
    tn, fp, fn, tp = confusion_matrix(y_test, pred_classes).ravel()
    gtn += tn
    gfp += fp
    gfn += fn
    gtp += tp 
  gtn = gtn / n_splits
  gfp = gfp / n_splits
  gfn = gfn / n_splits
  gtp = gtp / n_splits
  return metrics_calc(gtn, gfp, gfn, gtp)