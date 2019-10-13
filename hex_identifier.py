from tkinter import *
from tkinter import filedialog
import binascii # Convert between binary and ASCII (from standard library)

root = Tk()

header = 'The header is consistent with the format of a '
file_name = ''

def open_file():
    global file_name
    root.fileName = filedialog.askopenfilename \
                    (filetypes=(("All files","*.*"), \
                                ("All files","*.*")))

    # root.title(root.fileName)
    file_name = root.fileName





def make_hex_file():

    filename = file_name #selects the file that will be converted into a Hex
    with open(filename, 'rb') as f: #opens the file that was selected
        content = f.read() #reads the content of the file
    hex_info = binascii.hexlify(content) #converts the file into Hexadecimals

    #print (hex_info) #allows for printing in the terminal directly

    hex_file = open(filename + ".txt","w") #opens a new file with the same name as the previous file name
    hex_file.write(str(hex_info)) #writes the Hexadecimal as a string to the text file
    hex_file.close() #closes the file that is being written to



def highlight_file():
    pass



def show_filetype():

    # hex_1 = open(file_name,"r")
    f = open(file_name + ".txt", 'r') # open file in read mode
    data = f.read()      # copy to a string
    f.close()               # close the file
    # print (data)          # print the data
    if 'ffd8' in data:
        print(header,'JPG file.') #Trailer: FF D9 (ÿÙ)




open_file_button = Button(text='Open File', command= open_file).pack(side='left')
highlight_file_button = Button(text='Higlight Text', command= highlight_file).pack(side='left')
convert_file_button = Button(text='Make Hex', command= make_hex_file).pack(side='left')
print_file_button = Button(text='Show filetype', command= show_filetype).pack(side='left')
label = Label().pack()


root.mainloop()