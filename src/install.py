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

print("<br/> </br>Commiting changes please wait...  <br/> </br>")
install_data = {'policy-package' : 'standard',   'access' : 'true',   'threat-prevention' : 'false',   'targets' : [ 'vWaw', 'vKRK' ]}
install_results = api_call('192.168.10.145', 443,'install-policy', install_data ,sid)

print(print(json.dumps(install_results)))


logout_result = api_call(ip_address, 443,"logout", {},sid)
print(json.dumps(logout_result))
