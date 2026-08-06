from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragrah"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(mdblock: str) -> BlockType:
    
    for i in range (len(mdblock)):
        #check for heading
        if mdblock[i] == "#":
            if i+1 < len(mdblock):
                if mdblock[i+1] == " ":
                    return BlockType.HEADING
                elif mdblock[i+1] != "#":
                    raise Exception("Invalid heading block syntax")

        #check for code
        elif mdblock[i] == "`":    #if mdblock[i:i+3] == "```" and mdblock[i+3] == "\n":
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

        elif i == 0:
            #check for quote
            if mdblock[i] == ">":
                return BlockType.QUOTE

            #check for unordered list
            elif mdblock[i] == "-":
                #check that each line starts with "- "; space required
                split_list: list[str] = mdblock.splitlines()
                for item in split_list:
                    if len(item) > 1: 
                        if item[0] != "-" or item[1] != " ":
                            raise Exception("Invalid unordered list block syntax 2")
                    else:
                        raise Exception("Invalid unordered list block syntax 1")
                return BlockType.UNORDERED_LIST

            #check for ordered list
            elif mdblock[i].isdigit():
                #check that each line starts with "<number>. "; space required: list must start at 1 and increment by 1
                split_list: list[str] = mdblock.splitlines()
                last_number: int = 0

                for item in split_list:
                    #extract number from item
                    number: str = ""

                    for i in range (len(item)):
                        if item[i].isdigit():
                            number += item[i]
                        elif not item[i].isdigit():
                            break
                    number = int(number)

                    if number == last_number + 1: #check syntax further
                        last_number = number
                        if len(item) > 2:
                            if not item[0].isdigit():
                                raise Exception("Invalid ordered list block syntax 1")
                            elif item[1].isdigit():
                                raise Exception("Invalid ordered list block syntax 5")
                            elif item[1] != "." or item[2] != " ":
                                raise Exception("Invalid ordered list block syntax 2")
                        else:
                            raise Exception("Invalid ordered list block syntax 3")
                    else:
                        raise Exception("Invalid ordered list block syntax 4")
                return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

                    