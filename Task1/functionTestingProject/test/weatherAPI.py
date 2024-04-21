import pytest
from test.request_util import RequestUtil
from test.yaml_util import read_yaml

class TestWeather:
    #put testcase of yaml file into args_name
    @pytest.mark.parametrize("args_name", read_yaml('testcase.yaml'))

    #get different value of testcase by args_name
    def test_current_weather_report(self,args_name):
        url = args_name['request']['url']
        data = args_name['request']['data']
        method = args_name['request']['method']

        #call request function
        res = RequestUtil().send_request(method=method,url=url,datas=data)
        #print the response
        print(res.json())