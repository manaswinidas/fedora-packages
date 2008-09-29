from fedora.client import ProxyClient
from Cookie import SimpleCookie
from pylons import request

class MFProxyClient(ProxyClient):
    def __init__(self, base_url, useragent=None, debug=False, return_auth=False):
        super(MFProxyClient, self).__init__(base_url, 
                                            useragent=useragent, 
                                            debug=debug)
        self._return_auth = return_auth
        
    def convert_to_simple_cookie(self, cookie):
        sc = SimpleCookie()
        for key, value in cookie.iteritems():
            sc[key] = value
            
        return sc

    def get_current_proxy_cookies(self):
        cookies = request.cookies
        cookies = self.convert_to_simple_cookie(cookies)
        return cookies
    
    def send_authenticated_request(self, method, req_params=None):
        auth_params = {'cookie': self.get_current_proxy_cookies()}
        result = self.send_request(method,
                                   req_params = req_params,
                                   auth_params = auth_params)
        
        if not self._return_auth:
            result = result[1]
            
        return result

class FasClient(MFProxyClient):
    def __init__(self, baseURL='https://admin.fedoraproject.org/accounts'):
        super(FasClient, self).__init__(baseURL)
    
    def user_list(self, search):
        result = self.send_authenticated_request('user/list/',
                                                 req_params = {'search': search})
        
        return result
    
    def group_list(self, search, groups_only=False):
        result = self.send_authenticated_request('group/list/',
                                                 req_params = {'search': search})
        if groups_only:
            result = {'groups': result['groups']} 
        
        return result
    
    def get_user_info(self, user, full_results=False):
        result = self.send_authenticated_request('user/view/' + user)
        
        return result
    
class PkgdbClient(MFProxyClient):
    def __init__(self, baseURL='https://admin.fedoraproject.org/pkgdb'):
        super(PkgdbClient, self).__init__(baseURL)
        
    def get_package_info(self, name):
        result = self.send_authenticated_request("packages/name", 
                                               req_params={'packageName': name})
        
        return result
    
    def get_user_packages(self, user):
        result = self.send_authenticated_request("users/packages/" + user)
        
        return result
    
class BodhiClient(MFProxyClient):
    def __init__(self, baseURL='https://admin.fedoraproject.org/updates'):
        super(BodhiClient, self).__init__(baseURL)
        
    def get_info(self, package='', get_auth=False):
         result = self.send_authenticated_request("list/",
                                                  req_params={'package': package,
                                                              'get_auth': get_auth}
                                                  )
         return result