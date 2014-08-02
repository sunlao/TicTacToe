#!/usr/bin/python

class MNG_Board(object):

    def __init__(self):
        from Config             import Config
        from MNG_JSON           import MNG_JSON
        from MNG_Player         import MNG_Player
        from MNG_Game_Status    import MNG_Game_Status

        config_obj              = Config()
        self.__json_obj         = MNG_JSON()
        self.__player_obj       = MNG_Player()
        self.__game_status_obj  = MNG_Game_Status()

        self.__board_width      = config_obj.get_value('board_width')
        self.__board_height     = config_obj.get_value('board_height')
        self.__empty_spc        = config_obj.get_value('empty_spc')

    def get_new_board(self):
        v_board_dict    = {}
        v_game_dict     = {}
        v_game_dict['game status']='ACT'
        v_game_dict['last player']=1
        v_game_dict['turn status']='Move'
        v_height_loop   = 0
        while v_height_loop <= self.__board_height:
            v_row_dict      = {}
            v_width_loop    = 0
            while v_width_loop <= self.__board_width:
                if v_height_loop == 0:
                    if v_width_loop == 0:
                        v_row_dict[0]='#'
                    else:
                        v_row_dict[v_width_loop]=v_width_loop
                else:
                    if v_width_loop == 0:
                        v_row_dict[0]=v_height_loop
                    else:
                        v_row_dict[v_width_loop] = self.__empty_spc
                v_width_loop    = v_width_loop+1
            v_board_dict[v_height_loop]=v_row_dict
            v_height_loop = v_height_loop+1

        self.__json_obj.write_json('board',v_board_dict)
        self.__json_obj.write_json('game',v_game_dict)
        self.print_board()

    def print_board(self):
        v_board_dict = self.__json_obj.get_json('board')
        v_height_loop   = 0
        while v_height_loop <= self.__board_height:
            v_dict_row  = v_board_dict[str(v_height_loop)]
            v_width_loop    = 0
            v_print_row     = ""
            while v_width_loop <= self.__board_width:
                v_col = v_dict_row[str(v_width_loop)]
                v_print_row = "%s  %s" %(v_print_row,v_col)
                v_width_loop    = v_width_loop+1
            print "%s\n" %(v_print_row.strip(' | '))
            v_height_loop = v_height_loop+1

    def get_board_value(self,p_row,p_col):
        v_board_dict = self.__json_obj.get_json('board')
        v_row_dict  = v_board_dict[str(p_row)]
        v_val       = v_row_dict[str(p_col)]

        return v_val

    def post_board(self,p_row,p_col):
        v_board_dict        = self.__json_obj.get_json('board')
        v_game_dict         = self.__json_obj.get_json('game')
        v_last_player       = v_game_dict['last player']
        v_turn_status       = v_game_dict['turn status']
        v_player_dict       = self.__player_obj.get_player_dict(v_last_player,v_turn_status)
        v_player_no         = v_player_dict['player_no']
        v_player_symbol     = self.__player_obj.get_player_symbol(v_player_no)
        v_row_dict          = v_board_dict[str(p_row)]
        v_row_dict[p_col]=v_player_symbol
        v_board_dict[p_row]=v_row_dict
        v_game_dict['last player']= v_player_no
        v_game_dict['turn status']= 'Done'
        self.__json_obj.write_json('board',v_board_dict)
        self.__json_obj.write_json('game',v_game_dict)
        self.print_board()
