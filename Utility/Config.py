#!/usr/bin/python

class Config(object):

    def __init__(self):
        from MNG_JSON       import MNG_JSON
        self.__json_obj     = MNG_JSON()

    def get_def_dict(self):
        v_config_dict = {
'playr1_symbol':'X',
'playr2_symbol':'O',
'empty_spc':'*',
'board_height':3,
'board_width':3,
'board_file_nm':'board.json',
'game_file_nm':'game.json',
'app_dir':'default'
        }

        return v_config_dict

    def get_dict(self):
        try:
            v_dict = self.__json_obj.get_dict('config')
        except:
            v_def_dict = self.get_def_dict()
            self.__json_obj.write_json('config',v_def_dict)
            v_dict = self.__json_obj.get_dict('config')

        return v_dict

    def post_key_pair(self,p_key,p_value):
        if  self.get_value(p_key)!=p_value:
            v_dict = self.get_dict()
            v_dict[p_key]=p_value
            self.__json_obj.write_json('config',v_dict)

    def get_value(self,p_key):
        v_dict = self.get_dict()
        v_value = v_dict[p_key]

        return v_value
