from textnode import TextNode, TextType
import os

def copy_static(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        raise Exception(f"Source directory '{src_dir}' does not exist")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    contents = os.listdir(src_dir)
    for item in contents:
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            #os.mkdir(dest_path)
            copy_static(src_path, dest_path)
    
    

def main():
    node_one = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node_one)



if __name__ == "__main__":
    main()