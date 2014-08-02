#!/usr/bin/python

class Config(object):

    def get_dict(self):
        v_config_dict = {
'playr1_symbol':'X',
'playr2_symbol':'O',
'empty_spc':'*',
'board_height':3,
'board_width':3,
'board_file_nm':'board.json',
'game_file_nm':'game.json'
        }

        return v_config_dict


    def get_value(self,p_key):
        v_dict = self.get_dict()
        v_value = v_dict[p_key]

        return v_value
