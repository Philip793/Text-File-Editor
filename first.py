import os
import tkinter as tk
from tkinter import messagebox


def save_selected_file():
    # Get selected file from the listbox
    selected_indices = file_listbox.curselection()
    if not selected_indices:
        messagebox.showinfo("No selection", "Please select a file to save.")
        return
    
    if len(selected_indices) > 1:
        messagebox.showinfo("Multiple selection", "Please select only one file to save.")
        return

    # Only one file should be selected
    index = selected_indices[0]
    filename = file_listbox.get(index)

    try:
        # Get content from the text area
        content = text_area.get("1.0", tk.END)
        
        # Save to the file (overwrite)
        with open(filename, 'w') as file:
            file.write(content)
        
        messagebox.showinfo("Saved", f"{filename} has been saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save {filename}: {e}")


def load_selected_file():
    selected_indices = file_listbox.curselection()
    if not selected_indices:
        messagebox.showinfo("No selection", "Please select a file to open.")
        return

    index = selected_indices[0]
    filename = file_listbox.get(index)

    for index in selected_indices:
        filename = file_listbox.get(index)
        try:
            with open(filename, 'r') as file:
                content = file.read()
                text_area.delete("1.0", tk.END) 
                text_area.insert(tk.END, content) 
                root.title(f"Text File Browser and Editor ({filename})")  
        except Exception as e:
            messagebox.showerror("Error", f"Could not open {filename}: {e}")



# Initialize GUI
root = tk.Tk()
root.title(f"Text File Browser and Editor")
root.geometry("700x500")

# Frame for file list
left_frame = tk.Frame(root)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

# Label and Listbox
tk.Label(left_frame, text="Select Text File(s):").pack()
file_listbox = tk.Listbox(left_frame, selectmode="single", height=20, width=40)
file_listbox.pack()

# Populate Listbox with .txt files in current directory
for filename in os.listdir():
    if filename.endswith(".txt"):
        file_listbox.insert(tk.END, filename)

# Load button
tk.Button(left_frame, text="Open Selected", command=load_selected_file, width=20).pack(pady=5)
tk.Button(left_frame, text="Save", command=save_selected_file, width=20).pack(pady=5)

# Text display area
text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both", padx=10, pady=10)

root.mainloop()