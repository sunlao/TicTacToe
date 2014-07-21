#!/usr/bin/python

class Config(object):

    def get_config_dict(self):
        v_config_dict = {
'playr1_symbol':'X',
'playr2_symbol':'O',
'empty_spc':'*',
'board_height':3,
'board_width':3
        }

        return v_config_dict


    def get_config_value(self,p_key):
        v_value = self.v_config_dict[p_key]

        return v_value
