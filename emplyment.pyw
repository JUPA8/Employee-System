from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#================basics===============
frm=Tk()
fnt='None 30 bold'
bg='#b3b3ff'
bgtxt='#ffffff'
fg='#000000'
fw=700
fh=500
x=(frm.winfo_screenwidth()-fw)/2
y=(frm.winfo_screenheight()-fh)/2-50
pad=10
#======================================
svcode=StringVar()
svname=StringVar()
svaddres=StringVar()
#===========func=======================
def creat():
    if svcode.get().strip()=='':
        messagebox.showinfo('','code is empaty !')
        code.focus()
    elif svname.get().strip()=='':
        messagebox.showinfo('','name is empaty !')
        name.focus()
    elif svaddres.get().strip()=='':
        messagebox.showinfo('','adress is empaty !')
        adress.focus()
    else:
        filename='Emp.txt'
        f=open(filename,'a')
        f.write('code   : '+svcode.get()+'\n')
        f.write('name   :'+svname.get()+'\n')
        f.write('Adress : '+svaddres.get()+'\n')
        f.write('================================================================')
        f.close()
        messagebox.showinfo('confratulatiom','emploee file is created')
        svcode.set('')
        svname.set('')
        svaddres.set('')
        code.focus()
#======================================
frm.geometry('%dx%d+%d+%d'%(fw,fh,x,y))
frm.title('Employment')
frm.config(bg=bg)
Label(frm,text='Emploee Data',bg=bg,fg='black',font=fnt).pack(pady=pad)
frame=Frame(frm,bg=bg)
frame.pack(pady=pad)
Label(frame,text='Code:',bg=bg,fg=fg,font=fnt).grid(row=0,column=0)
Label(frame,text='Name:',bg=bg,fg=fg,font=fnt).grid(row=1,column=0)
Label(frame,text='Adress:',bg=bg,fg=fg,font=fnt).grid(row=2,column=0)
code=Entry(frame,bg=bgtxt,fg=fg,font=fnt,textvariable=svcode)
name=Entry(frame,bg=bgtxt,fg=fg,font=fnt,textvariable=svname)
adress=Entry(frame,bg=bgtxt,fg=fg,font=fnt,textvariable=svaddres)
code.grid(row=0,column=1,pady=pad)
name.grid(row=1,column=1,pady=pad)
adress.grid(row=2,column=1,pady=pad)
btnstyle=ttk.Style()
btnstyle.configure('TButton',font=fnt,pady=pad,padding=pad)
ttk.Button(frm,text='creat Employee file now',command=creat).pack(pady=pad)
ttk.Button(frm,text='Exit Now',command=frm.destroy).pack(pady=pad)
#==================================================

frm.mainloop()
input("  ")
