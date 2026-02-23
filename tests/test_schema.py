import sys
import os
sys.path.append(os.path.abspath("src"))

from preprocess import load_and_clean, validate_schema

def test_schema_validation():
    df = load_and_clean("data/raw/ES_quant_buy_sma10.csv")
    assert validate_schema(df)