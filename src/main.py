import os 
from docs.docx import Docx

def main():
    path2files = "tests"
    files = [os.path.join(path2files, file) for file in os.listdir(path2files)]
    for file in files:
        docx = Docx(file)
        new_filename = f"translated_{os.path.basename(file)}"
        docx.rebuild(new_filename)
        print(f"{new_filename} Saved!")
    print("All Done! Thank You!")

if __name__ == '__main__':
    main()
