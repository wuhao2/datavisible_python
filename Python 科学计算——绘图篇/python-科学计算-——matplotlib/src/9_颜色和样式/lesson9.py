import numpy as np
import matplotlib.pyplot as plt

#Ĭ�����
y=np.arange(1,5)
plt.plot(y)
plt.show()

'''
#������ɫ
y=np.arange(1,5)
plt.plot(y,'y');
plt.plot(y+1,color=(0.1,0.2,0.3));
plt.plot(y+2,'#FF00FF');
plt.plot(y+3,color='0.5')

plt.show()
'''

'''
#����

y=np.arange(1,5)
plt.plot(y,'--');
plt.plot(y+1,'-.');
plt.plot(y+2,':');

plt.show()

'''
#����״

'''
y=np.arange(1,5)
plt.plot(y,'o');
plt.plot(y+1,'D');
plt.plot(y+2,'^');
plt.plot(y+3,'s');
plt.plot(y+4,'p');
plt.plot(y+5,'x');

plt.show()
'''

y=np.arange(1,5)
plt.plot(y,'cx--');
plt.plot(y+1,'kp:');
plt.plot(y+2,'mo-.');

plt.show()

