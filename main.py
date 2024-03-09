import dns_network_api as dns_net
import dns_bank_api as dns_bank


def main():
    # Check if network is online
    # while dns_net.network_status() == "Status: Server Is Online":
    # Print current time
    #     print(dns_net.network_time())
    #     if (dns_net.networth_check() != 0) :

    print(dns_net.network_check("101"))
    print(dns_net.network_request("101"))
    print(dns_bank.bank_status())
    print(dns_bank.bank_time())


main()
