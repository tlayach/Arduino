import tkinter as tk
import tkinter.messagebox as tk_msgbox
import tkinter.ttk as ttk
import serial
from PIL import Image, ImageTk
import webbrowser


class RSChild(ttk.Frame):
    def __init__(self, master=None, serial_conf=None):
        """
        General child configuration.
        :param master: tkinter.Tk
        """
        WIDTH, HEIGHT = 250, 230
        self.top = tk.Toplevel(master)
        ttk.Frame.__init__(self, self.top, width=WIDTH, height=HEIGHT)
        self.pack(fill=tk.BOTH, expand=1)
        self.top.withdraw()  # hide
        self.top.title("RS232")

        # window position
        # self.master.winfo_width() only works at the end
        x = int((self.top.winfo_screenwidth() - WIDTH - 40) / 2.0)
        y = int((self.top.winfo_screenheight() - HEIGHT) / 3.0)
        self.top.geometry("+{0}+{1}".format(x, y))
        self.top.resizable(width=False, height=False)  # max off

        # when button closing window (red or X) is pressed
        self.top.protocol(name="WM_DELETE_WINDOW", func=self.click_hide)

        # image
        # https://icons8.com/icon/set/serial/all
        self.img_rs = ImageTk.PhotoImage(Image.open(fp="./pictures/icons8-rs-232-male-50.png", mode="r"))
        tk.Label(self, image=self.img_rs).place(x=30, y=10)

        # text title
        ttk.Label(self, text="RS232", font=("helvetica", 14)).place(x=100, y=25)

        # text body
        ttk.Label(self, text="PORT: {}".format(serial_conf["port"])).place(x=40, y=75)
        ttk.Label(self, text="BAUD: {}".format(serial_conf["baudrate"])).place(x=40, y=105)
        ttk.Label(self, text="TIMEOUT: {}".format(serial_conf["timeout"])).place(x=40, y=135)

        # rs232 protocol
        ttk.Button(self, text="Protocol", command=self.open_website).place(x=150, y=190)

    # hide window
    def click_hide(self):
        """
        Hide window.
        :return: None
        """
        self.top.withdraw()

    # show window
    def show_window(self):
        """
        Show window.
        :return:
        """
        self.top.deiconify()

    # wikipedia website
    def open_website(self):
        """
        Opens RS232 protocol website.
        :return: None
        """
        URL = "https://en.wikipedia.org/wiki/RS-232"
        webbrowser.open_new(url=URL)


class AboutChild(ttk.Frame):
    def __init__(self, master=None):
        """
        General child configuration.
        :param master: tkinter.Tk
        """
        WIDTH, HEIGHT = 250, 230
        self.top = tk.Toplevel(master)
        ttk.Frame.__init__(self, self.top, width=WIDTH, height=HEIGHT)
        self.pack(fill=tk.BOTH, expand=1)
        self.top.withdraw()  # hide
        self.top.title("About")

        # window position
        # self.master.winfo_width() only works at the end
        x = int((self.top.winfo_screenwidth() - WIDTH + 40.0) / 2.0)
        y = int((self.top.winfo_screenheight() - HEIGHT) / 3.0)
        self.top.geometry("+{0}+{1}".format(x, y))
        self.top.resizable(width=False, height=False)  # max off

        # when button closing window (red or X) is pressed
        self.top.protocol(name="WM_DELETE_WINDOW", func=self.click_hide)

        # image
        # https://icons8.com/icon/set/user/all
        self.img_author = ImageTk.PhotoImage(Image.open(fp="./pictures/icons8-customer-50.png", mode="r"))
        tk.Label(self, image=self.img_author).place(x=30, y=10)

        # text title
        ttk.Label(self, text="Author", font=("helvetica", 14)).place(x=100, y=25)

        # text body
        ttk.Label(self, text="Name: Paulo G.P.").place(x=40, y=75)
        ttk.Label(self, text="Year: 2017").place(x=40, y=105)
        ttk.Label(self, text="All rights reserved.").place(x=40, y=135)

        # about.me website
        ttk.Button(self, text="About.Me", command=self.open_website).place(x=150, y=190)

    # hide window
    def click_hide(self):
        """
        Hide window.
        :return: None
        """
        self.top.withdraw()

    # show window
    def show_window(self):
        """
        Show window.
        :return:
        """
        self.top.deiconify()

    # wikipedia website
    def open_website(self):
        """
        Opens RS232 protocol website.
        :return: None
        """
        URL = "https://about.me/paulogp"
        webbrowser.open_new(url=URL)


