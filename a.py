import numpy as np
import matplotlib.pyplot as plt

test_acc=np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8])
train_acc=np.array([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])

x_axis = list(range(len(test_acc)))
plt.plot(x_axis, train_acc, 'b-', label='Train Acc.')
plt.plot(x_axis, test_acc, 'r-', label='Test Acc.')
plt.title('Train & Test Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()