import matplotlib.pyplot as plt
x_value=list(range(1,5001))
y_value=[x**3 for x in x_value]
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,edgecolor='none',s=40)
plt.title('Square Number',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)
plt.plot(x_value,y_value,linewidth=5)
plt.axis([0,5500,0,150000000000])
plt.show()
plt.save('threetimes_of_values.png',bbox_inches='tight')
