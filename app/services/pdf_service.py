from pypdf import PdfReader

def extract_text_from_pdf(file_path: str):
    reader = PdfReader(file_path)
    pages = reader.pages
    text = ''
    
    for page in pages:
        text_from_page = page.extract_text()
        if text_from_page:
            text += text_from_page + '\n\n'
        else:
            continue
        
    

    return text

def chunk(text):
    chunks = []
    start = 0
    end = 1000
    for text in range(start, end, 1000):
        chunks = text[start:end]
        start += 1000
        end += start + 1000
        

    

    return chunks