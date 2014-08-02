#!/usr/bin/python

class MNG_Game_Status(object):

    def __init__(self):
        from Config     import Config
        from MNG_JSON   import MNG_JSON

        config_obj              = Config()
        self.__json_obj     = MNG_JSON()

        self.__playr1_symbol    = config_obj.get_value('playr1_symbol')
        self.__playr2_symbol    = config_obj.get_value('playr2_symbol')
        self.__empty_spc        = config_obj.get_value('empty_spc')
        self.__board_height     = config_obj.get_value('board_height')
        self.__board_width      = config_obj.get_value('board_width')

    def chk_row_winner(self,p_board_dict):
        v_row_num   = 1
        v_empty_spc_cnt = 0
        v_plyr1_win_flg = -1
        v_plyr2_win_flg = -1
        v_tie_flg   = -1
        v_row_win_dict  = {}

        while v_row_num <= self.__board_height:
            v_dict_row = p_board_dict[str(v_row_num)]
            v_col_num       = 1
            v_playr1_cnt    = 0
            v_playr2_cnt    = 0

            while v_col_num <= self.__board_width:
                v_val = v_dict_row[str(v_col_num)]
                if  v_val == self.__playr1_symbol:
                    v_playr1_cnt = v_playr1_cnt +1
                elif v_val == self.__playr2_symbol:
                    v_playr2_cnt = v_playr2_cnt +1
                elif v_val == self.__empty_spc:
                    v_empty_spc_cnt = v_empty_spc_cnt+1

                if  v_playr1_cnt == self.__board_width:
                    v_plyr1_win_flg = 0
                    v_col_num = self.__board_width +1
                    v_row_num = self.__board_height +1
                elif    v_playr2_cnt == self.__board_width:
                    v_plyr2_win_flg = 0
                    v_col_num = self.__board_width +1
                    v_row_num = self.__board_height +1
                else:
                    v_col_num = v_col_num +1

            v_row_num = v_row_num +1

        if v_empty_spc_cnt == 0 and v_plyr1_win_flg == -1 and v_plyr2_win_flg == -1:
            v_tie_flg = 0

        v_row_win_dict['plyr1_win_flg']=v_plyr1_win_flg
        v_row_win_dict['plyr2_win_flg']=v_plyr2_win_flg
        v_row_win_dict['tie_flg']=v_tie_flg

        return v_row_win_dict

    def chk_diag_lft_winner(self,p_board_dict):
        v_row_num           = 1
        v_plyr1_win_flg     = -1
        v_plyr2_win_flg     = -1
        v_diag_lft_win_dict     = {}
        v_playr1_cnt        = 0
        v_playr2_cnt        = 0

        while v_row_num <= self.__board_height:
            v_dict_row = p_board_dict[str(v_row_num)]

            v_val = v_dict_row[str(v_row_num)]

            if  v_val == self.__playr1_symbol:
                v_playr1_cnt = v_playr1_cnt +1
            elif    v_val == self.__playr2_symbol:
                v_playr2_cnt = v_playr2_cnt +1

            v_row_num = v_row_num +1

        if  v_playr1_cnt == self.__board_height:
            v_plyr1_win_flg = 0
        elif    v_playr2_cnt == self.__board_height:
            v_plyr2_win_flg = 0

        v_diag_lft_win_dict['plyr1_win_flg']=v_plyr1_win_flg
        v_diag_lft_win_dict['plyr2_win_flg']=v_plyr2_win_flg

        return v_diag_lft_win_dict

    def chk_diag_rght_winner(self,p_board_dict):
        v_row_num               = 1
        v_plyr1_win_flg         = -1
        v_plyr2_win_flg         = -1
        v_diag_rght_win_dict    = {}
        v_playr1_cnt            = 0
        v_playr2_cnt            = 0

        while v_row_num <= self.__board_height:
            v_dict_row = p_board_dict[str(v_row_num)]

            v_col_key = (self.__board_width - v_row_num)+1
            v_val = v_dict_row[str(v_col_key)]

            if      v_val == self.__playr1_symbol:
                v_playr1_cnt = v_playr1_cnt +1
            elif    v_val == self.__playr2_symbol:
                v_playr2_cnt = v_playr2_cnt +1

            v_row_num = v_row_num +1

        if      v_playr1_cnt == self.__board_height:
            v_plyr1_win_flg = 0
        elif    v_playr2_cnt == self.__board_height:
            v_plyr2_win_flg = 0

        v_diag_rght_win_dict['plyr1_win_flg']=v_plyr1_win_flg
        v_diag_rght_win_dict['plyr2_win_flg']=v_plyr2_win_flg

        return v_diag_rght_win_dict

    def chk_col_winner(self,p_board_dict):
        v_col_num           = 1
        v_win_flg           = -1
        v_plyr1_win_flg     = -1
        v_plyr2_win_flg     = -1
        v_col_winner_dict   = {}
        while v_col_num <= self.__board_width and v_win_flg == -1:
            v_row_num       = 1
            v_playr1_cnt    = 0
            v_playr2_cnt    = 0
            while v_row_num <= self.__board_height:
                v_dict_row = p_board_dict[str(v_row_num)]
                v_val = v_dict_row[str(v_col_num)]
                if      v_val == self.__playr1_symbol:
                    v_playr1_cnt = v_playr1_cnt +1
                elif    v_val == self.__playr2_symbol:
                    v_playr2_cnt = v_playr2_cnt +1
                v_row_num = v_row_num +1
            if      v_playr1_cnt == self.__board_height:
                v_plyr1_win_flg = 0
                v_win_flg       = 0
            elif    v_playr2_cnt == self.__board_height:
                v_plyr2_win_flg = 0
                v_win_flg       = 0

            v_col_num       = v_col_num +1

        v_col_winner_dict['plyr1_win_flg']=v_plyr1_win_flg
        v_col_winner_dict['plyr2_win_flg']=v_plyr2_win_flg

        return v_col_winner_dict

    def get_game_status_dict(self):
        game_status_dict = {}
        v_game_over_flg = -1
        v_game_over_msg = "Keep Playing"
        v_board_dict    = self.__json_obj.get_json('board')
        v_row_win_dict  = self.chk_row_winner(v_board_dict)
        if  v_row_win_dict['plyr1_win_flg'] == 0:
            v_game_over_flg = 0
            v_game_over_msg = "Player 1 Wins!"
        elif    v_row_win_dict['plyr2_win_flg'] == 0:
            v_game_over_flg = 0
            v_game_over_msg = "Player 2 Wins!"
        else:
            v_diag_lft_win_dict = self.chk_diag_lft_winner(v_board_dict)
            if      v_diag_lft_win_dict['plyr1_win_flg'] == 0:
                v_game_over_flg = 0
                v_game_over_msg = "Player 1 Wins!"
            elif    v_diag_lft_win_dict['plyr2_win_flg'] == 0:
                v_game_over_flg = 0
                v_game_over_msg = "Player 2 Wins!"
            else:
                v_diag_rght_win_dict = self.chk_diag_rght_winner(v_board_dict)
                if  v_diag_rght_win_dict['plyr1_win_flg'] == 0:
                    v_game_over_flg = 0
                    v_game_over_msg = "Player 1 Wins!"
                elif    v_diag_rght_win_dict['plyr2_win_flg'] == 0:
                    v_game_over_flg = 0
                    v_game_over_msg = "Player 2 Wins!"
                else:

                    v_col_winner_dict = self.chk_col_winner(v_board_dict)

                    if  v_col_winner_dict['plyr1_win_flg'] == 0:
                        v_game_over_flg = 0
                        v_game_over_msg = "Player 1 Wins!"
                    elif    v_col_winner_dict['plyr2_win_flg'] == 0:
                        v_game_over_flg = 0
                        v_game_over_msg = "Player 2 Wins!"
                    elif    v_row_win_dict['tie_flg'] == 0:
                        v_game_over_flg = 0
                        v_game_over_msg = "The game is a draw"
        game_status_dict['game_over_flg']=v_game_over_flg
        game_status_dict['game_over_msg']=v_game_over_msg

        return game_status_dict
