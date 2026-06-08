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
    chunk_size = 1000
    start = 0
    end = 1000
    for text in range(start, end, 1000):
        chunks.append(text[start:end])
       

def chunks(text):
    chunks = []
    chunk_size = 3
    end = len(text)

    for start in range(0, end, chunk_size):
        chunks.append(text[start:start+chunk_size])

    return chunks
    
text = "abcdefghij"
print(chunks(text))
