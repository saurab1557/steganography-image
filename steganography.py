import cv2
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import ttk
import string


def savef():
    window.destroy()
    global top3
    top3 = Toplevel()
    top3.title("Stegpixel")
    top3.configure(background="#D2386C")
    wv = top3.winfo_screenwidth()
    hv = top3.winfo_screenheight()
    top3.geometry("%dx%d" % (wv, hv))
    key_info = keyyy.get()
    text_info = texttt.get()

    file = open("steg_info" + ".txt", 'w')
    file.write(key_info)
    file.close()
    file2 = open("txt_info" + ".txt", 'w')
    file2.write(text_info)
    file2.close()

    label1 = Label(top3, text="Your information has been saved", font=('bold', 18), pady=10, background="#D2386C",
                   fg="#FFFFFF").pack()
    Label2 = Label(top3, text="Click the button below to choose a picture to hide your information in",
                   font=('bold', 15), pady=5, background="#D2386C", fg="#FFFFFF").pack()
    Bttn = Button(top3, text="Browse", font=('bold', 10), width=15, bg='#EE58A8', command=p21).pack()


def main1():
    global window, keyyy, texttt
    window = Tk()
    wv = window.winfo_screenwidth()
    hv = window.winfo_screenheight()
    window.geometry("%dx%d" % (wv, hv))
    window.title("Stegpixel")
    window.configure(background="#D2386C")
    kll = Label(window, text=("Hello and Welcome to"), font=('bold', 30), pady=20, background="#D2386C", fg="#FFFFFF").pack()

    kll = Label(window, text=("Stegpixel"), font=('bold', 40), pady=20, background="#D2386C", fg="#FFFFFF").pack()
    kll = Label(window, text=("Let's get started"), font=('bold', 30), pady=20, background="#D2386C", fg="#FFFFFF").pack()
    kll = Label(window, text=("Fill in the details below"), font=('bold', 20), pady=15,
                background="#D2386C",
                fg="#FFFFFF").pack()
    kl = Label(window, text="Enter your security key : ", font=('bold', 20), pady=20, background="#D2386C",
               fg="#FFFFFF")
    kl.pack()

    keyyy = Entry(window, width=40)
    keyyy.pack()

    tl = Label(window, text="Enter your secret text to hide : ", font=('bold', 20), pady=20, background="#D2386C",
               fg="#FFFFFF")
    tl.pack()
    texttt = Entry(window, width=40)
    texttt.pack()
    kl2 = Label(window, text="", pady=20, background="#D2386C", fg="#FFFFFF").pack()
    B1 = Button(window, text="Save", font=('bold', 10), width=15, bg='#EE58A8', command=savef)
    B1.pack()


window1 = Tk()
wv = window1.winfo_screenwidth()
hv = window1.winfo_screenheight()
window1.geometry("%dx%d" % (wv, hv))
window1.title("Stegpixel")
window1.configure(background="#D2386C")
kll = Label(window1, text=("Welcome"), font=('bold', 50), pady=20, background="#D2386C", fg="#FFFFFF").pack()
kll = Label(window1, text=("To"), font=('bold', 30), pady=20, background="#D2386C", fg="#FFFFFF").pack()
kll = Label(window1, text=("Stegpixel"), font=('bold', 50), pady=20, background="#D2386C", fg="#FFFFFF").pack()
kll = Label(window1, text=("Click the button below to get started"), font=('bold', 20), pady=20, background="#D2386C", fg="#FFFFFF").pack()
B2 = Button(window1, text="Start", font=('bold', 10), width=15, bg='#EE58A8', command=main1).pack()


