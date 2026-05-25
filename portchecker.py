import socket

def check_port(host, port):
    try:
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # wait for 2 seconds

        # Try connecting
        result = s.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN on {host}")
        else:
            print(f"Port {port} is CLOSED on {host}")

        s.close()

    except Exception as e:
        print("Error:", e)

# Main program
host = input("Enter host (example: google.com or 127.0.0.1): ")
port = int(input("Enter port number: "))

check_port(host, port)