import os 
from docs.docx import Docx
# import tkinter as tk
# from ui.tkinter_ui import FileProcessingApp

def main():
    batch = 50
    path2files = "tests2"
    # root = tk.Tk()
    # app = FileProcessingApp(root)
    # root.mainloop()
    files = [os.path.join(path2files, file) for file in os.listdir(path2files) if file.endswith("docx")]
    for file in files:
        docx = Docx(file)
        new_filename = os.path.join("out",f"V2translated_{os.path.basename(file)}")
        docx.rebuild(new_filename, batch)
        print(f"{new_filename} Saved!")
    print("All Done! Thank You!")
    

if __name__ == '__main__':
    main()
