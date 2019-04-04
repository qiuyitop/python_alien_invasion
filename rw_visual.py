import matplotlib.pyplot as plt 
from random_walk import RandomWalk 
while True:
	rw=RandomWalk()
	rw.fill_walk()
	point_numbers=list(range(rw.num_points))
	plt.scatter(rw.x_value,rw.y_value,c=point_numbers,cmap=plt.cm.Reds,edgecolor='none',s=1)
	plt.scatter(0,0,c='green',edgecolor='none',s=100)
	plt.scatter(rw.x_value[-1],rw.y_value[-1],c='blue',edgecolor='none',s=100)
	#yingcangzuobianzhou
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()
	