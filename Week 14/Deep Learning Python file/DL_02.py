import tensorflow as tf
import numpy as np

dataset = tf.data.Dataset.range(10)
dataset = dataset.window(5, shift=1, drop_remainder=True)
print(dataset)
# for window_dataset in dataset:
#	for val in window_dataset:
#		print(val.numpy(), end=" ")
#	print()

dataset = dataset.flat_map(lambda window:window.batch(5))
# for window in dataset:
#	print(window.numpy())

dataset = dataset.map(lambda window: (window[:-1], window[-1:]))
dataset = dataset.shuffle(buffer_size=10)
dataset = dataset.batch(2).prefetch(1)
for x,y in dataset:
#   print(x.numpy(), y.numpy())
    print("x = ", x.numpy())
    print("y = ", y.numpy())
