import paramiko
import psutil
import time
import os
import socket
import sys
import datetime
import getpass

# SSH connection details
print("Please Provide your Hostname and login credentials!!\n")
hostname = input("Enter hostname OR Public IP: ")
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")


# Create an SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server
    ssh_client.connect(hostname, username=username, password=password)
    print("Successfully authenticated to the server.")
    # Get server hostname and IP address
    server_hostname = ssh_client.exec_command("hostname")[1].read().decode().strip()
    server_ip = socket.gethostbyname(hostname)
    print(f"Server Hostname: {server_hostname}")
    print(f"Server IP Address: {server_ip}")

    prev_net_io = psutil.net_io_counters()

    while True:
        # Get timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)

        # Get memory usage
        virtual_memory = psutil.virtual_memory()
        total_memory = virtual_memory.total
        available_memory = virtual_memory.available
        used_memory = virtual_memory.used
        memory_usage = virtual_memory.percent
        cached_memory = total_memory - available_memory  # Calculate cached memory
        swap_memory = psutil.swap_memory()
        swap_used = swap_memory.used
        swap_total = swap_memory.total

        # Get network I/O counters
        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent
        bytes_received = net_io.bytes_recv
        net_io_change_sent = bytes_sent - prev_net_io.bytes_sent
        net_io_change_received = bytes_received - prev_net_io.bytes_recv
        prev_net_io = net_io

        # Clear the terminal
        os.system("cls" if os.name == "nt" else "clear")

        # Print updated usage values
        print("\033[1;36mServer Usage Monitoring\033[0m")
        print("-----------------------")
        print(f"\033[1;37mServer: {server_hostname} ({server_ip})\033[0m")
        print(f"\033[1;33mTimestamp: {timestamp}\033[0m")
        print(f"CPU Usage: \033[1;32m{cpu_usage:.2f}%\033[0m")
        print(f"Total Memory: \033[1;35m{total_memory / 1024 / 1024:.2f} MB\033[0m")
        print(f"Available Memory: \033[1;34m{available_memory / 1024 / 1024:.2f} MB\033[0m")
        print(f"Used Memory: {used_memory / 1024 / 1024:.2f} MB")
        print(f"Cached Memory: {cached_memory / 1024 / 1024:.2f} MB")
        print(f"Memory Usage: \033[1;31m{memory_usage:.2f}%\033[0m")
        print(f"Bytes Sent: {bytes_sent / 1024 / 1024:.2f} MB")
        print(f"Bytes Received: {bytes_received / 1024 / 1024:.2f} MB")
        print(f"Network I/O Change (Sent): {net_io_change_sent / 1024 / 1024:.2f} MB")
        print(f"Network I/O Change (Received): {net_io_change_received / 1024 / 1024:.2f} MB")
        print(f"Swap Used: {swap_used / 1024 / 1024:.2f} MB")
        print(f"Swap Total: {swap_total / 1024 / 1024:.2f} MB")
        print("Press 'q' to stop monitoring.")

        try:
            if sys.stdin.isatty():
                if sys.platform == "win32":
                    import msvcrt
                    if msvcrt.kbhit() and msvcrt.getch() == b'q':
                        break
                else:
                    import termios
                    import atexit
                    import select
                    import tty

                    def is_data():
                        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

                    def read_key():
                        return sys.stdin.read(1)

                    fd = sys.stdin.fileno()
                    old_settings = termios.tcgetattr(fd)
                    atexit.register(termios.tcsetattr, fd, termios.TCSADRAIN, old_settings)
                    tty.setcbreak(sys.stdin.fileno())
                    if is_data():
                        if read_key() == "q":
                            break 
        except (ImportError, ModuleNotFoundError):
            pass

        time.sleep(0.5)  # Pause for a few seconds before the next iteration

except KeyboardInterrupt:
    pass
except paramiko.AuthenticationException:
    print("Connection failed. Authentication error.")
except Exception as e:
    print(f"An error occurred: {e}")

# Close the SSH connection gracefully
try:
    ssh_client.close()
except:
    pass

print("Monitoring stopped.")
