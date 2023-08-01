import socket

def start_server():
	#Create a socket object
	s= socket.socket()
	
	#Bind socket to a port
	s.bind(("localhost",8080))
	
	#Listen for incoming connections
	s.listen(1)
	print("Server is listening on port 8080...")
	
	while True:
		#Accept an incoming connection
		conn, addr = s.accept()
		print(f"Connection established with {addr}")
		
		try:
			while True:
				#Receive data from connection,max 1024 byte
				data = conn.recv(1024)
				if not data:
					break
				
				#Convert bytes to string and print received data
				received_message = data.decode('utf-8')
				print(f"Received message: {received_message}")
				
				#Send the received message back to the client
				conn.sendall(data)
				
	    except Exception as e:
			print(f"Error occured : {e}")
		
		finally:
			#Close the connection when done
			conn.close()
			print(f"Connection with {addr} closed.")

if __name__ == "__main__":
	start_server()
