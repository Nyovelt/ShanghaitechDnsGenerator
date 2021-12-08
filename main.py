from re import U
import dns.resolver

DNS_SERVER_LAN="10.15.44.11" # GeekPie DNS
resolver_lan = dns.resolver.Resolver(configure=False)
resolver_lan.nameservers = [DNS_SERVER_LAN]
DNS_SERVER_WAN="10.15.89.182" # Tencent DNS
resolver_wan = dns.resolver.Resolver(configure=False)
resolver_wan.nameservers = [DNS_SERVER_WAN]
urlPath="url.conf"

def print_lan_hosts(url, resolver):
    answer = resolver.resolve(url, 'A')
    print(answer[0].address, url)

def print_wan_hosts(url, resolver):
    answer = resolver.resolve(url, 'A')
    print(answer[0].address, url)


# Main Start
print("# ShanghaiTech Start")
fp = open(urlPath, "r")
for lines in fp.readlines():
    lines = lines.strip()
    print_lan_hosts(lines, resolver_lan)
    # print_wan_hosts(lines, resolver_wan)
fp.close()
print("# ShanghaiTech End")
