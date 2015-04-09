import games

game = games.TicTacToe()
state = game.initial

#print games.play_game(game, games.random_player, games.alphabeta_player)

player = 'X'

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        coor_str = raw_input("Movimiento x,y: ")
        coor = str(coor_str).strip().split(",")
        x, y = int(coor[0]), int(coor[1])

        state = game.make_move((x, y), state)
        player = 'X'
    else:
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        move = games.alphabeta_full_search(state, game)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        print "Numero de veces que se llega a un nodo terminal: "
        print game.getTerminalCounter()
        break
