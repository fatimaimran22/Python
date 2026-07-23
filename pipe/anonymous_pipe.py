import os

def main():
    read_fd, write_fd=os.pipe()
    print(f"Two end of pipe created.\nReading end: {read_fd}\nWriting end: {write_fd}")

    pid=os.fork()

    if pid>0:
        print(f"\n-----Inside Parent Process: {os.getpid()}----")
        os.close(read_fd)   #no need for read_fd here so close it

        parent_msg="Hello from Parent!"

        print("\n Writing message in pipe.")
        os.write(write_fd,parent_msg.encode())

        os.close(write_fd)

        os.wait()   #blocks parent until child process finishes

    else:
        print(f"\n-----Inside Child Process: {os.getpid()}----")

        os.close(write_fd)  #close writing end no need for it

        msg_from_parent=os.read(read_fd,100)

        print(f"\nMessage received from Parent in Child Process: {msg_from_parent.decode()}")

        os.close(read_fd)

if __name__=="__main__":
    main()


