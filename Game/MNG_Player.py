#!/usr/bin/python

class MNG_Player(object):
    def __init__(self):
        from Utility.Config     import Config
        config_obj              = Config()
        self.__playr1_symbol    = config_obj.get_value('playr1_symbol')
        self.__playr2_symbol    = config_obj.get_value('playr2_symbol')

    def get_player_symbol(self,p_player_no):
        if  p_player_no == 1:
            v_player_symbol = self.__playr1_symbol
        elif    p_player_no == 2:
            v_player_symbol = self.__playr2_symbol
        else:
            v_player_symbol = -1
        return v_player_symbol

    def get_player_dict(self,p_last_player,p_turn_status):
        if      p_last_player == 1 and p_turn_status == 'Move':
            v_player_no             = 1
            v_next_player_no        = 2
        elif    p_last_player == 1 and p_turn_status == 'Done':
            v_player_no             = 2
            v_next_player_no        = 1
        elif    p_last_player == 2 and p_turn_status == 'Move':
            v_player_no             = 2
            v_next_player_no        = 1
        elif    p_last_player == 2 and p_turn_status == 'Done':
            v_player_no             = 1
            v_next_player_no        = 2

        v_player_dict ={}
        v_player_dict['player_no']=v_player_no
        v_player_dict['next_player_no']=v_next_player_no

        return v_player_dict
