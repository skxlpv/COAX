from HelloWorld.ContextManager import FileManager


@staticmethod
def writeWord():
    with FileManager("/HelloWorld/File.txt", "w") as file:
        word = input("Please enter a word to print: ")
        list(word)

        for i in range(len(word)):
            file.write(f"{word[i]}\n")
