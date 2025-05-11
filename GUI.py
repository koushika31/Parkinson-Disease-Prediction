
from tkinter import *
import os
from tkinter import filedialog
import cv2

from tkinter import messagebox





def file_sucess():
    global file_success_screen
    file_success_screen = Toplevel(training_screen)
    file_success_screen.title("File Upload Success")
    file_success_screen.geometry("150x100")

    Label(file_success_screen, text="File Upload Success").pack()
    Button(file_success_screen, text='''ok''', font=(
        'Palatino Linotype', 15), height="2", width="30").pack()


global ttype

def training():
    global training_screen

    global clicked

    training_screen = Toplevel(main_screen)
    training_screen.title("Training")
    # login_screen.geometry("400x300")
    training_screen.geometry("600x450+650+150")
    training_screen.minsize(120, 1)
    training_screen.maxsize(1604, 881)
    training_screen.resizable(1, 1)
    training_screen.configure()
    # login_screen.title("New Toplevel")



    Label(training_screen, text='''Upload Image ''',
          foreground="#000000",  width="300", height="2", font=("Palatino Linotype", 16)).pack()
    Label(training_screen, text="").pack()


    options = [
        "Healthy",
        "Parkinson"
    ]

    # datatype of menu text
    clicked = StringVar()


    # initial menu text
    clicked.set("Healthy")

    # Create Dropdown menu
    drop = OptionMenu(training_screen, clicked, *options )
    drop.config(width="30")

    drop.pack()

    ttype=clicked.get()

    Button(training_screen, text='''Upload Image''', font=(
        'Palatino Linotype', 15), height="2", width="30", command=imgtraining).pack()




def imgtraining():
    name1 = clicked.get()

    print(name1)

    import_file_path = filedialog.askopenfilename()
    import os
    s = import_file_path
    os.path.split(s)
    os.path.split(s)[1]
    splname = os.path.split(s)[1]


    image = cv2.imread(import_file_path)
    #filename = 'Test.jpg'
    filename = 'Train/'+name1+'/'+splname


    cv2.imwrite(filename, image)
    print("After saving image:")
    image = cv2.resize(image, (780, 540))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



    cv2.imshow('Original image', image )
    cv2.imshow('Gray image', gray)
    # import_file_path = filedialog.askopenfilename()
    print(import_file_path)
    fnm = os.path.basename(import_file_path)
    print(os.path.basename(import_file_path))

    from PIL import Image, ImageOps

    im = Image.open(import_file_path)


    im_invert = ImageOps.invert(im)
    im_invert.save('lena_invert.jpg', quality=95)
    im = Image.open(import_file_path).convert('RGB')

    im_invert = ImageOps.invert(im)
    im_invert.save('tt.png')
    image2 = cv2.imread('tt.png')
    image2 = cv2.resize(image2, (780, 540))
    cv2.imshow("Invert", image2)

    """"-----------------------------------------------"""

    img = image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original image', img)

    dst = cv2.medianBlur(img, 7)
    cv2.imshow("Noise Removal", dst)




def fulltraining():
    import Model as mm







def testing():
    global testing_screen
    testing_screen = Toplevel(main_screen)
    testing_screen.title("Testing")
    # login_screen.geometry("400x300")
    testing_screen.geometry("600x450+650+150")
    testing_screen.minsize(120, 1)
    testing_screen.maxsize(1604, 881)
    testing_screen.resizable(1, 1)
    testing_screen.configure()
    # login_screen.title("New Toplevel")

    Label(testing_screen, text='''Upload Image''',  width="300", height="2", font=("Palatino Linotype", 16)).pack()
    Label(testing_screen, text="").pack()
    Label(testing_screen, text="").pack()
    Label(testing_screen, text="").pack()
    Button(testing_screen, text='''Upload Image''', font=(
        'Palatino Linotype', 15), height="2", width="30", command=imgtest).pack()

def imgtest():


    import_file_path = filedialog.askopenfilename()

    image = cv2.imread(import_file_path)
    print(import_file_path)
    filename = 'Output/Out/Test.jpg'
    cv2.imwrite(filename, image)
    print("After saving image:")
    #result()

    #import_file_path = filedialog.askopenfilename()
    print(import_file_path)
    fnm = os.path.basename(import_file_path)
    print(os.path.basename(import_file_path))

   # file_sucess()

    print("\n*********************\nImage : " + fnm + "\n*********************")
    img = cv2.imread(import_file_path)
    if img is None:
        print('no data')

    img1 = cv2.imread(import_file_path)
    print(img.shape)
    img = cv2.resize(img, ((int)(img.shape[1] / 5), (int)(img.shape[0] / 5)))
    original = img.copy()
    neworiginal = img.copy()
    img1 = cv2.resize(img1, (400, 400))

    img1S = cv2.resize(img1, (400, 400))

    cv2.imshow('Original image', img1S)

    dst = cv2.fastNlMeansDenoisingColored(img1, None, 10, 10, 7, 21)
    dst = cv2.resize(dst, (400, 400))
    cv2.imshow("Noise Removal", dst)
    result()




def result():
    import warnings
    warnings.filterwarnings('ignore')

    import tensorflow as tf
    classifierLoad = tf.keras.models.load_model('pdmodel.h5')

    import numpy as np
    from keras.preprocessing import image
    test_image = image.load_img('./Output/Out/Test.jpg', target_size=(200, 200))
    # test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifierLoad.predict(test_image)


    out = ''
    if result[0][0] == 1:
        print("Healthy")
        out="Healthy"

        messagebox.showinfo("Result", 'Healthy')


    elif result[0][1] == 1:
        print("Parkinson")
        out="Parkinson"
        messagebox.showinfo("Result", 'Parkinson')
        messagebox.showinfo("Prescription", 'Levodopa, the most effective Parkinson disease medication, is a natural chemical that passes into your brain and is converted to dopamine.')









def main_account_screen():
    global main_screen
    main_screen = Tk()
    width = 600
    height = 500
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    main_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    main_screen.resizable(0, 0)
    # main_screen.geometry("300x250")
    main_screen.configure()
    main_screen.title("Parkinson Detection")

    Label(text="Parkinson Detection ", width="300", height="5", font=("Palatino Linotype", 16)).pack()

    Button(text="UploadImage", font=(
        'Palatino Linotype', 15), height="2", width="20", command=training, highlightcolor="black").pack(side=TOP)
    Label(text="").pack()
    Button(text="Training", font=(
        'Palatino Linotype', 15), height="2", width="20", command=fulltraining, highlightcolor="black").pack(side=TOP)
    Label(text="").pack()
    Button(text="Testing", font=(
        'Palatino Linotype', 15), height="2", width="20", command=testing).pack(side=TOP)
    Label(text="").pack()


    main_screen.mainloop()


main_account_screen()

