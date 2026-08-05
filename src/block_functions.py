from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragrah"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(mdblock: str) -> BlockType:
  
    backtick_count: int = 0

    #for char in mdblock:
    for i in range (len(mdblock)):
        #check for heading
        if mdblock[i] == "#":
            if i+1 < len(mdblock):
                if mdblock[i+1] == " ":
                    return BlockType.HEADING
                elif mdblock[i+1] != "#":
                    raise Exception("Invalid heading block syntax")

        #check for code
        if mdblock[i] == "`":    #if mdblock[i:i+3] == "```" and mdblock[i+3] == "\n":
            if i+1 < len(mdblock):
                if i == 2 and mdblock[i+1] == "\n": 
                    i += 1
                    while i < len(mdblock) and mdblock[i] != "`":
                        i += 1
                    if i+2 < len(mdblock): #check for 3 additional backticks
                        if mdblock[i] == "`" and mdblock[i+1] == "`" and mdblock[i+2] == "`":
                            return BlockType.CODE
                    raise Exception("Invalid code block syntax 2")
                elif mdblock[i+1] != "`":
                    raise Exception("Invalid code block syntax 1")

        #check for quote
        if mdblock[i] == ">":
            return BlockType.QUOTE

        #check for unordered list
        if mdblock[i] == "-":
            ...



    

      
