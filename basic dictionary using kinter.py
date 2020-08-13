#!Python3
# Tcl/Tk version 8.6

# A basic self dictionary using Tkinter GUI module.
# TODO implement SQLight.
# TODO Improve so it accepts inputs from user.
# TODO Implement a machime learnig alg to help with spaced repetion.


import tkinter as tk 

# key down function
def click():
    entered_text = wordentry.get() # this will collect text from text entry box
    output.delete(0.0, 'end')
    try:
        definition = mydictionary[entered_text]
    except:
        definition = 'No such word in dictionary'
    output.insert('end', definition)

def close_window():
    window.destroy()
    exit()

## main
window = tk.Tk()
window.title('A Basic Dictionary')
window.configure(background='black')

# adding logo to window (gif works best with pyhton)
photo1 = tk.PhotoImage(file='open_book.png')
tk.Label (window, image=photo1, bg='black').grid(
        row=0, column=0, padx = 5, pady = 10, sticky = 'w')

# create label
tk.Label (window, text='Enter the word:', bg='black', fg='white', font='none 12 bold') .grid(
        row=1, column=0, padx = 5, pady = 10, sticky = 'nw')

# create a text entry box
wordentry = tk.Entry(window, width=20, bg='white')
wordentry.grid(row=2, column=0, sticky='w', padx = 5, pady = 10)

# add a submit button
tk.Button (window, text='ENTER', width=6, command=click).grid(
        row=3, column=0, sticky ='nw',  padx = 5, pady = 10)

# create another label
tk.Label(window, text='\nDefinition', bg='grey', fg='white', font='none 12 bold').grid(
        row=4, column=0, sticky='nw', padx = 5, pady = 10)

# create a text output box
output = tk.Text(window, width=75, height=6, wrap='word', background='white')
output.grid(row=5, column=0, columnspan=2, sticky='w', padx=5, pady=10)

# the dictionary 
mydictionary = {
        'giraffe' : 'a large African mammal with a very long neck and forelegs, having a coat patterned with brown patches separated by lighter lines. It is the tallest living animal.',
        'bear' : 'a large, heavy, mammal that walks on the soles of its feet, with thick fur and a very short tail. Bears are related to the dog family but most species are omnivorous.'
        }

#exit label
tk.Label (window, text='Click to Exit:', bg='black', fg='white', font='none 12 bold') .grid(
            row=6, column=3, padx = 5, pady = 10, sticky = 'se')
# exit button
tk.Button (window, text='Exit', width=6, command=close_window).grid(
           row=7, column=3, sticky ='nw',  padx = 5, pady = 10)


# run the main loop ?
window.mainloop()



# if __name__ == '__main__':
#    main()

