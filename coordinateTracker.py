# imports
from tkinter import *
from tkinter import ttk

def inputCoordsStructure():
    def writeStructureCoords():
        structure_file = open('structures.txt', 'a+')
        structure_file.write(structure.get(1.0, END) + '\n')
        # structure_file.close()
        window2.destroy()
    window2 = Toplevel(mainWindow)
    window2.geometry('500x500')
    structure = Text(window2)
    structure.pack()
    Button(window2, text="Submit", command=writeStructureCoords).pack()

def inputCoordsBiome():
    def writeBiomeCoords():
        biome_file = open('biomes.txt', 'a+')
        biome_file.write(biome.get(1.0, END))
        # structure_file.close()
        window3.destroy()

    window3 = Toplevel(mainWindow)
    window3.geometry('500x500')
    biome = Text(window3)
    biome.pack()
    Button(window3, text="Submit", command=writeBiomeCoords).pack()

def inputCoordsLocation():
    def writeLocationCoords():
        structure_file = open('locations.txt', 'a+')
        structure_file.write(location.get(1.0, END))
        # structure_file.close()
        window4.destroy()

    window4 = Toplevel(mainWindow)
    window4.geometry('500x500')
    location = Text(window4)
    location.pack()
    Button(window4, text="Submit", command=writeLocationCoords).pack()

def readCoordsStructure():
    with open('structures.txt', 'r') as f:
        Label(tab2, text=f.read()).pack()

def readCoordsBiomes():
    with open('biomes.txt', 'r') as f:
        Label(tab2, text=f.read()).pack()

def readCoordsLocation():
    with open('locations.txt', 'r') as f:
        Label(tab2, text=f.read()).pack()

# creates new window
mainWindow = Tk()
mainWindow.geometry('700x700')
mainWindow.title("Coordinate Tracker")
# creates new tabs
tab = ttk.Notebook(mainWindow)
tab1 = ttk.Frame(mainWindow)
tab2 = ttk.Frame(mainWindow)
tab.add(tab1, text='Input Coordinates')
tab.add(tab2, text='View Coordinates')
tab.pack()

# creates titles
Label(tab1, text="Welcome to Coordinate Tracker", font=("Courier")).pack()
Label(tab1, text="Please select the button that applies to your coordinates", font=("Courier")).pack()

Label(tab2, text="Please select one of the buttons to button to view coordinates")

# creates buttons for tab1
Button(tab1, text="Structure", command=inputCoordsStructure, font=("Courier")).pack()
Button(tab1, text="Biome", command=inputCoordsBiome, font=("Courier")).pack()
Button(tab1, text="Location", command=inputCoordsLocation, font=("Courier")).pack()

Button(tab2, text="View Structure Coords", command=readCoordsStructure, font=("Courier")).pack()
Button(tab2, text='View Biome Coords', command=readCoordsBiomes, font=('Courier')).pack()
Button(tab2, text='View Location Coords', command=readCoordsLocation, font=('Courier')).pack()

#runs mainWindow
mainWindow.mainloop()