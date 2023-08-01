import socket
import ssl
import threading

def handle_client(conn, addr):
	try:
		#Wrap the connection in an SSL context
		ssl_conn = ssl.wrap_socket(conn,
										certfile = "server.crt"
										keyfile = "server.key"
										ssl_version =ssl.PROTOCOL_TLSv1)
		
		#Send data to connection
		ssl_conn.send(b"Hello World")
		
		#Receive data from connection
		data= ssl_conn.recv(1024)
		print(f"Received from  {addr}: {data.decode()}")
		
	except Exception as e:
		print(f"Error handling client {addr}: {e}")
		
	finally:
		#Close the connection
		ssl_conn.close()
		
def main():
	try:
		#Create a socket object
		s = socket.socket()
		
		#Bind the socket to a port
		s.bind(("localhost",8080))
		
		#Listen for incoming connections
		s.listen()
		
		print("Server started. Listening for incoming connections")
		
		while True:
			#Accept an incoming connection
			conn, addr = s.accept()
			
			#Create a new thread to handle the client
			client_thread = threading.Thread(target=handle_client, args=(conn, addr))
			client_thread.start()
			
	except KeyboardInterrupt:
		print("Server terminated by user")
		
	except Exception as e:
		print(f"Error has occured: {e}")
	
	finally:
		s.close()
		
if __name__="__main__":
	main()
