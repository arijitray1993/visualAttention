import pandas as pd
import numpy as np
import scipy
from sklearn import mixture

df=pd.read_pickle("visualAttention_oct30.pkl")

execfile("scri.py")

uniquetypes=list(set(df['question_type']))

chosen_type=df['question_type'][0]

i=0

g=mixture.GMM(n_components=1)
mean_covars=0

for types in df['question_type']:
	if types==chosen_type:
		points=[xcor[i],ycor[i]]
		points=np.asarray(points)
		points=points.T

		gaussian=g.fit(points)

		print(gaussian.means_)
		print(gaussian.covars_)
		mean_covars=mean_covars+gaussian.covars_
	i=i+1

mean_covars=mean_covars/(i-1)

print mean_covars



