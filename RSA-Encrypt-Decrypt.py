from tkinter import *
import sympy
class MyWindow:
    def __init__(self, win):
        Label(win, text='1.  Generate primes p and q ').grid(row=0, column=0)
        Button(win, text='GEN',command=self.Gen).grid(row=0, column=1)
        Label(win, text='( 1000 < p, q > 5000 )').grid(row=0, column=2)
        Label(win, text='p = ').grid(row=1, column=0)
        self.tp = Entry(win, text='q',bd=3)
        self.tp.grid(row=1, column=2)
        Label(win, text='q = ').grid(row=2, column=0)
        self.tq = Entry(win, text='',bd=3)
        self.tq.grid(row=2, column=2)
        Label(win, text='2.  Compute n=pq ').grid(row=3, column=0)
        Button(win, text='Com',command=self.computePQ).grid(row=3, column=1)
        Label(win, text='n = ').grid(row=4, column=0)
        self.tn = Entry(win, text='',bd=3)
        self.tn.grid(row=4, column=2)
        Label(win, text='3. Set a public key e  e = ').grid(row=5, column=0)
        self.te = Entry(win, text='',bd=3)
        self.te.grid(row=5, column=2)
        Label(win, text='4.  Calculate the private key d ').grid(row=6, column=0)
        Button(win, text='Cal', command=self.computeD).grid(row=6, column=1)
        Label(win, text='d = ').grid(row=7, column=0)
        self.td = Entry(win, text='',bd=3)
        self.td.grid(row=7, column=2)
        Label(win, text='5. Input a message m    m = ').grid(row=8, column=0)
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
        self.tp.delete(0, 'end')
        self.tp.insert(END,int(p))
        self.tq.delete(0, 'end')
        self.tq.insert(END,int(q))
    def computePQ(self):
        p = self.tp.get()
        q = self.tq.get()
        a = int(p)
        b = int(q)
        d = a*b
        self.tn.delete(0, 'end')
        self.tn.insert(END, int(d))
    ###modinverse function
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('No modular inverse')
        return x % m
    ###modinverse function end
    def computeD(self):
        print("computed")
        self.td.delete(0, 'end')
        p = self.tp.get()
        q = self.tq.get()
        e = self.te.get()
        a = int(p)
        b = int(q)
        phin = (a-1)*(b-1)
        #print(sympy.mod_inverse(e,phin))
        print(e)
        print(phin)
        self.modinv(e, int(phin))
    def encrypt(self):
        print("encrypt")
    def decrypt(self):
        print("decrypt")

window=Tk()
mywin=MyWindow(window)
window.title('RSA Encryption/Decryption')
window.geometry("700x400+20+20")
window.mainloop()
