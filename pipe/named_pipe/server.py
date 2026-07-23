import os
import time

FIFO_PATH="/home/dev/Python/pipe/named_pipe/fifo_"

def main():
    if not os.path.exists(FIFO_PATH):
        try:
            os.mkfifo(FIFO_PATH)
            print(f"\nServer created FIFO at path: {FIFO_PATH}")
        except FileExistsError:
            pass

    print("\nReader: Waiting for a writer to open the pipe..")

    with open(FIFO_PATH,"r") as fifo:
        data=fifo.read()
        time.sleep(2)
        print(f"\nReader: Server received data -> {data}")
   
    with open(FIFO_PATH,"w") as fifo:
        message="Bye!"
        fifo.write(message)
        time.sleep(2)
        print(f"\nWriter: Server sent-> {message}")

if __name__=="__main__":
    main()