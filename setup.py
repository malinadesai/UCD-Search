
#imports

# std lib
from setuptools import setup
import subprocess
import sys
import os
from getpass import getpass
import numpy as np
import pylab as plt
import matplotlib
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.lines as mlines
import matplotlib.style
import matplotlib as mpl
import pandas as pd
from numpy.polynomial import polynomial as P

# Data Lab
from dl import authClient as ac, queryClient as qc, storeClient as sc

# machine learning
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, classification_report, \
PrecisionRecallDisplay, RocCurveDisplay, f1_score, recall_score, plot_confusion_matrix
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split, KFold,RepeatedKFold, GridSearchCV, RandomizedSearchCV
from sklearn.calibration import calibration_curve

# others
from dl.helpers.utils import convert
import warnings
from pathlib import Path
from typing import Iterable, List, Optional, Union

