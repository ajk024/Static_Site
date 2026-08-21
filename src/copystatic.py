import os
from pathlib import Path
import shutil

def CopyStatic():
    dir = Path(__file__).resolve().parent.parent / "public"

    if Path(dir).exists():
        shutil.rmtree(dir) #delete directory; does not return anything

        if Path(dir).exists():
            raise Exception('"public" directory not deleted')

    if not Path(dir).exists(): #make new directory
        os.mkdir(dir) #does not return anything

    source_dir = Path(__file__).resolve().parent.parent / "static"
    shutil.copytree(source_dir, dir, dirs_exist_ok=True)
        

    
    

  

