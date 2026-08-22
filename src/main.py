from textnode import *
from builder import *

def main():
        CopyStatic()

        base_dir = "/home/akozbial/boot.dev/projects/Static_Site/"

        from_path = base_dir + "content/index.md"
        template_path = base_dir + "template.html"
        dest_path = base_dir + "public/index.html"
        #generate_page(from_path, template_path, dest_path)

        dir_path_content = base_dir + "content/"
        dest_dir_path = base_dir + "public/"
        generate_pages_recursive(dir_path_content, template_path, dest_dir_path)

if __name__ == "__main__":
        main()