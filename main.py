from tkinter import *
from tkinter.scrolledtext import ScrolledText
import Parser
import Compiler
import SemanticErrorDetector
from subprocess import call
from tkinter import filedialog

global input_labels
input_labels = []
global entries
entries = {}
# Compile souce code
def compile(ast=None):
    # Set the text box to editable
    compiled_code_text_box.config(state=NORMAL)

    # Try to parse the source
    try:
        if ast is None:
            ast = Parser.parse(source_code_text_box.get(1.0, END), verbose=False)
            SemanticErrorDetector.check_semantic_error(ast)

    # If there are compile errors display them out
    except Exception as e:
        compiled_code_text_box.delete(1.0, END)
        compiled_code_text_box.insert(INSERT, e)
        run_button.config(state=DISABLED)
    # Display compiled code
    else:
        global result_
        result_ = Compiler.compile(ast)
        Compiler.get_variable(ast)

        # Combine the code with other parts to create a program
        global input_variables
        global result
        global input_code
        global output_code
        global subtract_function
        global pre_declare
        global output
        
        # if len(input_labels) > 0:
        #     for label in input_labels:
        #         label.destroy()
        #         input_labels.remove(label)
        # if len(entries) > 0:
        #     for key, value in entries.items():
        #         value.destroy()
        print(input_labels)
        input_code, input_variables = Compiler.require_input()
        output_code, output = Compiler.output_variables()
        subtract_function = Compiler.define_subtract()
        pre_declare = Compiler.pre_declare_variables()
        result = "" \
                 +"#--------Redefine subtract function--------\n\n" \
                 + subtract_function \
                 + "\n#--------Safe pre declare variables--------\n\n" \
                 + pre_declare \
                 + "\n#-----------Input requirer code------------\n\n" \
                 + input_code \
                 + "\n#-----------Compiled code------------\n\n" \
                 + result_ + "\n#-----------Output variables code------------\n\n" \
                 + output_code + "\n#-----------End-------------\n\n" \
                 + save_output(output)
        display = "\n#-----------Compiled code------------\n\n" + result_
        
        row_ = 5
        
        if len(input_variables) > 0:
            input_variables.sort()
            for variable in input_variables:
                label = Label(sub_frame, text="Enter value for " + variable + ": ")
                label.grid(row=row_, column=0)
                entries[variable] = Entry(sub_frame)
                entries[variable].grid(row=row_, column=1)
                row_ += 1

        else:
            # Save result code to temp file
            save_result(result)

            # Enable run button
            run_button.config(state=NORMAL)

        compiled_code_text_box.delete(1.0, END)
        compiled_code_text_box.insert(INSERT, display)
        print(input_labels)
        print(entries)
        print(input_variables)
        

    finally:

        # Set the text box to read only
        compiled_code_text_box.config(state=DISABLED)


# Save compiled result code to temp file
def save_result(text):
    file = open("temp.py", 'w')
    file.write(text)
    file.close()


# Load the source code from file
def get_input():
    file_path = filedialog.askopenfilename()
    file = open(file_path, 'r')
    source_code_text_box.delete(1.0, END)
    source_code_text_box.insert(INSERT, file.read())
    file.close()

# Load the output 
def get_output():
    file = open('output.txt', 'r')
    output_display_box.delete(1.0, END)
    output_display_box.insert(INSERT, file.read())
    file.close()

def save_output(output):
    output = 'with open(\'output.txt\', \'w\') as f:\n' \
            + '    f.write(f\"' + output + "\"" + ')\n' \
            + '    f.close()'
    return output

#Get input on screen display
def get_input_on_screen():
    global values
    values = {}
    input_ = ""
    for variable in input_variables:
        values[variable] = entries[variable].get()
        input_ += variable + "=" + str(values[variable]) + "\n"
    result = "" \
                 +"#--------Redefine subtract function--------\n\n" \
                 + subtract_function \
                 + "\n#--------Safe pre declare variables--------\n\n" \
                 + pre_declare \
                 + "\n#-----------Input requirer code------------\n\n" \
                 + input_ \
                 + "\n#-----------Compiled code------------\n\n" \
                 + result_ + "\n#-----------Output variables code------------\n\n" \
                 + output_code + "\n#-----------End-------------\n\n" \
                 + save_output(output)

    # Save result code to temp file
    save_result(result)

    # Enable run button
    run_button.config(state=NORMAL)
     


# Run compiled code
def run():
    call("python temp.py", shell=True)
    get_output()


#Setup UI
root = Tk()
root.configure(bg="#F0F0F0")

title_font = ("Helvetica", 16, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 12)

Label(root, text="Bare Bones Compiler", font=title_font, bg="#F0F0F0").grid(row=0, column=0, columnspan=2, pady=10)

open_file_button = Button(root, text="Open", font=button_font, bg="#4da6ff", command=get_input)
open_file_button.grid(row=1, column=0)

compiler_button = Button(root, text="Compile", font=button_font, bg="#4da6ff", command=compile)
compiler_button.grid(row=1, column=1)

Label(root, text="Source code", font=label_font, bg="#F0F0F0").grid(row=2, column=0)
Label(root, text="Process", font=label_font, bg="#F0F0F0").grid(row=2, column=1)

source_code_text_box = ScrolledText(root, width=50, height=20)
source_code_text_box.grid(row=3, column=0)

compiled_code_text_box = ScrolledText(root, width=50, height=20)
compiled_code_text_box.grid(row=3,column=1)

run_button = Button(root,text="Run",font=button_font,bg="#4da6ff",command=run)
run_button.grid(row=4,column=1,pady=10)


Label(root,text="Input",font=label_font,bg="#F0F0F0").grid(row=5,column=0)
Label(root,text="Output",font=label_font,bg="#F0F0F0").grid(row=5,column=1)

sub_frame = Frame(root)
sub_frame.grid(row=6,column=0)
   

output_display_box = ScrolledText(root, width=50, height=15)
output_display_box.grid(row=6,column=1)

input_button = Button(root,text="Get Input",font=button_font,bg="#4da6ff",command=get_input_on_screen)
input_button.grid(row=7,column=0,pady=10)

root.title("BareBones Compiler")
root.mainloop()