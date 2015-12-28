import numpy as np
import array
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import mixture


qtypes = 8
que = np.zeros((qtypes, 1), dtype = int);
maxi = len(df['question_type']);
modes = np.zeros((maxi, 1), dtype = int);
def gaussianMixtureModel(x2,y2):
	siz = x2.size;
	#X = numpy.zeros((siz, 2),dtype = int);
        Y = np.concatenate((x2,y2),axis = 0)
        Y1 = Y.reshape(2, siz)
	X = Y1.T
	lowest_bic = np.infty
        bic = []
	Ra = min(6, siz);
	if Ra >= 1:
        	n_components_range = range(1, Ra)
        	cv_types = ['spherical', 'tied', 'diag', 'full']
        	for cv_type in cv_types:
        	    for n_components in n_components_range:
        	        # Fit a mixture of Gaussians with EM
        	        gmm = mixture.GMM(n_components=n_components, covariance_type=cv_type)
        	        gmm.fit(X)
        	        bic.append(gmm.bic(X))
        	        if bic[-1] < lowest_bic:
        	            lowest_bic = bic[-1]
        	            best_gmm = gmm

        	bic = np.array(bic)
        	clf = best_gmm
        	bars = []
        	return(best_gmm.n_components)
	else:
		return(1)

for j in range(0,499):

	#if a == 0 and ycor[j] == 0 : 
	if df ['question_type'][j][0] == 'h' and df ['question_type'][j][1] == 'o' :
		qu = 0;
		#r1 = r1+1;
        elif df ['question_type'][j][0] == 'w' and df ['question_type'][j][1] == 'h'and df ['question_type'][j][2] == 'i':
                qu = 1;
        elif df ['question_type'][j][0] == 'w' and df ['question_type'][j][1] == 'h'and df ['question_type'][j][2] == 'a':
                qu = 2;
        elif df ['question_type'][j][0] == 'w' and df ['question_type'][j][1] == 'h'and df ['question_type'][j][2] == 'e':
                qu = 3;
        elif df ['question_type'][j][0] == 'a' and df ['question_type'][j][1] == 'r':
                qu = 4;
        elif df ['question_type'][j][0] == 'n' and df ['question_type'][j][1] == 'o':
                qu = 5;
        elif df ['question_type'][j][0] == 'i' and df ['question_type'][j][1] == 's':
                qu = 6;
	else:
		qu = 7;
	que[qu] = que[qu] +1;
	
	if qu == 0 :
		x1 = xcor[j];
		y1 = ycor[j];
		k = -1;
		for r in x1:
			k = k+1;
			if r == 0 and x1[k+2] == 0 :
				break;
		modes[que[qu]-1] = gaussianMixtureModel(x1[0:k], y1[0:k])
					
print que





	

