#encoding: utf-8

import unittest
import qjson

class qjson_test(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头
    def test_decimal(self):
        self.assertEqual(qjson.loads('{"a":1.7}').a, 1.7, 'test decimal fail')
    
    def test_array(self):
        self.assertEqual(qjson.loads('{"a":["b",1]}').a, ["b", 1], 'test decimal fail')
    
    def test_string(self):
        self.assertEqual(qjson.loads('{"a":"b"}').a, "b", 'test decimal fail')
    
    def test_complex(self):
        json_str = '{"person":\
            {"name":"jerry", "age":32, "web":{"url":"http://jatsz.org", "desc":"blog"}}, \
            "grade": "a", "score":[80,90]}'
        info = qjson.loads(json_str)

        self.assertEqual(info.person.name, 'jerry', 'test_complex fail')
        self.assertEqual(info.person.age, 32, 'test_complex fail')
        self.assertEqual(info.person.web.url, "http://jatsz.org", 'test_complex fail')
        self.assertEqual(info.person.web.desc, "blog", 'test_complex fail')

        self.assertEqual(info.grade, "a", 'test_complex fail')
        self.assertEqual(info.score, [80, 90], 'test_complex fail')
        
        
if __name__ =='__main__':
    unittest.main()