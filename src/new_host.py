import requests, json
import warnings

ip_address = '10.14.0.100'

warnings.filterwarnings("ignore")
def api_call(ip_addr, port, command, json_payload, sid):
    url = 'https://' + ip_address  + ':' + '443' + '/web_api/' + command
    if sid == '':
        request_headers = {'Content-Type' : 'application/json'}
    else:
        request_headers = {'Content-Type' : 'application/json', 'X-chkp-sid' : sid}
    r = requests.post(url,data=json.dumps(json_payload), headers=request_headers, verify=False)
    return r.json()


def login(user,password):
    payload = {'user':user, 'password' : password}
    response = api_call(ip_address, 443, 'login', payload, '')




    return response["sid"]

sid = login('orchiestra','Pass1234')
print("session id: " + sid)


new_host_data = {'name':'webserwer10', 'ip-address':'192.168.1.1'}
#new_host_result = api_call('192.168.10.145', 443,'add-host', new_host_data ,sid)
#print(json.dumps(new_host_result))

add_to_group_data = {'name': 'Dynamic_Public_WebServers',  'members':  {'add': 'webserwer10'}}
add_to_group_result = api_call(ip_address, 443,'set-group', add_to_group_data ,sid)
print(json.dumps(add_to_group_result))


show_hosts_data = {  }
show_hosts_results =  api_call(ip_address, 443,'show-hosts', show_hosts_data ,sid)


print("saadsadas\n")
print(show_hosts_results.get("objects"))

hosts_present = show_hosts_results.get("objects")

for host in hosts_present:
    if host.get("name").startswith("web"):
        print("Nazwa:  " , host.get("name") ,"\tIP:  ",  host.get("ipv4-address"))



#for x in show_hosts_results:
#    print(x[1])




publish_result = api_call(ip_address, 443,"publish", {},sid)
print("publish result: " + json.dumps(publish_result))

logout_result = api_call(ip_address, 443,"logout", {},sid)
print("logout result: " + json.dumps(logout_result))