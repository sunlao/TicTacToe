 board.py
#!/usr/bin/python

import json

class MNG_JSON(object):

    def write_json(self,p_type,p_dict):

        if p_type == 'board':
            v_file_nm = self.board_file_nm
        elif    p_type == 'game':
            v_file_nm = self.game_file_nm
            v_json_str  = json.dumps(p_dict)
            file_obj = open(v_file_nm,'w')
            file_obj.write(json.dumps(p_dict))
            file_obj.close

    def get_json(self,p_type):

        if  p_type == 'board':
            v_file_nm = self.board_file_nm
        elif    p_type == 'game':
            v_file_nm = self.game_file_nm
            file_obj = open(v_file_nm,'r')
            v_json_str = file_obj.read()
            file_obj.close
            v_board = json.loads(v_json_str)

        return v_board

