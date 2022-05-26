import time

def main():
    while (True):
        res = input_string("Hello World")
        print(res)
        time.sleep(5)

def input_string(str):
    return str

if __name__ == "__main__":
    main()
