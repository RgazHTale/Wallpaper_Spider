import os, sys
from PIL import Image
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD, RMSprop, Adam
from keras.layers import Conv2D, MaxPooling2D
import shutil

def prepicture(picname):
    img = Image.open('.././wallpaper/' + picname)
    new_img = img.resize((100, 100), Image.BILINEAR)
    new_img.save(os.path.join('./load_img/', os.path.basename(picname)))

def read_image2(filename):
    img = Image.open('./load_img/'+filename).convert('RGB')
    return np.array(img)

def start_predict(filename):
    '''对图片的种类进行预测'''

    # 加载预测图片
    prepicture(filename)
    x_test = []

    x_test.append(read_image2(filename))

    x_test = np.array(x_test)

    x_test = x_test.astype('float32')
    x_test /= 255

    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    # 共有两种类型
    model.add(Dense(2, activation='softmax'))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    model.load_weights('./wallpaper_weights.h5')
    classes = model.predict_classes(x_test)[0]

    # 清理掉load_img文件夹中的图片
    os.remove(f'./load_img/{filename}')

    return classes

def load_img(filepath):
    '''加载预测的图片'''
    images = os.listdir(filepath)
    print('加载图片......')
    for name in images:
        classes = start_predict(name)
        if classes == 0:
            shutil.move(f".././wallpaper/{name}", ".././wallpaper_classify/人物/")
        elif classes == 1:
            shutil.move(f".././wallpaper/{name}", ".././wallpaper_classify/其它/")

    print('分类完毕，程序正常退出！')

    return
