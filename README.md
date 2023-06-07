# PythonRwhois
ARIN RWhois Server with MySQL Integration

The ARIN RWhois Server with MySQL Integration is a project that aims to create a WHOIS server adhering to the ARIN RWhois (Referral Whois) specifications while populating client details from a MySQL database. WHOIS servers provide a means to obtain information about IP addresses and domain names, allowing organizations and individuals to retrieve relevant network registration data.

This project involves building a server that listens on port 43, the standard port for WHOIS queries, and establishes a TCP connection with clients, including ARIN or other WHOIS clients. Upon receiving a connection, the server waits for the client to send an IP address query.

The server then retrieves the client details from a MySQL database using the Python MySQL Connector library. The MySQL database stores information such as network ID, network name, IP range, organization details, contact information, and other relevant network registration data.

Once the client details are fetched, the server constructs a response conforming to the ARIN RWhois format. The response includes key network-related information such as network ID, authentication area, network name, IP network, organization name, address, city, state, postal code, country code, technical contact, abuse contact, administrative contact, and creation/update timestamps.

The constructed response is then sent back to the requesting client, fulfilling the WHOIS query and providing the relevant network registration details in the expected ARIN RWhois format.

This project is designed to provide a foundational implementation of an ARIN RWhois server, allowing for customization and further enhancements based on specific requirements. Integration with a MySQL database ensures dynamic retrieval of client information, allowing the server to provide up-to-date and accurate WHOIS responses.


# Author
Lyron Foster
