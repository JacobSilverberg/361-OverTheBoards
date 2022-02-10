from tkinter import *

root = Tk()

roster = ["Hoban Washburne", "River Tam", "Shepard Book", "Adelai Niska", "Warwick Harrow", "Malcolm Reynolds",
          "Inara Serra", "Simon Tam", "Yolanda Saffron", "Fess Higgins", "Jayne Cobb", "Kaylee Frye", "Zoe Washburne",
          "Jubal Early", "Atherton Wing", "Sheppard Badger", "Tracey Smith", "Lieutenant Womack", "Sheriff Bourne",
          "Clarke Nandi", "Magistrate Higgins", "Patience Whitefall", "Stitch Hessian", "Lawrence Dobson",
          "Thomas Anderson"]

positions = ["1 - LW", "1 - C ", "1 - RW", "2 - LW", "2 - C ", "2 - RW", "3 - LW", "3 - C ", "3 - RW",
             "4 - LW", "4 - C ", "4 - RW", "1 - LD", "1 - RD", "2 - LD", "2 - RD", "3 - LD", "3 - RD", "1 - G ",
             "Scratch"]




def positionSwitch():
    print("Position Selected is", variable.get())


# frame creation
FLW0 = Frame(root)
FC_0 = Frame(root)
FRW0 = Frame(root)

FLW1 = Frame(root)
FC_1 = Frame(root)
FRW1 = Frame(root)

FLW2 = Frame(root)
FC_2 = Frame(root)
FRW2 = Frame(root)

FLW3 = Frame(root)
FC_3 = Frame(root)
FRW3 = Frame(root)

FLW4 = Frame(root)
FC_4 = Frame(root)
FRW4 = Frame(root)

FLD0 = Frame(root)
FRD0 = Frame(root)

FLD1 = Frame(root)
FRD1 = Frame(root)

FLD2 = Frame(root)
FRD2 = Frame(root)

FLD3 = Frame(root)
FRD3 = Frame(root)

FG_0 = Frame(root)
FG_1 = Frame(root)

# position labels and spacers
LW0 = Label(FLW0, text="Left Wing")
C_0 = Label(FC_0, text="Center")
RW0 = Label(FRW0, text="Right Wing")
LD0 = Label(FLD0, text="Left D")
RD0 = Label(FRD0, text="Right D")
G_0 = Label(FG_0, text="Goalie")
Scr = Label(root, text="Scratches:")

# player name labels
LW1 = Label(FLW1, text=roster[0])
C_1 = Label(FC_1, text=roster[1])
RW1 = Label(FRW1, text=roster[2])

LW2 = Label(FLW2, text=roster[3])
C_2 = Label(FC_2, text=roster[4])
RW2 = Label(FRW2, text=roster[5])

LW3 = Label(FLW3, text=roster[6])
C_3 = Label(FC_3, text=roster[7])
RW3 = Label(FRW3, text=roster[8])

LW4 = Label(FLW4, text=roster[9])
C_4 = Label(FC_4, text=roster[10])
RW4 = Label(FRW4, text=roster[11])

LD1 = Label(FLD1, text=roster[12])
RD1 = Label(FRD1, text=roster[13])

LD2 = Label(FLD2, text=roster[14])
RD2 = Label(FRD2, text=roster[15])

LD3 = Label(FLD3, text=roster[16])
RD3 = Label(FRD3, text=roster[17])

G_1 = Label(FG_1, text=roster[18])

# position selection create pos_var
pos_varFLW1 = StringVar(root)
pos_varFC_1 = StringVar(root)
pos_varFRW1 = StringVar(root)
pos_varFLW2 = StringVar(root)
pos_varFC_2 = StringVar(root)
pos_varFRW2 = StringVar(root)
pos_varFLW3 = StringVar(root)
pos_varFC_3 = StringVar(root)
pos_varFRW3 = StringVar(root)
pos_varFLW4 = StringVar(root)
pos_varFC_4 = StringVar(root)
pos_varFRW4 = StringVar(root)
pos_varFLD1 = StringVar(root)
pos_varFRD1 = StringVar(root)
pos_varFLD2 = StringVar(root)
pos_varFRD2 = StringVar(root)
pos_varFLD3 = StringVar(root)
pos_varFRD3 = StringVar(root)
pos_varFG_1 = StringVar(root)

# set default dropdown to correct position
pos_varFLW1.set(positions[0])
pos_varFC_1.set(positions[1])
pos_varFRW1.set(positions[2])
pos_varFLW2.set(positions[3])
pos_varFC_2.set(positions[4])
pos_varFRW2.set(positions[5])
pos_varFLW3.set(positions[6])
pos_varFC_3.set(positions[7])
pos_varFRW3.set(positions[8])
pos_varFLW4.set(positions[9])
pos_varFC_4.set(positions[10])
pos_varFRW4.set(positions[11])
pos_varFLD1.set(positions[12])
pos_varFRD1.set(positions[13])
pos_varFLD2.set(positions[14])
pos_varFRD2.set(positions[15])
pos_varFLD3.set(positions[16])
pos_varFRD3.set(positions[17])
pos_varFG_1.set(positions[18])

