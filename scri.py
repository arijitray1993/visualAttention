import numpy
k = 0;
j = 0;
p = 0;
ycor = numpy.zeros((60000,10000), dtype = int)
xcor = numpy.zeros((60000,10000), dtype = int)

while df ['saliencyMap'][k] != "":
	j = 0;
	p = 0;
        for i in df ['saliencyMap'][k]:
		j = j+1;
                if i == 'x':
			if df['saliencyMap'][k][j+3] == 'n':
				xcor[k][p] =  0;
                        elif df['saliencyMap'][k][j+4] == '}' or df['saliencyMap'][k][j+4] == '.':
                                xcor[k][p] = df['saliencyMap'][k][j+3] ;
                        elif df['saliencyMap'][k][j+5] == '}' or df['saliencyMap'][k][j+5] == '.':
                                xcor[k][p] = df['saliencyMap'][k][j+3] +df['saliencyMap'][k][j+4];
                        else:
                                xcor[k][p] = df['saliencyMap'][k][j+3] +df['saliencyMap'][k][j+4] + df['saliencyMap'][k][j+5]
			p= p+1;
                if i == 'y':
                        if df['saliencyMap'][k][j+3] == 'n':
                                ycor[k][p] =  0;
                        elif df['saliencyMap'][k][j+4] == ',' or df['saliencyMap'][k][j+4] == '.':
                                ycor[k][p] = df['saliencyMap'][k][j+3];
                        elif df['saliencyMap'][k][j+5] == ',' or df['saliencyMap'][k][j+5] == '.':
                                ycor[k][p] = df['saliencyMap'][k][j+3] +df['saliencyMap'][k][j+4];
                        else:
                                ycor[k][p] = df['saliencyMap'][k][j+3] +df['saliencyMap'][k][j+4] + df['saliencyMap'][k][j+5]       

	if k == 7227:
		k = k+2;
	else:
		k = k+1;


