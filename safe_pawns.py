def safe_pawns(pawns):
    total = 0
    protected = []
    for pawn1 in pawns:
        for pawn2 in pawns:
            columDif = ord(pawn2[0]) == ord(pawn1[0]) - 1 or ord(pawn2[0]) == ord(pawn1[0]) + 1
            if(columDif) and int(pawn1[1]) == (int(pawn2[1]) + 1):
                if pawn1 not in protected:
                    total += 1
                    protected.append(pawn1)
                print(pawn1, pawn2)
    return total
