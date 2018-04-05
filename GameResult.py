def checkio(game_result):
    for i in range(3):
        if game_result[i][0] == game_result[i][1] and game_result[i][0] == game_result[i][2]:
            return game_result[i][0]
        elif game_result[0][i] == game_result[1][i] and game_result[0][i] == game_result[2][i]:
            return game_result[0][i]
        elif game_result[0][0] == game_result[1][1] and game_result[0][0] == game_result[2][2]:
            return game_result[0][0]
        elif game_result[2][0] == game_result[1][1] and game_result[2][0] == game_result[0][2]:
            return game_result[2][0]
    return "D"
