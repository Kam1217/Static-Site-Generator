def markdown_to_blocks(doc):
    blocks = doc.split("\n\n")
    result = []

    for block in blocks:
        stripped = block.strip()
        if stripped:
            result.append(stripped)
    
    return result
