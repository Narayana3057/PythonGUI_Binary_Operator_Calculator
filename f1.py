from tkinter import*
import math 
from tkinter import messagebox
def RESULT():
    E3.delete(0, 'end');
    p=r.get()
    q1=E1.get()
    q2=E2.get()
    if q1=="" or q2=="":
        msg = messagebox.showinfo("Validation","Please enter the values...");    
    elif p!=1 and p!=2 and p!=3 and p!=4:
        msg = messagebox.showinfo("Validation","Please select the gate...");
    else:
        a=int(q1)
        b=int(q2)
        if p==1:
            c=a&b;
            E3.insert(0,c);
        if p==2:
            c=a|b;
            E3.insert(0,c);
        if p==3:
            def onesComplement(a): 
                number_of_bits = (int)(math.floor(math.log(a)/math.log(2))) + 1;  
                return ((1 << number_of_bits) - 1) ^ a;
            c=onesComplement(a)
            def onesComplementB(b): 
                number_of_bits = (int)(math.floor(math.log(b)/math.log(2))) + 1;  
                return ((1 << number_of_bits) - 1) ^ b;
            c1=onesComplementB(b)
            k=c,"and",c1;
            E3.insert(0,k);
        if p==4:
            c=a^b;
            E3.insert(0,c);
def ABOUT():
    root=Tk()
    p=r.get()
    c = Canvas(width = 500, height = 500, bg = 'grey')
    c.pack(expand = YES, fill = BOTH)
    if p==1:
        f="and.png"
    if p==2:
        f=""
    if p==3:
        f=""
    if p==4:
        f=""
    gif1 = PhotoImage(file=f)
    c.create_image(50, 10, image = gif1, anchor = NW)
    root.mainloop()
def EXIT():
    bitwise.destroy()
def RESET():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    E3.delete(0, 'end')
def EXPLANATION():
    p=r.get()
    q1=E1.get()
    q2=E2.get()
    y=E3.get()
    if q1=="" or q2=="":
        msg = messagebox.showinfo("Validation","Please enter the values...");    
    elif p!=1 and p!=2 and p!=3 and p!=4:
        msg = messagebox.showinfo("Validation","Please select the gate...");
    elif y=="":
        msg = messagebox.showinfo("Validation","It will work after submition only, Please submit frist..");     
    else:
        exp=Tk()
        def EXIT123():
            exp.destroy()
        exp.config(background="grey")
        exp.title("EXPLANATION")
        exp.geometry("1250x450")
        l0=Label(exp,text="EXPLANATION",borderwidth=10,relief="groove",width=76,height=1)
        l0.place(x=5,y=10,bordermode=OUTSIDE)
        l0.configure(font=("Times New Roman",20,"bold"))
        l1=Label(exp,text="Number-1:",borderwidth=2,relief="groove",width=20,height=2).place(x=195,y=110,bordermode=OUTSIDE)
        e1=Entry(exp,bd=4)
        e1.place(x=340,y=110,width=200,height=35)
        l2=Label(exp,text="Binary of Number-1 (A):",borderwidth=2,relief="groove",width=20,height=2).place(x=710,y=110,bordermode=OUTSIDE)
        e2=Entry(exp,bd=4)
        e2.place(x=855,y=110,width=200,height=35)
        l3=Label(exp,text="Number-2:",borderwidth=2,relief="groove",width=20,height=2).place(x=195,y=180,bordermode=OUTSIDE)
        e3=Entry(exp,bd=4)
        e3.place(x=340,y=180,width=200,height=35)
        l4=Label(exp,text="Binary of Number-2 (B):",borderwidth=2,relief="groove",width=20,height=2).place(x=710,y=180,bordermode=OUTSIDE)
        e4=Entry(exp,bd=4)
        e4.place(x=855,y=180,width=200,height=35)
        p=r.get()
        if p==1:
            t="'A'  AND  'B' :"
            y="ABOUT AND GATE"
        if p==2:
            t="'A'  OR  'B' :"
            Y="ABOUT OR GATE"
        if p==3:
            t="NOT gate of 'A' :"
            Y="ABOUT NOT GATE"
            l7=Label(exp,text="NOT gate of 'B':",borderwidth=2,relief="groove",width=20,height=2).place(x=710,y=280,bordermode=OUTSIDE)
            e7=Entry(exp,bd=4)
            e7.place(x=855,y=280,width=200,height=35)
        if p==4:
            t="'A'  XOR  'B' :"
            y="ABOUT XOR GATE"
        l5=Label(exp,text=t,borderwidth=2,relief="groove",width=20,height=2).place(x=710,y=240,bordermode=OUTSIDE)
        e5=Entry(exp,bd=4)
        e5.place(x=855,y=240,width=200,height=35)
        l6=Label(exp,text="DECIMAL RESULT :",borderwidth=2,relief="groove",width=20,height=2).place(x=275,y=340,bordermode=OUTSIDE)
        e6=Entry(exp,bd=4)
        e6.place(x=420,y=340,width=200,height=35)
        b0=Button(exp,text="EXIT", width=30,height=2,bd=5,  bg='red',fg='black', activebackground='brown', activeforeground='black',command=EXIT123)
        b0.place(x=15,y=380)
        a=int(E1.get())
        b=int(E2.get())
        bina=bin(a).replace("0b","");
        binb=bin(b).replace("0b","");
        e1.insert(0,a);
        e3.insert(0,b);
        e2.insert(0,bina);
        e4.insert(0,binb);
        if p==1:
            c=a&b;
            binc=bin(c).replace("0b","");
            e5.insert(0,binc);
            e6.insert(0,c);
        if p==2:
            c=a|b;
            binc=bin(c).replace("0b","");
            e5.insert(0,binc);
            e6.insert(0,c);
        if p==3:
            def onesComplementA(a): 
                number_of_bits = (int)(math.floor(math.log(a)/math.log(2))) + 1;  
                return ((1 << number_of_bits) - 1) ^ a;
            c=onesComplementA(a)
            def onesComplementB(b): 
                number_of_bits = (int)(math.floor(math.log(b)/math.log(2))) + 1;  
                return ((1 << number_of_bits) - 1) ^ b;
            c1=onesComplementB(b)
            binc1=bin(c1).replace("0b","");
            e7.insert(0,binc1);    
            binc=bin(c).replace("0b","");
            e5.insert(0,binc);
            binc=bin(c).replace("0b","");
            k=c,"and",c1;
            e6.insert(0,k);
        if p==4:
            c=a^b;
            binc=bin(c).replace("0b","");
            e5.insert(0,binc);
            e6.insert(0,c);
        exp.mainloop()
