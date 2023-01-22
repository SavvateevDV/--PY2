class Cup:
    def __init__(self, material: str, volume: float, volume_of_liquid: float):
        self.material = material
        self.volume = volume
        self.volume_of_liquid = volume_of_liquid
        self.remaining_volume_of_the_cup = volume

    def pour_the_liquid(self, refilled_volume_liquid: float):
        ...
        """ 
        Метод увеличивает объем жидкости в кружке
        :param refilled_volume_liquid: доливаемый объем жидкости
        :param new_volume_of_liquid: новый объем жидкости в кружке
        """
    def pour_out_the_liquid(self, poured_volume_liquid: float):
        ...
        """ 
        Метод уменьшает объем жидкости в кружке
        :param poured_volume_liquid: выливаемый объем жидкости
        :param new_volume_of_liquid: новый объем жидкости в кружке
        """
    def remaining_volume_of_the_cup(self, volume_of_liquid, volume):
        if volume_of_liquid > volume:
            raise ValueError("Объем жидкости в кружке не должен привышать объем кружки")

class Door:
    def __init__(self, material: str, height: float, width: float, thickness: float, is_open: bool):
        self.material = material
        self.height = height
        self.width = width
        self.thickness = thickness
        self.is_open = is_open

    def open_door(self, is_open):
        ...
        """ 
        Метод открывает дверь
        :param is_open: открытость двери
        """
        if is_open is True:
            raise ValueError("Дверь уже открыта")

    def close_door(self, is_open):
        ...
        """ 
        Метод закрывает дверь
        :param is_open: открытость двери
        """
        if is_open is False:
            raise ValueError("Дверь уже закрыта")

class Point:
    def __init__(self, X_coordinate: float, Y_coordinate: float, Z_coordinate: float):
        self.X_coordinate = X_coordinate
        self.Y_coordinate = Y_coordinate
        self.Z_coordinate = Z_coordinate

    def moving(self, X_moving, Y_moving, Z_moving):
        ...
        """ 
        Метод перемещает точку в пространстве
        :param X_moving: перемещение по X
        :param Y_moving: перемещение по Y
        :param Z_moving: перемещение по Z
        :param X_coordinate_final: конечная координата X
        :param Y_coordinate_final: конечная координата Y
        :param Z_coordinate_final: конечная координата Z
        """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
# пустая строка