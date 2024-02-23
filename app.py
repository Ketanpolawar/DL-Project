import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
model = load_model('')

img=''

image = 'Ketanpolawar/Deep-Learning-Foundations/Banana-Single.jpg'
image =tf.keras.utils.load_img(image,target_size=(img_height,img_width))
img_arr = tf.keras.utils.array_to_img(image)
img_bat=tf.expand_dims(img_arr,0)