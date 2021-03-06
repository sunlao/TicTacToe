TicTacToe
==========

TicTacToe is traditionally a game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal row wins the game.

### Execute Game
* Exe_Tic_Tac_Toe.py   - Starts a new game or recovers last unfinished game

### Game Functions
* MNG_Game_Play.py 
  * exe_game             - Executes game
  * start_new_game       - Starts new game
  * chk_input_valid      - Check input values are valid
  * mng_input_move       - Mangage input of moves from players 
  * chk_game_over        - Checks if game is over or should continue
* MNG_Board.py
  * get_new_board        - Get new board from a JSON file
  * print_board          - Print a board to screen from a JSON file
  * get_board_value      - Get a value for a board by row and column from a JSON file
  * post_board           - Post an update to board into a JSON file
* MNG_Game_Status.py
  * chk_row_winner       - Check for a winner by row
  * chk_diag_lft_winner  - Check for a left diagonal winner
  * chk_diag_rght_winner - Check for a right diagonal winner
  * chk_col_winner       - Check for a winner by column
  * get_game_status_dict - Get a Game Status dictionary
* MNG_Player.py
  * get_player_symbol    - Get a player symbol by player number
  * get_player_dict      - Get a Player dictionary

### Utility
* MNG_JSON.py
  * write_json           - Create a JSON file from a dictionary by file name
  * get_dict             - Get a dictionary from a JSON file by file name
* Config.py
  * get_def_dict         - get default dictionary for app if JSON does not exist 
  * get_dict             - get a configuration dictionary for app from JSON file or default dict
  * post_config          - update config json file with new Key Value Pair
  * get_value            - get a value by a key from configuration dictionary
