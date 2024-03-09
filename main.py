import dns_network_api as dns_net
import dns_bank_api as dns_bank


def main():
    result = dns_net.network_status()
    serverTime = dns_net.network_time()
    print(result, serverTime)
    print(dns_bank.bank_status())


main()
