from tkinter import *
import sympy
class MyWindow:
    def __init__(self, win):
        Label(win, text='1.  Generate primes p and q ').grid(row=0, column=0)
        Button(win, text='GEN',command=self.Gen).grid(row=0, column=1)
        Label(win, text='( 1000 < p, q > 5000 )').grid(row=0, column=2)
        Label(win, text='p = ').grid(row=1, column=0)
        tp = Entry(win, text='q',bd=3)
        tp.grid(row=1, column=2)
        Label(win, text='q = ').grid(row=2, column=0)
        tq = Entry(win, text='',bd=3)
        tq.grid(row=2, column=2)
        Label(win, text='2.  Compute n=pq ').grid(row=3, column=0)
        Button(win, text='Com').grid(row=3, column=1)
        Label(win, text='n = ').grid(row=4, column=0)
        Entry(win, text='',bd=3).grid(row=4, column=2)
        Label(win, text='3. Set a public key e  e = ').grid(row=5, column=0)
        Entry(win, text='',bd=3).grid(row=5, column=2)
        Label(win, text='4.  Calculate the private key d ').grid(row=6, column=0)
        Button(win, text='Cal').grid(row=6, column=1)
        Label(win, text='d = ').grid(row=7, column=0)
        Entry(win, text='',bd=3).grid(row=7, column=2)
        Label(win, text='5. Input a message m         m = ').grid(row=8, column=0)
        Entry(win, text='',bd=3).grid(row=8, column=2)
        Label(win, text='6. Encrypt c=m^e mod n ').grid(row=9, column=0)
        Button(win, text='Enc').grid(row=9, column=1)
        Label(win, text='C = ').grid(row=9, column=2)
        Entry(win, text='',bd=3).grid(row=9, column=3)
        Label(win, text='7. Decrypt m=c^d mod n ').grid(row=10, column=0)
        Button(win, text='Dec').grid(row=10, column=1)
        Label(win, text='m = ').grid(row=10, column=2)
        Entry(win, text='',bg='white',fg='black',bd=3).grid(row=10, column=3)
    def Gen(self):
        p = sympy.randprime(1000, 5000)
        q = sympy.randprime(1000, 5000)
        self.tp.insert(END,str(p))
        self.tq.insert(END,str(q))
        print(p)  # Output : 83
        print(q)  # Output : 41

window=Tk()
mywin=MyWindow(window)
window.title('RSA Encryption/Decryption')
window.geometry("700x400+20+20")
window.mainloop()