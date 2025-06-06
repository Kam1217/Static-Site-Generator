def extract_title(markdown):

    title = ""

    markdown_lines = markdown.split("\n")

    for line in markdown_lines:
        if line.startswith("# "):
            strp_line = line[2: ]
            title = strp_line.strip()
            break
    
    if title == "":
        raise Exception("<h1> title not found")
    
    return title
