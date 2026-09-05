#!/bin/bash
set -e

mkdir -p data models

curl -sL "https://raw.githubusercontent.com/mohitgupta-1O1/Kaggle-SMS-Spam-Collection-Dataset-/master/spam.csv" -o data/spam.csv

python3 scripts/explore_data.py
python3 scripts/train_model.py