def p21():
    top3.destroy()
    global imgf, f1, top4
    f1 = filedialog.askopenfilename(initialdir="C:/Users", title="Choose your picture",
                                    filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    top4 = Toplevel()
    wv = top4.winfo_screenwidth()
    hv = top4.winfo_screenheight()
    top4.geometry("%dx%d" % (wv, hv))
    top4.title("Stegpixel")
    top4.configure(background="#D2386C")
    imgf = ImageTk.PhotoImage(Image.open(f1))

    kll = Label(top4, text=("Are you sure you want to hide your information in this picture?"), font=('bold', 15),
                pady=20, background="#D2386C", fg="#FFFFFF").pack()

    imgl = Label(top4, image=imgf, font=('bold', 17), pady=40, background="#D2386C", fg="#FFFFFF").pack()
    kll = Label(top4, text=("If yes, click the button below"), font=('bold', 15), pady=15, background="#D2386C",
                fg="#FFFFFF").pack()

    imgb1 = Button(top4, text="Hide", font=('bold', 10), width=15, bg='#EE58A8', command=btn3).pack()
    kll = Label(top4, text=("If not choose your picture again"), font=('bold', 15), pady=15, background="#D2386C",
                fg="#FFFFFF").pack()
    Bttn = Button(top4, text="Browse", font=('bold', 10), width=15, bg='#EE58A8', command=p21).pack()


def btn3():
    top4.destroy()
    global d, c, x, l, top1

    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)
    x = cv2.imread(f1)

    i = x.shape[0]
    j = x.shape[1]

    key = keyyy.get()
    text = texttt.get()

    kl = 0

    z = 0
    n = 0
    m = 0

    l = len(text)

    for i in range(l):
        x[n, m, z] = d[text[i]] ^ d[key[kl]]
        n = n + 1
        m = m + 1
        m = (
                    m + 1) % 3
        kl = (kl + 1) % len(key)

    cv2.imwrite("New_img.jpg", x)
    top1 = Toplevel()
    wv = top1.winfo_screenwidth()
    hv = top1.winfo_screenheight()
    top1.geometry("%dx%d" % (wv, hv))
    top1.title("Stegpixel")
    top1.configure(background="#D2386C")
    ll = Label(top1, text="The information was hidden successfully", font=('bold', 18), pady=20, background="#D2386C",
               fg="#FFFFFF").pack()
    ll = Label(top1, text="The information was hidden in the following encrypted format:", font=('bold', 15), pady=15,
               background="#D2386C",
               fg="#FFFFFF").pack()

    fr = ttk.Frame(top1)
    fr.pack()

    lst = Text(fr, width=30)

    lst.insert(END, x)
    lst.pack()

    ll1 = Label(top1, text="Click here to extract your hidden data", font=('bold', 15), pady=20, background="#D2386C",
                fg="#FFFFFF").pack()
    bt1 = Button(top1, text="Extract", font=('bold', 10), width=15, bg='#EE58A8', command=ex1).pack()
    ll2 = Label(top1, text="Click here to exit the program", font=('bold', 15), pady=20, background="#D2386C",
                fg="#FFFFFF").pack()
    bt2 = Button(top1, text="Exit", font=('bold', 10), width=15, bg='#EE58A8', command=ext).pack()


def ext():
    exit()


def ex1():
    top1.destroy()
    global key2, top2
    key = keyyy.get()
    top2 = Toplevel()
    wv = top2.winfo_screenwidth()
    hv = top2.winfo_screenheight()
    top2.geometry("%dx%d" % (wv, hv))
    top2.title("Stegpixel")
    top2.configure(background="#D2386C")

    lbb = Label(top2, text="Type the Security key below:", font=('bold', 15), pady=20, background="#D2386C",
                fg="#FFFFFF").pack()
    key2 = Entry(top2).pack()
    lbb = Label(top2, text="", font=('bold', 15), pady=20, background="#D2386C",
                fg="#FFFFFF").pack()
    bttt = Button(top2, text="Go", font=('bold', 10), width=15, bg='#EE58A8', command=dec).pack()


def dec2():
    ley = key2.get()
    ley2 = keyyy.get()
    if ley2 == ley:
        dec()
    else:
        print("n")


def dec():
    try:
        key = keyyy.get()

        kl = 0

        z = 0
        n = 0
        m = 0

        decrypt = ""

        for i in range(l):
            decrypt += c[x[n, m, z] ^ d[key[kl]]]
            n = n + 1
            m = m + 1
            m = (m + 1) % 3
            kl = (kl + 1) % len(key)
        lbb1 = Label(top2, text="Hidden text is :", font=('bold', 15), pady=20, background="#D2386C",
                     fg="#FFFFFF").pack()
        fr = ttk.Frame(top2)
        fr.pack()

        lst = Text(fr, width=30)

        lst.insert(END, decrypt)
        lst.pack()

    except ValueError:
        lbb1 = Label(top2, text="There was an error processing your request", font=('bold', 15), pady=20, background="#D2386C",
                     fg="#FFFFFF").pack()


window1.mainloop()