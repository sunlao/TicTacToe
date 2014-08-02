#!/usr/bin/python

import json

class MNG_JSON(object):

    def  __init__(self):
        from Config             import Config
        config_obj              = Config()

        self.__board_file_nm    = config_obj.get_value('board_file_nm')
        self.__game_file_nm     = config_obj.get_value('game_file_nm')

    def write_json(self,p_type,p_dict):

        if      p_type == 'board':
            v_file_nm = self.__board_file_nm
        elif    p_type == 'game':
            v_file_nm = self.__game_file_nm
        v_json_str  = json.dumps(p_dict)
        file_obj = open(v_file_nm,'w')
        file_obj.write(json.dumps(p_dict))
        file_obj.close

    def get_dict(self,p_type):

        if      p_type == 'board':
            v_file_nm = self.__board_file_nm
        elif    p_type == 'game':
            v_file_nm = self.__game_file_nm
        file_obj = open(v_file_nm,'r')
        v_json_str = file_obj.read()
        file_obj.close
        v_json_dict = json.loads(v_json_str)

        return v_json_dict
