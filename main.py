if __name__ == "__main__":
    for ascii in range(255):
        print(f"{ascii}".rjust(3), " : ", f"{(chr(ascii))}")