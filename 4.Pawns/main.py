max_number_of_pawns = 8
len_coordinate = 2

def count_number_of_defended_pawns(pawn_coordinates):
    number_of_pawns = len(pawn_coordinates)
    if number_of_pawns > max_number_of_pawns:
        return "Количество заданных координат превышает возможное число"

    number_of_protected_pawns = 0
    for pawn_coordinate in pawn_coordinates:
        len_pawn_coordinate = len(pawn_coordinate)
        if not (len_pawn_coordinate == len_coordinate) or \
                pawn_coordinate[0] < 'a' or pawn_coordinate[0] > 'h' or \
                pawn_coordinate[1] < '1' or pawn_coordinate[1] > '8' or \
                not pawn_coordinate[1].isdigit() or not pawn_coordinate[0].isalpha():
            return "Координаты заданны неправильно"

        pawn_coordinates_on_left = chr(ord(pawn_coordinate[0]) - 1)
        pawn_coordinates_on_right = chr(ord(pawn_coordinate[0]) + 1)
        pawn_coordinates_on_left += chr(ord(pawn_coordinate[1]) - 1)
        pawn_coordinates_on_right += chr(ord(pawn_coordinate[1]) - 1)
        if pawn_coordinates_on_left in pawn_coordinates or \
                pawn_coordinates_on_right in pawn_coordinates:
            number_of_protected_pawns += 1

    return number_of_protected_pawns

if __name__ == '__main__':
    assert count_number_of_defended_pawns({"q4", "d4", "q4", "c3", "e3", "g5", "d2"}) == "Координаты заданны неправильно"
    assert count_number_of_defended_pawns({"b41", "d4", "f41", "c3", "e3", "g5", "d2"}) == "Координаты заданны неправильно"
    assert count_number_of_defended_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2", "a1", "b2"}) == "Количество заданных координат превышает возможное число"
    assert count_number_of_defended_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert count_number_of_defended_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1