# create dropdown button object
dropdownFLW1 = OptionMenu(FLW1, pos_varFLW1, *positions)
dropdownFC_1 = OptionMenu(FC_1, pos_varFC_1, *positions)
dropdownFRW1 = OptionMenu(FRW1, pos_varFRW1, *positions)

dropdownFLW2 = OptionMenu(FLW2, pos_varFLW2, *positions)
dropdownFC_2 = OptionMenu(FC_2, pos_varFC_2, *positions)
dropdownFRW2 = OptionMenu(FRW2, pos_varFRW2, *positions)

dropdownFLW3 = OptionMenu(FLW3, pos_varFLW3, *positions)
dropdownFC_3 = OptionMenu(FC_3, pos_varFC_3, *positions)
dropdownFRW3 = OptionMenu(FRW3, pos_varFRW3, *positions)

dropdownFLW4 = OptionMenu(FLW4, pos_varFLW4, *positions)
dropdownFC_4 = OptionMenu(FC_4, pos_varFC_4, *positions)
dropdownFRW4 = OptionMenu(FRW4, pos_varFRW4, *positions)

dropdownFLD1 = OptionMenu(FLD1, pos_varFLD1, *positions)
dropdownFRD1 = OptionMenu(FRD1, pos_varFRD1, *positions)

dropdownFLD2 = OptionMenu(FLD2, pos_varFLD2, *positions)
dropdownFRD2 = OptionMenu(FRD2, pos_varFRD2, *positions)

dropdownFLD3 = OptionMenu(FLD3, pos_varFLD3, *positions)
dropdownFRD3 = OptionMenu(FRD3, pos_varFRD3, *positions)

dropdownFG_1 = OptionMenu(FG_1, pos_varFG_1, *positions)

# grid creation with frames
FLW0.grid(row=0, column=0)
FC_0.grid(row=0, column=2)
FRW0.grid(row=0, column=4)

FLW1.grid(row=1, column=0)
FC_1.grid(row=1, column=2)
FRW1.grid(row=1, column=4)

FLW2.grid(row=2, column=0)
FC_2.grid(row=2, column=2)
FRW2.grid(row=2, column=4)

FLW3.grid(row=3, column=0)
FC_3.grid(row=3, column=2)
FRW3.grid(row=3, column=4)

FLW4.grid(row=4, column=0)
FC_4.grid(row=4, column=2)
FRW4.grid(row=4, column=4)

FLD0.grid(row=5, column=1)
FRD0.grid(row=5, column=3)

FLD1.grid(row=6, column=1)
FRD1.grid(row=6, column=3)

FLD2.grid(row=7, column=1)
FRD2.grid(row=7, column=3)

FLD3.grid(row=8, column=1)
FRD3.grid(row=8, column=3)

FG_0.grid(row=9, column=2)
FG_1.grid(row=10, column=2)

# packing
LW0.pack()
C_0.pack()
RW0.pack()

LW1.pack(side=LEFT)
C_1.pack(side=LEFT)
RW1.pack(side=LEFT)

LW2.pack(side=LEFT)
C_2.pack(side=LEFT)
RW2.pack(side=LEFT)

LW3.pack(side=LEFT)
C_3.pack(side=LEFT)
RW3.pack(side=LEFT)

LW4.pack(side=LEFT)
C_4.pack(side=LEFT)
RW4.pack(side=LEFT)

LD0.pack(side=LEFT)
RD0.pack(side=LEFT)

LD1.pack(side=LEFT)
RD1.pack(side=LEFT)

LD2.pack(side=LEFT)
RD2.pack(side=LEFT)

LD3.pack(side=LEFT)
RD3.pack(side=LEFT)

G_0.pack(side=LEFT)
G_1.pack(side=LEFT)

dropdownFLW1.pack(side=RIGHT)
dropdownFC_1.pack(side=RIGHT)
dropdownFRW1.pack(side=RIGHT)

dropdownFLW2.pack(side=RIGHT)
dropdownFC_2.pack(side=RIGHT)
dropdownFRW2.pack(side=RIGHT)

dropdownFLW3.pack(side=RIGHT)
dropdownFC_3.pack(side=RIGHT)
dropdownFRW3.pack(side=RIGHT)

dropdownFLW4.pack(side=RIGHT)
dropdownFC_4.pack(side=RIGHT)
dropdownFRW4.pack(side=RIGHT)

dropdownFLD1.pack(side=RIGHT)
dropdownFRD1.pack(side=RIGHT)

dropdownFLD2.pack(side=RIGHT)
dropdownFRD2.pack(side=RIGHT)

dropdownFLD3.pack(side=RIGHT)
dropdownFRD3.pack(side=RIGHT)

dropdownFG_1.pack(side=RIGHT)

# scratches
Scr.grid(row=11, column=0)
for i in range(len(roster)-19):
    j = Label(root, text=roster[i+19])
    j.grid(row=12+(i // 5), column=i % 5)



root.mainloop()
