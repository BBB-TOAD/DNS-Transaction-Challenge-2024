import dns_network_api as dns_net
import dns_bank_api as dns_bank
import time
import socket

res = """
Card Data: {8734844245014478364
4227829629}
Price: {22}
Time: 2024-03-09 15:17:05
"""
# def main():
#     # Check if network is online
#     while dns_net.network_status() == "Status: Server Is Online":
#         # Print current time
#         print(dns_net.network_time())
#         # Check if there is an unopened packet
#         if dns_net.network_check("101") != "Check: 101: 0":
#             # If there is an unopened packet
#             # Make a request
#             req = dns_net.network_request("101")
#             # Make a transaction
#             # dns_bank.transfer(
#             #     req.account_from, req.account_to, secure_code, req["Price"]
#             # )
#         time.sleep(100)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("204.83.169.199", 25542)
client_socket.sendto("request\n101".encode(), server_address)
buffer, _ = client_socket.recvfrom(1024)
received_data = buffer.decode()
req = print(res.split("\n"))
# main()
