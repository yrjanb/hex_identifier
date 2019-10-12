import binascii # Convert between binary and ASCII (from standard library)

filename = 'iro.jpg' #selects the file that will be converted into a Hex
with open(filename, 'rb') as f: #opens the file that was selected
    content = f.read() #reads the content of the file
hex_info = binascii.hexlify(content) #converts the file into Hexadecimals
#print (hex_info) #allows for printing in the terminal directly
file1 = open(filename + ".txt","a") #opens a new file with the same name as the previous file name
file1.write(str(hex_info)) #writes the Hexadecimal as a string to the text file
file1.close() #closes the file that is being written to