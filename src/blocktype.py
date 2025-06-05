from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered"
    ORDERED_LIST = "ordered"

def block_to_block_type(block):

    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break   
    if count >= 1 and count <= 6 and block[count] == " ":
        return BlockType.HEADING
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE