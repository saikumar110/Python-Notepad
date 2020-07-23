import tkinter as tk
from tkinter import ttk
import os
from tkinter import font, colorchooser, filedialog, messagebox

main_appliction = tk.Tk()
main_appliction.geometry('1200x650')
main_appliction.title('PY-PAD')

'''
<--------------------------------------------------MAIN_MENU--------------------------------------->
'''
main_menu = tk.Menu()

# file-menu icons
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

file = tk.Menu(main_appliction, tearoff=False)

# Edit icons
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit = tk.Menu(main_appliction, tearoff=False)

# view ICons
toolbar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
statusbar_icon = tk.PhotoImage(file='icons2/status_bar.png')

View = tk.Menu(main_appliction, tearoff=False)

# color Themes
light_default_color = tk.PhotoImage(file='icons2/light_default.png')
light_plus_color = tk.PhotoImage(file='icons2/light_plus.png')
dark_color = tk.PhotoImage(file='icons2/dark.png')
red_color = tk.PhotoImage(file='icons2/red.png')
monokai_color = tk.PhotoImage(file='icons2/monokai.png')
nightblue_color = tk.PhotoImage(file='icons2/night_blue.png')

theme_choice = tk.StringVar()
color_icons = (light_default_color, light_plus_color, dark_color, red_color, monokai_color, nightblue_color)
color_dict = {
    '	': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2')

}
count = 0


# function to change theme
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)


color = tk.Menu(main_appliction, tearoff=False)
for i in color_dict:
    color.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT,
                          command=change_theme)
    count += 1

# cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=View)
main_menu.add_cascade(label='Color Theme', menu=color)

'''
<--------------------------------------------------END  MAIN_MENU--------------------------------------->
'''

'''
<--------------------------------------------------TOOL-BAR --------------------------------------->
'''

toolbar = tk.Label(main_appliction)
toolbar.pack(side=tk.TOP, fill=tk.X)

# font box
font_tuplw = tk.font.families()
font_familiy_selected = tk.StringVar()
fontbox = ttk.Combobox(toolbar, width=30, textvariable=font_familiy_selected, state='readonly')
fontbox['values'] = font_tuplw
fontbox.current(font_tuplw.index('Arial'))
fontbox.grid(row=0, column=0, padx=5, pady=5)

# font size box
font_size_selected = tk.IntVar()
font_size = ttk.Combobox(toolbar, width=14, textvariable=font_size_selected, state='readonly')
font_size['values'] = tuple(range(8, 81))
font_size.current(0)
font_size.grid(row=0, column=1, padx=5, pady=5)

## bold button
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(toolbar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

## italic button 
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(toolbar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

## underline button 
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(toolbar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

## font color button 
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(toolbar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

## align left 
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(toolbar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

## align center 
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(toolbar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

## align right 
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(toolbar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

'''
<--------------------------------------------------END-TOOL-BAR --------------------------------------->
'''
# "<---------------------------------------------------TEXT-EDITOR----------------------->"

text_editor = tk.Text(main_appliction)
text_editor.config(wrap='word', relief=tk.FLAT)

scrool_bar = tk.Scrollbar(main_appliction)
text_editor.focus_set()
scrool_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scrool_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scrool_bar.set)

# font size and fontstyle/familiy functionality

current_fontfamiliy = "Arial"
current_fontsize = 12


def changefont(main_appliction):
    global current_fontfamiliy, current_fontsize
    current_fontfamiliy = fontbox.get()
    text_editor.configure(font=(current_fontfamiliy, current_fontsize))


def change_font_size(main_appliction):
    global current_fontfamiliy, current_fontsize
    current_fontsize = font_size.get()
    # fontsize=font_size.get()
    text_editor.configure(font=(current_fontfamiliy, current_fontsize))


fontbox.bind("<<ComboboxSelected>>", changefont)
font_size.bind("<<ComboboxSelected>>", change_font_size)


# bold function
def bold_function():
    textproperty = tk.font.Font(font=text_editor['font'])
    if textproperty.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_fontfamiliy, current_fontsize, 'bold'))
    if textproperty.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_fontfamiliy, current_fontsize, 'normal'))


bold_btn.configure(command=bold_function)


# italic function
def italic_function():
    textproperty = tk.font.Font(font=text_editor['font'])
    if textproperty.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_fontfamiliy, current_fontsize, 'italic'))
    if textproperty.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_fontfamiliy, current_fontsize, 'normal'))


italic_btn.configure(command=italic_function)


# underline function
def underline_function():
    textproperty = tk.font.Font(font=text_editor['font'])
    if textproperty.actual()['underline'] == 0:
        text_editor.configure(font=(current_fontfamiliy, current_fontsize, 'underline'))
    if textproperty.actual()['underline'] == 1:
        text_editor.configure(font=(current_fontfamiliy, current_fontsize, 'normal'))


underline_btn.configure(command=underline_function)


# font_colour_function
def font_color():
    color_var = colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=font_color)


# Align-left function
def align_left():
    textcontent = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, textcontent, 'left')


align_left_btn.configure(command=align_left)


# Align-left function
def align_center():
    textcontent = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, textcontent, 'center')


align_center_btn.configure(command=align_center)


def align_right():
    textcontent = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, textcontent, 'right')


align_right_btn.configure(command=align_right)

# status bar
status_bar = tk.Label(main_appliction, text="status bar")
status_bar.pack(side=tk.BOTTOM)


# status bar count value
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)


text_editor.bind('<<Modified>>', changed)

# add commands to file menu

# variable
url = ''


# function for new_file
def newfile(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)


file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+n', command=newfile)


# function for open_file
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='select file',
                                     filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r+') as file_read:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, file_read.read())
    except FileNotFoundError:

        return


file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+o', command=open_file)


# function for save_file
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                           filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return


file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+s', command=save_file)


# function for save_as_file
def save_as_file(event=None):
    global url
    content = text_editor.get(1.0, tk.END)
    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                   filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    url.write(content)
    url.close()


file.add_command(label='Save as', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+alt+s', command=save_as_file)


# function for save_as_file
## exit functionality

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_appliction.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                   filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_appliction.destroy()
            elif mbox is False:
                main_appliction.destroy()
        else:
            main_appliction.destroy()
    except:
        return


file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+e', command=exit_func)

# add commands to edit  menu

edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+c',
                 command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+v',
                 command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+x',
                 command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear', image=clear_icon, compound=tk.LEFT, accelerator='Ctrl+c',
                 command=lambda: text_editor.delete(1.0, tk.END))


# find function
def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0, 0)

    # frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    # labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    # button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    # entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    # button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()


edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+f', command=find_func)

# add commands to View menu

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar = False
    else :
        text_editor.pack_forget()
        status_bar.pack_forget()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


View.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=False, variable=show_toolbar, image=toolbar_icon, compound=tk.LEFT,
                 command=hide_toolbar)
View.add_checkbutton(label='Status Bar', onvalue=True, offvalue=False, variable=show_statusbar, image=statusbar_icon,
                 compound=tk.LEFT, command=hide_statusbar)

main_appliction.config(menu=main_menu)

main_appliction.bind("<Control-n>", newfile)
main_appliction.bind("<Control-o>", open_file)
main_appliction.bind("<Control-s>", save_file)
main_appliction.bind("<Control-Alt-s>", save_as_file)
main_appliction.bind("<Control-q>", exit_func)
main_appliction.bind("<Control-f>", find_func)

main_appliction.mainloop()
