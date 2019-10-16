from tkinter import * #Graphical User Interface (GUI) that is a part of the sandard library
from tkinter import filedialog 
import binascii # Convert between binary and ASCII (from standard library)

root = Tk()

header = 'The header is consistent with the format of a ' #just an variable that is used in print statements
file_name = '' #saves the filename as a global variable

def open_file(): #function that opens the specified file
    global file_name #calls the global file_name variable
    root.fileName = filedialog.askopenfilename \
                    (filetypes=(('All files','*.*'), \
                                ('All files','*.*'))) #opens the location of the file and chooses which filetype to show

    # root.title(root.fileName)
    file_name = root.fileName #rewrites the global variable file_name to the new file name





def make_hex_file(): #function that makes the file a hex file

    filename = file_name #selects the file that will be converted into a Hex
    with open(filename, 'rb') as f: #opens the file that was selected
        content = f.read() #reads the content of the file
    hex_info = binascii.hexlify(content) #converts the file into Hexadecimals

    #print (hex_info) #allows for printing in the terminal directly

    hex_file = open(filename + ".txt","w") #opens a new file with the same name as the previous file name
    hex_file.write(str(hex_info)) #writes the Hexadecimal as a string to the text file
    hex_file.close() #closes the file that is being written to



def highlight_file(): #function to highlight where the specific text was found
    pass 



def show_filetype():

    f = open(file_name + ".txt", 'r') # open file in read mode
    data = f.read()      #makes the file readable from the data variable
    f.close()               # close the file

    file_header = {'ffd8' : 'jpg', 
                '89504e470d0a1a0a' : 'png', 
                '000001b' : ['mpeg', 'mpg'],  
                '000001ba' : 'mpg', 
                '000100080001000101' : 'img', 
                '0908100000060500' : 'xls', 
                '0d444f43' : 'doc',
                '0f00e803' : 'ppt', 
                '1a45dfa3' : ['mkv', 'webm'],
                '25504446': 'adobe'}

        
    for i in file_header: # Loops through every key in the dictionary
        if i in data: # If the key is in the test string (if "123456789" is in "uyrfr..."
            file_type = file_header[i] # Print the value of the key
            break # We break out of the loop incase of multiple keys that are in the test string 

    label = Label(text=header + file_type).grid(column=0, row=1, columnspan=4) #a field that displays the filetype

open_file_button = Button(text='Open File', command= open_file).grid(column=0, row=0) #Button to open the file
highlight_file_button = Button(text='Higlight Text', command= highlight_file).grid(column=1, row=0) #A button that shows the highlighted text
convert_file_button = Button(text='Make Hex', command= make_hex_file).grid(column=2, row=0) #Button that converts the file into hexadecimals
print_file_button = Button(text='Show filetype', command= show_filetype).grid(column=3, row=0) #Button that checks for the filetype in the hex code




root.mainloop()