class Master(ttk.Frame):
    def __init__(self, master=None):
        """
        General configuration.
        :param master: tkinter.Tk
        """
        # serial settings
        self.serial_conf = {"port": "COM3",  # mac: "/dev/cu.usbmodem411",  # pc: "COM1",
                            "baudrate": 9600,  # 115200  # 9600
                            "parity": serial.PARITY_NONE,
                            "stopbits": 1,
                            "bytesize": serial.EIGHTBITS,
                            "timeout": 0.1}
        # start all
        self.master = master

        # menu
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        # menu File
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", underline=0, menu=file_menu)
        file_menu.add_command(label="Exit", underline=1, command=self.click_exit, accelerator="Ctrl+Q")
        self.master.bind("<Control-q>", self.click_exit_bind)  # extra arg to def
        # menu help
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", underline=0, menu=help_menu)
        help_menu.add_command(label="RS232", underline=0, command=self.show_rs232_child)
        help_menu.add_separator()
        help_menu.add_command(label="About", underline=0, command=self.show_about_child)

        # frame I - toolbar
        # https://icons8.com/icon/free-pack/music/office
        toolbar = tk.Frame(master, bd=1, relief=tk.SUNKEN)
        # play serial
        self.img_play = ImageTk.PhotoImage(Image.open(fp="./pictures/icons8-rocket-26.png", mode="r"))
        tk.Button(toolbar, image=self.img_play, relief=tk.FLAT, command=self.open_serial)\
            .pack(side=tk.LEFT, padx=2.0, pady=1.0)
        # stop serial
        self.img_stop = ImageTk.PhotoImage(Image.open(fp="./pictures/icons8-private-26.png", mode="r"))
        tk.Button(toolbar, image=self.img_stop, relief=tk.FLAT, command=self.close_serial)\
            .pack(side=tk.LEFT, padx=2.0, pady=1.0)
        # play beep
        self.img_beep = ImageTk.PhotoImage(Image.open(fp="./pictures/icons8-notification-26.png", mode="r"))
        tk.Button(toolbar, image=self.img_beep, relief=tk.FLAT, command=self.play_beep)\
            .pack(side=tk.LEFT, padx=2.0, pady=1.0)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # frame II - body
        WIDTH, HEIGHT = 400, 210
        ttk.Frame.__init__(self, self.master, width=WIDTH, height=HEIGHT)
        self.pack()
        self.master.title("Temperature")

        # window position
        # self.master.winfo_width() only works at the end
        x = int((self.master.winfo_screenwidth() - WIDTH) / 2.0)
        y = int((self.master.winfo_screenheight() - HEIGHT) / 3.0)
        self.master.geometry("+{0}+{1}".format(x, y))
        self.master.resizable(width=False, height=False)  # max off
        self.master.lift()  # raise window (stacking order)
        # self.master.deiconify()  # iconify -> minimized

        # icon
        # https://www.shareicon.net/aliens-fuel-exploration-nasa-rocket-spaceship-space-103505
        self.master.wm_iconbitmap("./pictures/spaceship.ico")

        # when button closing window (red or X) is pressed
        self.master.protocol(name="WM_DELETE_WINDOW", func=self.click_exit)

        # image board
        # https://icons8.com/icon/set/electronic-board/all
        self.img_board = ImageTk.PhotoImage(Image.open(fp="./pictures/icons8-motherboard-50.png", mode="r"))
        tk.Label(self, image=self.img_board).place(x=30, y=20)

        # label with variable
        self.micro_msg = tk.StringVar()
        self.micro_msg.set("-----")
        # bg="red", fg="white"
        ttk.Label(self, textvariable=self.micro_msg, width=5, font=("helvetica", 40)).place(x=150, y=50)

        # button Start
        # ttk.Button(self, text="Start", command=self.open_serial).place(x=100, y=120)

        # button Stop
        # ttk.Button(self, text="Stop", command=self.close_serial).place(x=220, y=120)

        # frame III - statusbar
        # serial status image
        # https://icons8.com/icon/set/connect/office
        self.img_status_on = ImageTk.PhotoImage(Image.open(fp="./pictures/icons8-connected-16.png", mode="r"))
        self.img_status_off = ImageTk.PhotoImage(Image.open(fp="./pictures/icons8-disconnected-16.png", mode="r"))
        statusbar = tk.Frame(master, bd=1, relief=tk.SUNKEN)
        self.label_status = tk.Label(statusbar, image=self.img_status_off)
        self.label_status.pack(side=tk.LEFT, padx=2.0, pady=1.0)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)

        # prepare classes
        # serial class
        self.micro_serial = None

        # author child class
        self.about_child = AboutChild(self.master)

        # rs child class
        self.rs_child = RSChild(master=self.master, serial_conf=self.serial_conf)

    # exit application
    def click_exit(self):
        """
        Result of selecting menu Exit - Dialog.
        :return: None
        """
        result = tk_msgbox.askyesno(title="Quit?", message="Are you sure you want to quit?", icon="question")
        if result:
            self.master.destroy()

    # exit application bind
    def click_exit_bind(self, *args):
        """
        A bind to exit...
        :param args: None
        :return: None
        """
        self.click_exit()

    # open serial
    def open_serial(self):
        """
        Open serial connection.
        :return: None
        """
        if self.micro_serial is None:
            try:
                self.micro_serial = serial.Serial(port=self.serial_conf["port"],
                                                  baudrate=self.serial_conf["baudrate"],
                                                  parity=self.serial_conf["parity"],
                                                  stopbits=self.serial_conf["stopbits"],
                                                  bytesize=self.serial_conf["bytesize"],
                                                  timeout=self.serial_conf["timeout"])
                self.process_serial()
                self.label_status["image"] = self.img_status_on
            except Exception as e:
                self.label_status["image"] = self.img_status_off
                tk_msgbox.showerror(title="Alert", message=e)
        else:
            print("Connection already open!")

    # close serial
    def close_serial(self):
        """
        Close serial connection.
        :return: None
        """
        self.micro_serial.flush()
        self.micro_serial.close()
        self.micro_serial = None
        self.label_status["image"] = self.img_status_off

    # read serial data
    def process_serial(self):
        """
        Read data from serial connection.
        :return: None
        """
        if self.micro_serial is not None:
            if self.micro_serial.isOpen():
                try:
                    while True:
                        if self.micro_serial.inWaiting() > 0:
                            data = self.micro_serial.readline()
                            self.micro_msg.set(data)
                        else:
                            self.micro_serial.flush()
                            break

                    self.after(ms=2, func=self.process_serial)
                except Exception as e:
                    self.micro_serial = None
                    self.label_status["image"] = self.img_status_off
                    tk_msgbox.showerror(title="Alert", message=e)

    # show about window
    def show_about_child(self):
        """
        Shows About window.
        :return: None
        """
        self.about_child.show_window()

    # show rs232 window
    def show_rs232_child(self):
        """
        Shows RS232 window.
        :return: None
        """
        self.rs_child.show_window()

    # beep (may need it for the alerts)
    def play_beep(self):
        """
        Emits a beep.
        :return: None
        """
        self.bell()


if __name__ == "__main__":
    root = tk.Tk()
    # root.geometry("250x150+300+300")
    app = Master(root)
    root.mainloop()
