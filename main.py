import socket
import mysql.connector

WHOIS_PORT = 43
DB_HOST = 'localhost'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_DATABASE = 'your_database'

def fetch_client_details(ip_address):
    # Connect to the MySQL database
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )

        # Retrieve client details based on the IP address
        cursor = connection.cursor()
        query = "SELECT * FROM clients WHERE ip_address = %s"
        cursor.execute(query, (ip_address,))
        client_data = cursor.fetchone()

        # Close the database connection
        cursor.close()
        connection.close()

        return client_data

    except mysql.connector.Error as error:
        print("Error connecting to the database:", str(error))
        return None

def format_rwhois_response(ip_address):
    client_data = fetch_client_details(ip_address)

    if client_data:
        response = f"""\
%rwhois V-1.5:001ae1:00 rwhois.arin.net (by Network Solutions, Inc. V-1.5.9.6)
network:ID;I:NET-{client_data[0]}
network:Auth-Area:{client_data[1]}
network:Network-Name:{client_data[2]}
network:IP-Network:{client_data[3]}
network:Org-Name:{client_data[4]}
network:Street-Address:{client_data[5]}
network:City:{client_data[6]}
network:State:{client_data[7]}
network:Postal-Code:{client_data[8]}
network:Country-Code:{client_data[9]}
network:Tech-Contact:{client_data[10]}
network:Abuse-Contact:{client_data[11]}
network:Admin-Contact:{client_data[12]}
network:Updated:{client_data[13]}
network:Created:{client_data[14]}
"""
    else:
        response = "No client details found for the provided IP address."

    return response

def handle_whois_request(client_socket, ip_address):
    response = format_rwhois_response(ip_address)

    # Send the response back to the ARIN client
    client_socket.sendall(response.encode())

def start_whois_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('0.0.0.0', WHOIS_PORT))
        server_socket.listen(1)
        print("WHOIS server started on port %d" % WHOIS_PORT)

        while True:
            client_socket, client_address = server_socket.accept()
            print("Connection from: %s" % str(client_address))

            # Receive the IP address from the ARIN client
            data = client_socket.recv(1024).decode()
            ip_address = data.strip()

            # Handle the WHOIS request
            handle_whois_request(client_socket, ip_address)

            client_socket.close()

# Start the WHOIS server
start_whois_server()
