from textnode import TextNode, TextType


def main():
    node_one = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node_one)

if __name__ == "__main__":
    main()