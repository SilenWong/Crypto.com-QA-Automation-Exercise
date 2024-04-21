import requests
class RequestUtil:
    #create a session to manage the execution of testcases
    sess = requests.session()

    #one request function to handle different request method
    def send_request(self,method,url,datas,**kwargs):
        method = str(method).lower()
        res = RequestUtil.sess.request(method=method,url=url,params=datas,**kwargs)
        return res