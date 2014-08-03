#!/usr/bin/python

import json

class MNG_JSON(object):

    def  __init__(self):
        import os

        v_cur_path  = os.path.dirname(os.path.abspath(__file__))
        self.__path = '%s/JSON' %(v_cur_path)

    def write_json(self,p_file_nm,p_dict):

        v_json_str  = json.dumps(p_dict)
        v_path  = "%s/%s.json"  %(self.__path,p_file_nm)
        file_obj = open(v_path,'w')
        file_obj.write(json.dumps(p_dict))
        file_obj.close

    def get_dict(self,p_file_nm):

        v_path  = "%s/%s.json"  %(self.__path,p_file_nm)
        file_obj = open(v_path,'r')
        v_json_str = file_obj.read()
        file_obj.close
        v_json_dict = json.loads(v_json_str)

        return v_json_dict
