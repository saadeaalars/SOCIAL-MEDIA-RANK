# toxic_checker.py
from detoxify import Detoxify

def check_toxicity(text):
    result = Detoxify('original').predict(text)
return result