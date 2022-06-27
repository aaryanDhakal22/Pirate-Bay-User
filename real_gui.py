
import sys
import scraper
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import supporter
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    supporter.set_Tk_var()
    top = Toplevel1 (root)
    supporter.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    supporter.set_Tk_var()
    top = Toplevel1 (w)
    supporter.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("471x230+699+294")
        top.title("Torrent Finder")
        top.configure(background="#d9d9d9")
        top.configure(highlightcolor="#646464")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.0, rely=0.609, height=26, width=82)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Name :''')
        self.Label1.configure(width=82)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.021, rely=0.783, height=26, width=72)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Pages :''')
        self.Label2.configure(width=72)


        def generat():
            name = self.TEntry1.get()
            value = int(supporter.selected.get())
            scraper.generator_oppo(name , value)


        self.Button1 = tk.Button(top,command = generat)
        self.Button1.place(relx=0.764, rely=0.783, height=33, width=86)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Generate''')
        self.Button1.configure(width=86)

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.17, rely=0.609, relheight=0.113
                , relwidth=0.777)
        self.TEntry1.configure(width=366)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=-0.021, rely=0.0, relheight=0.535
                , relwidth=1.025)
        self.Canvas1.configure(background="#2f5597")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="#000000")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=483)

        self.Label3 = tk.Label(self.Canvas1)
        self.Label3.place(relx=0.228, rely=0.163, height=86, width=249)
        self.Label3.configure(background="#ff8f2e")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"./knoted.png")
        self._img0 = tk.PhotoImage(file=photo_location)
        self.Label3.configure(image=self._img0)
        self.Label3.configure(width=249)

        self.style.map('TRadiobutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.TRadiobutton1 = ttk.Radiobutton(top)
        self.TRadiobutton1.place(relx=0.17, rely=0.783, relwidth=0.066
                , relheight=0.0, height=26)
        self.TRadiobutton1.configure(variable=supporter.selected)
        self.TRadiobutton1.configure(value="5")
        self.TRadiobutton1.configure(takefocus="")
        self.TRadiobutton1.configure(text='''5''')

        self.TRadiobutton2 = ttk.Radiobutton(top)
        self.TRadiobutton2.place(relx=0.446, rely=0.783, relwidth=0.083
                , relheight=0.0, height=26)
        self.TRadiobutton2.configure(variable=supporter.selected)
        self.TRadiobutton2.configure(value="20")
        self.TRadiobutton2.configure(takefocus="")
        self.TRadiobutton2.configure(text='''20''')

        self.TRadiobutton3 = ttk.Radiobutton(top)
        self.TRadiobutton3.place(relx=0.297, rely=0.783, relwidth=0.083
                , relheight=0.0, height=26)
        self.TRadiobutton3.configure(variable=supporter.selected)
        self.TRadiobutton3.configure(value="10")
        self.TRadiobutton3.configure(takefocus="")
        self.TRadiobutton3.configure(text='''10''')

if __name__ == '__main__':
    vp_start_gui()
