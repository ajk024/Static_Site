from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragrah"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(mdblock: str) -> BlockType:
    
    #check for heading
    if mdblock[0] == "#":
        i = 1
        while i < len(mdblock) and mdblock[i] == "#":
            i += 1
        if mdblock[i] == " ":
            return BlockType.HEADING
        else:
            raise Exception("Invalid heading block syntax")

    #check for code
    elif mdblock.startswith("```"):
        if not mdblock.startswith("```\n"):
            raise Exception("Invalid code block syntax 1")
        i = 4
        while i < len(mdblock) and mdblock[i] != "`":
            i += 1
        if (
            i+2 < len(mdblock)
            and mdblock[i:i+3] == "```"
        ):
            return BlockType.CODE
        raise Exception("Invalid code block syntax 2")
        

    #check for quote
    elif mdblock[0] == ">":
        return BlockType.QUOTE

    #check for unordered list
    elif mdblock[0] == "-":
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
    elif mdblock[0].isdigit():
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

                    