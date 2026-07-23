import os
import sys

def main():
    try:
        read_fd, write_fd=os.pipe()
    except OSError as e:
        print(f"Failed to create pipe: {e}")
        sys.exit(1)

    print(f"Two end of pipe created.\nReading end: {read_fd}\nWriting end: {write_fd}")

    try:
        pid=os.fork()
    except OSError as e:
        print(f"Fork failed: {e}")
        os.close(read_fd)
        os.close(write_fd)
        sys.exit(1)

    if pid>0:
        print(f"\n-----Inside Parent Process: {os.getpid()}----")

        try:
            os.close(read_fd)   #no need for read_fd here so close it
        except OSError as e:
            print(f"Parent: error closing read_fd: {e}")

        parent_msg="Hello from Parent!"

        try:
            print("\nWriting message in pipe.")
            os.write(write_fd, parent_msg.encode())
        except OSError as e:
            print(f"Parent: error writing to pipe: {e}")
        finally:
            try:
                os.close(write_fd)
            except OSError as e:
                print(f"Parent: error closing write_fd: {e}")

        try:
            os.wait()  # blocks parent until child process finishes
        except ChildProcessError as e:
            print(f"Parent: error waiting for child: {e}")

    else:
        try:
            print(f"\n-----Inside Child Process: {os.getpid()}----")

            try:
                    os.close(write_fd)  # not needed in child
            except OSError as e:
                    print(f"Child: error closing write_fd: {e}")

            try:
                msg_from_parent = os.read(read_fd, 100)
                print(f"\nMessage received from Parent in Child Process: {msg_from_parent.decode()}")
            except OSError as e:
                print(f"Child: error reading from pipe: {e}")
            except UnicodeDecodeError as e:
                print(f"Child: error decoding message: {e}")
            finally:
                try:
                    os.close(read_fd)
                except OSError as e:
                    print(f"Child: error closing read_fd: {e}")
        finally:
            os._exit(0)

if __name__=="__main__":
    main()


