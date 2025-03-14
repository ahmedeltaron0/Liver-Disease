import tensorflow as tf
print("TensorFlow is working fine!")
print("Num GPUs Available:", len(tf.config.experimental.list_physical_devices('GPU')))
