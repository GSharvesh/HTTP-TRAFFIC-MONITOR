# HTTP-TRAFFIC-MONITOR
## Overview:

Developed a real-time network packet sniffer in Python using the Scapy library to monitor and analyze live network traffic. The tool captures low-level network packets and extracts useful metadata including:

•	Source and destination IP addresses

•	Source and destination port numbers

•	Communication protocol (TCP, UDP, HTTP)

•	HTTP request details (method, host, URL)

•	Packet count

•	Live timestamped logging to a .txt file

This project simulates the foundational functionality of tools like Wireshark, tailored for educational, debugging, and ethical security auditing purposes.

________________________________________
 ## Technologies Used:
 
•	Python 3

•	Scapy (for packet sniffing and protocol parsing)

•	Raw Sockets & Linux Networking

•	Terminal-based CLI + .txt file logging

________________________________________
## Key Features:

•	Live packet capturing with protocol classification

•	Detection of HTTP traffic with method, host, and URL extraction

•	Tracks and logs packet statistics

•	Logs all activity to an external file (packet_log.txt)

•	Graceful handling and user interrupt support

________________________________________
## Purpose:

To understand and demonstrate:

•	Low-level network data interception

•	Packet structure and protocol dissection (TCP/IP & HTTP layers)

•	Practical implementation of a packet analysis tool

•	The role of raw sockets and permissions in cybersecurity

________________________________________
## Execution:

•	Developed and tested on Linux (Kali) using sudo privileges

•	Output verified using both console and file logging


