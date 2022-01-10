        if Game_State == Game.Board4by4:
            Game_State = pygame.display.set_mode((Board4X4_Width, Board4X4_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 4X4 Board')
            start_4by4_Board()

        if Game_State == Game.Board5by5:
            Game_State = pygame.display.set_mode((Board5X5_Width, Board5X5_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 5X5 Board')
            start_5by5_Board()

        if Game_State == Game.Board6X6:
            Game_State = pygame.display.set_mode((Board6X6_Width, Board6X6_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 6X6 Board')
            start_6X6_board()
        
        if Game_State == Game.Board7By7:
            Game_State = pygame.display.set_mode((Board7X7_Width, Board7X7_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 7X7 Board')
            start_7X7_Board()
        
        if Game_State == Game.Board10By10:
            Game_State = pygame.display.set_mode((Board10X10_Width, Board10X10_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 10X10 Board')
            start_10X10_Board()
    
        if Game_State == Game.AiBoard_3by3:
            Game_State = pygame.display.set_mode((Ai_Board3X3_Width, Ai_Board3X3_Height))
            Game_State = pygame.display.set_caption('Ai Tic-Tac-Toe 3X3 Board')
            start_Ai_3by3_Board()
        
        if Game_State == Game.AiBoard_4by4:
            Game_State = pygame.display.set_mode((Ai_Board4X4_Width, Ai_Board4X4_Height))
            Game_State = pygame.display.set_caption('Ai Tic-Tac-Toe 4X4 Board')
            start_ai_4by4_Board()
            
        if Game_State == Game.Ai_Board5by5:
            Game_State = pygame.display.set_mode((Ai_Board5X5_Width, Ai_Board5X5_Height))
            Game_State = pygame.display.set_caption('Ai Tic-Tac-Toe 5X5 Board')
            start_ai_5by5_Board()
