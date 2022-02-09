from tkinter import *

root = Tk()

roster = ["Hoban Washburne", "River Tam", "Shepard Book", "Adelai Niska", "Warwick Harrow", "Malcolm Reynolds",
          "Inara Serra", "Simon Tam", "Yolanda Saffron", "Fess Higgins", "Jayne Cobb", "Kaylee Frye", "Zoe Washburne",
          "Jubal Early", "Atherton Wing", "Sheppard Badger", "Tracey Smith", "Lieutenant Womack", "Sheriff Bourne",
          "Clarke Nandi", "Magistrate Higgins", "Mr. Universe", "The Operative", "Lawrence Dobson", "Thomas Anderson"]

positions = ["1 - LW", "1 - C", "1 - RW", "2 - LW", "2 - C", "2 - RW", "3 - LW", "3 - C", "3 - RW",
             "4 - LW", "4 - C", "4 - RW"]

variable = StringVar(root)
variable.set(positions[0])
dropdown = OptionMenu(root, variable, *positions)
dropdown.grid(row=14, column=0)


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

# labels and spacers
LW0 = Label(root, text="Left Wing")
C_0 = Label(root, text="Center")
RW0 = Label(root, text="Right Wing")
LD0 = Label(root, text="Left D")
RD0 = Label(root, text="Right D")
G_0 = Label(root, text="Goalie")
Scratched = Label(root, text="Scratches:")

# player labels
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

LD2 = Label(FLD1, text=roster[14])
RD2 = Label(FRD1, text=roster[15])

LD3 = Label(FLD1, text=roster[16])
RD3 = Label(FRD1, text=roster[17])

G_1 = Label(FG_1, text=roster[18])

# grid creation
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
LW1.pack()
C_1.pack()
RW1.pack()

LW2.pack()
C_2.pack()
RW2.pack()

LW3.pack()
C_3.pack()
RW3.pack()

LW4.pack()
C_4.pack()
RW4.pack()

LD1.pack()
RD1.pack()

LD2.pack()
RD2.pack()

LD3.pack()
RD3.pack()

G_1.pack()

# scratches
Scratched.grid(row=11, column=0)
for i in range(len(roster)-19):
    j = Label(root, text=roster[i+19])
    j.grid(row=12+(i // 5), column=i % 5)



root.mainloop()
