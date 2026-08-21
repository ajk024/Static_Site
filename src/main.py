from textnode import *
from builder import *

def main():
        CopyStatic()

        from_path = "/home/akozbial/boot.dev/projects/Static_Site/content/index.md"
        template_path = "/home/akozbial/boot.dev/projects/Static_Site/template.html"
        dest_path = "/home/akozbial/boot.dev/projects/Static_Site/public/index.html"
        generate_page(from_path, template_path, dest_path)

if __name__ == "__main__":
        main()