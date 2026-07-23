import os
import time

FIFO_PATH="/home/dev/Python/pipe/named_pipe/fifo_"

def main():
    if not os.path.exists(FIFO_PATH):
        os.mkfifo(FIFO_PATH)
        print(f"\nFIFO Created at path: {FIFO_PATH}")

    print("\nWriter: Waiting for a reader to open the pipe..")

    
    with open(FIFO_PATH,"w") as fifo:
        message="Hello!"
        fifo.write(message)
        print(f"\nWriter: Client sent-> {message}")
    
    
    with open(FIFO_PATH,"r") as fifo:
        data=fifo.read()
        time.sleep(2)
        print(f"\nReader: Client received data -> {data}")

if __name__=="__main__":
    main()