import requests, json
import warnings

ip_address = '10.14.0.100'



############################# API ###############################################################################

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


############################# API ###############################################################################


sid = login('WebAPI','Pass1234')
#print("session id: " + sid)


show_hosts_data = {  }
show_hosts_results =  api_call(ip_address, 443,'show-hosts', show_hosts_data ,sid)


#print("saadsadas\n")
#print(show_hosts_results.get("objects"))
print("Registered Web Servers: <br/> <br/>")
hosts_present = show_hosts_results.get("objects")

for host in hosts_present:
    if host.get("name").startswith("Web"):
        print("Nazwa:  " , host.get("name") ,"\tIP:  ",  host.get("ipv4-address"), "<br/>")

print('<br/><br/><br/>')

logout_result = api_call(ip_address, 443,"logout", {},sid)

