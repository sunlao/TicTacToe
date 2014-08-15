#!/usr/bin/python

class MNG_Game_Play(object):

    def __init__(self):
        from Utility.Config     import Config
        from Utility.MNG_JSON   import MNG_JSON
        from MNG_Board          import MNG_Board
        from MNG_Game_Status    import MNG_Game_Status
        from MNG_Player         import MNG_Player

        config_obj              = Config()
        self.__json_obj         = MNG_JSON()
        self.__board_obj        = MNG_Board()
        self.__game_status_obj  = MNG_Game_Status()
        self.__player_obj       = MNG_Player()

        self.__board_width      = config_obj.get_value('board_width')
        self.__board_height     = config_obj.get_value('board_height')
        self.__empty_spc        = config_obj.get_value('empty_spc')
        self.__playr1_symbol    = config_obj.get_value('playr1_symbol')
        self.__playr2_symbol    = config_obj.get_value('playr2_symbol')

    def exe_game(self):
        try:
            v_game_dict = self.__json_obj.get_dict('game')
        except IOError:
            self.start_new_game()
        else:
            if  v_game_dict['game status']=='Over':
                self.start_new_game()
            else:
                v_input_str = "A game exists.  Would you like to continue? (Y/N) "
                v_continue_game = raw_input(v_input_str)
                v_continue_game = v_continue_game.upper()

                if v_continue_game.upper()== 'N':
                    print "Lets start a new game!"
                    self.start_new_game()
                elif v_continue_game.upper() == 'Y':
                    print "Last Game Loaded"
                    self.print_board()
                    v_last_player   = v_game_dict['last player']
                    v_turn_status   = v_game_dict['turn status']
                    v_player_dict   = self.get_player_dict(v_last_player,v_turn_status)
                    v_player_no     = v_player_dict['player_no']
                    v_player_symbol = self.get_player_symbol(v_player_no)
                    v_input_str     = "Player %s please select a row and column to place your %s (i.e. 2,2) " %(v_player_no,v_player_symbol)
                    self.mng_input_move(v_input_str)
                else:
                    print "Please enter a 'Y' to load previous game or a'N' to start a new game"
                    self.exe_game()

    def start_new_game(self):
        self.__board_obj.get_new_board()
        v_input_str   = "Player 1 please select a row and column to place your %s (i.e. 2,2) " %(self.__playr1_symbol)
        self.mng_input_move(v_input_str)

    def chk_input_valid(self,p_row,p_col):
        if      p_row >= 1 and p_row <= self.__board_width and p_col >= 1 and p_col <= self.__board_height:
            if      self.__board_obj.get_board_value(p_row,p_col) == self.__empty_spc:
                v_val = 0
            else:
                v_val = -3
        elif    p_row >= 1 and p_row > self.__board_height:
            v_val = -1
        elif    p_col >= 1 and p_col > self.__board_width:
            v_val = -2

        return v_val

    def mng_input_move(self,p_input_str):
        try:
            v_row_col_str   = input(p_input_str)
            v_chk_val = self.chk_input_valid(v_row_col_str[0],v_row_col_str[1])
            if  v_chk_val == 0:
                self.__board_obj.post_board(v_row_col_str[0],v_row_col_str[1])
            else:
                v_game_dict     = self.__json_obj.get_dict('game')
                v_last_player   = v_game_dict['last player']
                v_turn_status   = v_game_dict['turn status']
                v_player_dict   = self.__player_obj.get_player_dict(v_last_player,v_turn_status)
                v_player_no     = v_player_dict['player_no']
                if v_chk_val == -1:
                    v_input_str = "Player %s please use a Row value between 1 and %s " %(v_player_no,self.__board_height)
                elif v_chk_val == -2:
                    v_input_str = "Player %s please use a Column value between 1 and %s " %(v_player_no,self.__board_width)
                elif v_chk_val == -3:
                    v_input_str = "Player %s please select an unused space " %(v_player_no)
                self.mng_input_move(v_input_str)
        except:
            print "Please try again with two valid numbers seperated by a comma"
            v_game_dict     = self.__json_obj.get_dict('game')
            v_last_player   = v_game_dict['last player']
            v_turn_status   = v_game_dict['turn status']
            v_player_dict   = self.__player_obj.get_player_dict(v_last_player,v_turn_status)
            v_player_no     = v_player_dict['player_no']
            v_player_symbol = self.__player_obj.get_player_symbol(v_player_no)
            v_input_str = "Player %s please select a row and column to place your %s (i.e. 2,2) " %(v_player_no,v_player_symbol)
            self.mng_input_move(v_input_str)
        self.chk_game_over()

    def chk_game_over(self):
        v_game_over_dict = self.__game_status_obj.get_game_status_dict()
        if  v_game_over_dict['game_over_flg'] == -1:
            v_game_dict             = self.__json_obj.get_dict('game')
            v_last_player           = v_game_dict['last player']
            v_turn_status           = v_game_dict['turn status']
            v_player_dict           = self.__player_obj.get_player_dict(v_last_player,v_turn_status)
            v_player_no        = v_player_dict['player_no']
            v_player_symbol    = self.__player_obj.get_player_symbol(v_player_no)
            v_input_str             = "Player %s please select a row and column to place your %s (i.e. 2,2) " %(v_player_no,v_player_symbol)
            self.mng_input_move(v_input_str)
        else:
            v_game_dict             = self.__json_obj.get_dict('game')
            v_game_dict['game status']='Over'
            self.__json_obj.write_json('game',v_game_dict)
            print v_game_over_dict['game_over_msg']
