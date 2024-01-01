import docx
from tqdm import tqdm
from func.translation import translate

class Docx():
    def __init__(self, path):
        self.path = path
        self.rawdoc = docx.Document(self.path)

    def rebuild(self, name = "translated.docx"):
        SKIP = '1234567890!"№;%:?*),'
        with tqdm(total=len(self.rawdoc.paragraphs) + len(self.rawdoc.tables)) as pbar:
            for i, paragraph in enumerate(self.rawdoc.paragraphs):
                if paragraph.text and paragraph.text not in SKIP:
                    translation = translate(paragraph.text)
                    paragraph.text = translation
                    pbar.update(1)

            for n, table in enumerate(self.rawdoc.tables):
                for i, row in enumerate(table.rows):
                    for j, cell in enumerate(row.cells):
                        if cell.text and cell.text not in SKIP:
                            translation = translate(cell.text)
                            cell.text = translation
                            pbar.update(1)
        self.rawdoc.save(name)
