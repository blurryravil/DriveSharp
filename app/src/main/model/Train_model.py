from keras.models import Sequential
from keras.layers import Dense,Dropout,Conv2D,MaxPooling2D,Flatten
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import os

BATCH_SIZE = 16

train = ImageDataGenerator(rescale=1/255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
validation = ImageDataGenerator(rescale=1/255)

train_datagen = ImageDataGenerator(rescale = 1./255, rotation_range = 0.2,shear_range = 0.2,
    zoom_range = 0.2,width_shift_range = 0.2,
    height_shift_range = 0.2, validation_split = 0.2)

train_data= train_datagen.flow_from_directory(os.path.join('mrlEyes_2018_01', 'data', 'train'),
                                target_size = (80,80), batch_size = BATCH_SIZE, 
                                class_mode = 'categorical',subset='training' )

test_datagen = ImageDataGenerator(rescale = 1./255)

test_data = test_datagen.flow_from_directory(os.path.join('mrlEyes_2018_01', 'data', 'test'),
                                target_size=(80,80), batch_size = BATCH_SIZE, class_mode='categorical')

batch_size=32
SPE= len(train_datagen.classes)//batch_size 
VS = len(test_datagen.classes)//batch_size 
print(SPE,VS)

print(train_datagen.class_indices)

model = Sequential()
model.add(Conv2D(64,(3,3),input_shape=(100,100,1),activation="relu"))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(32,(3,3),activation="relu"))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(32,(3,3),activation="relu"))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(16,(3,3),activation="relu"))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(16,(3,3),activation="relu"))
model.add(MaxPooling2D((2,2)))

model.add(Flatten())
model.add(Dropout(0.5))

model.add(Dense(128,activation="relu"))
model.add(Dropout(0.2))

model.add(Dense(64,activation="relu"))
model.add(Dropout(0.2))

model.add(Dense(1,activation='sigmoid'))

model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])

results = model.fit_generator(train_datagen,validation_data=test_datagen,epochs=10,steps_per_epoch=SPE,validation_steps=VS)

model.save("CNN__model.h5")

lite_model = tf.keras.models.load_model('CNN__model.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(lite_model)
tflmodel = converter.convert()
file = open( 'model.tflite' , 'wb' ) 
file.write( tflmodel )
