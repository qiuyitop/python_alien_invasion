import matplotlib.pyplot as plt 
from random_walk import RandomWalk 
while True:
	rw=RandomWalk(50000)
	rw.fill_walk()
	point_numbers=list(range(rw.num_points))
	plt.plot(rw.x_value,rw.y_value,linewidth=1)
	
	#yingcangzuobianzhou
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()