def AA():
    E3.delete(0, 'end')
bitwise=Tk()
bitwise.config(background="grey")
bitwise.title("Bitwise Operators")
bitwise.geometry("1250x560")
L0=Label(bitwise,text="BITWISE OPERATIONS",borderwidth=10,relief="groove",width=76,height=1)
L0.place(x=5,y=10,bordermode=OUTSIDE)
L0.configure(font=("Times New Roman",20,"bold"))
L1=Label(bitwise,text="Number-1:",borderwidth=2,relief="groove",width=20,height=2).place(x=195,y=110,bordermode=OUTSIDE)
E1=Entry(bitwise,bd=4)
E1.place(x=340,y=110,width=200,height=35)
L2=Label(bitwise,text="Number-2:",borderwidth=2,relief="groove",width=20,height=2).place(x=710,y=110,bordermode=OUTSIDE)
E2=Entry(bitwise,bd=4)
E2.place(x=855,y=110,width=200,height=35)
r=IntVar()
Radiobutton(bitwise,text="AND GATE",variable=r,value=1,indicatoron=0,borderwidth=2,relief="raised",bd=3,padx=20,fg="black",bg="grey",width=20,command=AA).place(x=530,y=180)
Radiobutton(bitwise,text="OR GATE",variable=r,value=2,indicatoron=0,borderwidth=2,relief="raised",bd=3,padx=20,fg="black",bg="grey",width=20,command=AA).place(x=530,y=220)
Radiobutton(bitwise,text="NOT GATE",variable=r,value=3,indicatoron=0,borderwidth=2,relief="raised",bd=3,padx=20,fg="black",bg="grey",width=20,command=AA).place(x=530,y=260)
Radiobutton(bitwise,text="EXOR GATE",variable=r,value=4,indicatoron=0,borderwidth=2,relief="raised",bd=3,padx=20,fg="black",bg="grey",width=20,command=AA).place(x=530,y=300)
B1=Button(bitwise,justify = LEFT)
photo=PhotoImage(file="photo.png")
B1.config(image=photo,width="200",height="50",bd=0,background="grey",activebackground='grey',command=RESULT)
B1.place(x=525,y=347)
L3=Label(bitwise,text="RESULT:",borderwidth=2,relief="groove",width=20,height=2).place(x=195,y=420,bordermode=OUTSIDE)
E3=Entry(bitwise,bd=4)
E3.place(x=340,y=420,width=200,height=35)
B2=Button(bitwise,text="EXPLANATION",font=("Times New Roman",10,'bold'), width=30,height=2,bd=5,  bg='light green',fg='black', activebackground='lightgreen', activeforeground='black',command=EXPLANATION)
B2.place(x=780,y=410)
B3=Button(bitwise,text="EXIT",font=("Times New Roman",10,'bold'), width=30,height=2,bd=5,  bg='red',fg='black', activebackground='brown', activeforeground='black',command=EXIT)
B3.place(x=15,y=510)
B3=Button(bitwise,text="RESET",font=("Times New Roman",10,'bold'), width=30,height=2,bd=5,  bg='BLUE',fg='black', activebackground='lightblue', activeforeground='black',command=RESET)
B3.place(x=1000,y=510)

bitwise.mainloop()
