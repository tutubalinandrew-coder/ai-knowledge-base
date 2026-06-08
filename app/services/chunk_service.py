

def chunk_text(
    text: str,
    chunk_size: int = 200,
    overlap: int = 50,
) -> list[str]:
    if chunk_size <= overlap:
        raise ValueError("overlap must be less than chunk_size")
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if overlap < 0:
        raise ValueError("overlap must be non-negative")
    chunks = []
    words = text.split()
    step = chunk_size - overlap
    end = len(words)
    for start in range (0, end, step):
        chunk =' '.join(words[start:start+chunk_size])
        chunks.append(chunk)
    return chunks
        
        


