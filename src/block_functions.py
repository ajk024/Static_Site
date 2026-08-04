from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragrah"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(mdblock: str) -> BlockType:
    hash_count: int = 0
    backtick_count: int = 0

    for char in mdblock:
        #check for heading
        if char == "#":
            hash_count += 1
        

        if hash_count > 0 and hash_count < 7: #headings start with 1-6 #
            return BlockType.HEADING

        #check for code
        if char == "`":
            backtick_count += 1
        elif char != "`":
            break

        if backtick_count == 3:
            ...

