from predict import load_img

def classify_img():
    print('是否对图片进行分类[y/n]:')
    res = input()
    if res == 'y':
        load_img('.././wallpaper')
    elif res == 'n':
        print('程序正常退出！')
    else:
        print("请输入'y'或者'n'!")
        classify_img() # 递归调用

    return
