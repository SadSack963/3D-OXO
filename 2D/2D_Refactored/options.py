from tkinter import Tk, IntVar, Checkbutton, Label, Frame, SUNKEN


TITLE_FONT = ("Sergoe UI", 24, "bold")
LARGE_FONT = ("Sergoe UI", 16, "normal")
NORMAL_FONT = ("Sergoe UI", 12, "normal")
LIGHT = '#7c7c7c'
DARK = '#3c3c3c'


class Options:
    def __init__(self):
        # Window Definition
        self.window = Tk()
        self.window.title('Options')
        self.window.config(padx=30, pady=0, bg=LIGHT)
        self.window.wm_attributes()

        self.player_1_check_human = IntVar()
        self.player_1_check_human.set(1)  # Default to checked
        self.player_1_check_ai = IntVar()
        self.player_1_check_ai.set(0)  # Default to unchecked

        self.player_2_check_human = IntVar()
        self.player_2_check_human.set(0)  # Default to unchecked
        self.player_2_check_ai = IntVar()
        self.player_2_check_ai.set(1)  # Default to checked

        # Widget Definitions

        self.label_title = Label(
            text="Choose Players",
            bg=LIGHT,
            fg="black",
            font=TITLE_FONT
        )

        self.frame_separator = Frame(
            master=self.window,
            padx=0,
            pady=0,
            bg=LIGHT,
        )

        self.label_separator = Label(
            master=self.frame_separator,
            text='  ',
            bg=LIGHT,
        )

        # ---------------- PLAYER 1 CHOICES ----------------

        self.frame_player_1 = Frame(
            master=self.window,
            padx=5,
            pady=5,
            bg=DARK,
            borderwidth=5,
            relief=SUNKEN,
        )

        self.label_player_1 = Label(
            master=self.frame_player_1,
            text="Player 1 - X",
            pady=5,
            bg=DARK,
            fg="white",
            font=LARGE_FONT,
        )

        self.checkbutton_player_1_human = Checkbutton(
            master=self.frame_player_1,
            text="Human",
            bg=DARK,
            fg="white",
            indicatoron=False,
            selectcolor='green',
            font=NORMAL_FONT,
            variable=self.player_1_check_human,
            command=self.player_1_select_human,
        )

        self.checkbutton_player_1_ai = Checkbutton(
            master=self.frame_player_1,
            text="AI",
            bg=DARK,
            fg="white",
            indicatoron=False,
            selectcolor='green',
            font=NORMAL_FONT,
            variable=self.player_1_check_ai,
            command=self.player_1_select_ai,
        )

        # ---------------- PLAYER 1 CHOICES ----------------

        self.frame_player_2_frame = Frame(
            master=self.window,
            padx=5,
            pady=5,
            bg=DARK,
            borderwidth=5,
            relief=SUNKEN,
        )

        self.label_player_2 = Label(
            master=self.frame_player_2_frame,
            text="Player 2 - O",
            pady=5,
            bg=DARK,
            fg="white",
            font=LARGE_FONT,
        )

        self.checkbutton_player_2_human = Checkbutton(
            master=self.frame_player_2_frame,
            text="Human",
            bg=DARK,
            fg="white",
            indicatoron=False,
            selectcolor='green',
            font=NORMAL_FONT,
            variable=self.player_2_check_human,
            command=self.player_2_select_human,
        )

        self.checkbutton_player_2_ai = Checkbutton(
            master=self.frame_player_2_frame,
            text="AI",
            bg=DARK,
            fg="white",
            indicatoron=False,
            selectcolor='green',
            font=NORMAL_FONT,
            variable=self.player_2_check_ai,
            command=self.player_2_select_ai,
        )

        # Grid Layout
        self.label_title.grid(row=0, column=0, columnspan=3, pady=10)

        self.frame_player_1.grid(row=1, column=0, sticky='EW', pady=(0, 30))
        self.label_player_1.grid(row=0, column=0, sticky='EW')
        self.checkbutton_player_1_human.grid(row=1, column=0, pady=5)
        self.checkbutton_player_1_ai.grid(row=2, column=0, pady=5)

        self.frame_separator.grid(row=1, column=1)
        self.label_separator.grid(row=0, column=0)

        self.frame_player_2_frame.grid(row=1, column=2, sticky='EW', pady=(0, 30))
        self.label_player_2.grid(row=0, column=0, sticky='EW')
        self.checkbutton_player_2_human.grid(row=1, column=0, pady=5)
        self.checkbutton_player_2_ai.grid(row=2, column=0, pady=5)

        self.window.mainloop()

    def player_1_select_human(self):
        self.checkbutton_player_1_human.select()
        self.checkbutton_player_1_ai.deselect()

    def player_1_select_ai(self):
        self.checkbutton_player_1_human.deselect()
        self.checkbutton_player_1_ai.select()

    def player_2_select_human(self):
        self.checkbutton_player_2_human.select()
        self.checkbutton_player_2_ai.deselect()

    def player_2_select_ai(self):
        self.checkbutton_player_2_human.deselect()
        self.checkbutton_player_2_ai.select()

    def get_players(self):
        player_dict = {}
        if self.player_1_check_human.get()\
                and not self.player_1_check_ai.get():
            player_dict['player_1'] = 'human'
        if not self.player_1_check_human.get()\
                and self.player_1_check_ai.get():
            player_dict['player_1'] = 'ai'

        if self.player_2_check_human.get()\
                and not self.player_2_check_ai.get():
            player_dict['player_2'] = 'human'
        if not self.player_2_check_human.get()\
                and self.player_2_check_ai.get():
            player_dict['player_2'] = 'ai'

        return player_dict


if __name__ == '__main__':
    options = Options()
