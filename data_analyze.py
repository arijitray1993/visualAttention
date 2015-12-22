import pandas as pd
import base64
from PIL import Image
from io import BytesIO

df=pd.read_pickle('visualAttention_oct30.pkl')

for keys in df:
	print keys

unique_types=list(set(question_type))
for types in unique_types:
	


