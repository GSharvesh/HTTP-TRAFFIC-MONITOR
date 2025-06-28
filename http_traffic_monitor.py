from scapy.all import *
from scapy.layers.http import HTTPRequest, HTTP
import datetime

# Global counter
packet_counter = 0

# Log file
log_file = open("packet_log.txt", "w")

def log_to_file(data):
    log_file.write(data + "\n")
    log_file.flush()

def process_packet(packet):
    global packet_counter
    packet_counter += 1

    src_ip = packet[IP].src if packet.haslayer(IP) else "Unknown"
    dst_ip = packet[IP].dst if packet.haslayer(IP) else "Unknown"
    src_port = packet[TCP].sport if packet.haslayer(TCP) else (packet[UDP].sport if packet.haslayer(UDP) else "N/A")
    dst_port = packet[TCP].dport if packet.haslayer(TCP) else (packet[UDP].dport if packet.haslayer(UDP) else "N/A")
    proto = "TCP" if packet.haslayer(TCP) else ("UDP" if packet.haslayer(UDP) else "Other")
    method = "-"
    host = "-"
    url = "-"

    if packet.haslayer(HTTPRequest):
        http_layer = packet[HTTPRequest]
        method = http_layer.Method.decode() if hasattr(http_layer, 'Method') else "-"
        host = http_layer.Host.decode() if hasattr(http_layer, 'Host') else "-"
        url = http_layer.Path.decode() if hasattr(http_layer, 'Path') else "-"
        proto = "HTTP"

    # Build log string
    log_entry = f"[{datetime.datetime.now()}] Packet #{packet_counter}: {proto} | {src_ip}:{src_port} -> {dst_ip}:{dst_port} | Method: {method} | Host: {host} | URL: {url}"
    
    print(log_entry)
    log_to_file(log_entry)

# Start sniffing
if __name__ == "__main__":
    print("Starting packet capture... (Press Ctrl+C to stop)\n")
    try:
        sniff(prn=process_packet, store=False)
    except KeyboardInterrupt:
        print("\nSniffing stopped.")
        log_file.close()
