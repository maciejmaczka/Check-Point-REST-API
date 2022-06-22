import requests, json
import warnings
import sys

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



print("<br/> </br>Adding new server: <br/> </br>")
new_host_data = {'name':sys.argv[1], 'ip-address':sys.argv[2], 'color' : 'red'}
new_host_result = api_call('192.168.10.145', 443,'add-host', new_host_data ,sid)
print(json.dumps(new_host_result))


print("<br/> </br>Adding to group: <br/> </br>")
add_to_group_data = {'name': 'Public_WebServers',  'members':  {'add': sys.argv[1]}}
add_to_group_result = api_call(ip_address, 443,'set-group', add_to_group_data ,sid)
print(json.dumps(add_to_group_result))

print("<br/> </br>Saving: <br/> </br>")
publish_result = api_call(ip_address, 443,"publish", {},sid)
print(json.dumps(publish_result))

logout_result = api_call(ip_address, 443,"logout", {},sid)
print(json.dumps(logout_result))
