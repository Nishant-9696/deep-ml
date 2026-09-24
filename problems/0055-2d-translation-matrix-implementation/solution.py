import numpy as np
def translate_object(points, tx, ty):
	points=np.asarray(points)
	result=[]
	for i in range(len(points)):
		x=points[i][0]
		y=points[i][1]
		result.append([x+tx,y+ty])
	return result


	
