if __name__ == "__main__":
    pass


class Point1D:
    """Точка в одномерном пространстве"""
    def __init__(self, name: str, x_coord: float):
        self.name = name
        self.x_coord = x_coord

    def __str__(self):
        return f'Точка "{self.name}" с координатой X={self.x_coord}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.x_coord!r})'

    def move(self, x_move: float):
        """Метод перемещает точку по координате X"""
        self.x_coord += x_move

    def move_to_zero(self):
        """Метод возвращает точку в начало коориданат"""
        coords = vars(self)
        for x in coords:
            if x != "name":
                coords[x] = 0


class Point2D(Point1D):
    """Точка в двумерном пространстве"""
    def __init__(self, name: str, x_coord: float, y_coord: float):
        super().__init__(name, x_coord)
        self.y_coord = y_coord

    def __str__(self):
        return f'Точка "{self.name}" с координатами X={self.x_coord}, Y={self.y_coord}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.x_coord!r}, {self.y_coord!r})'

    def move(self, x_move: float, y_move: float):
        """Метод наследует перемещение точки по координате X и перегружается перемещением точки по координате Y"""
        super().move(x_move)
        self.y_coord += y_move

    def move_to_zero(self):
        """Метод возвращает точку в начало коориданат"""
        super().move_to_zero()


class Point3D(Point2D):
    """Точка в трехмерном пространстве"""
    def __init__(self, name: str, x_coord: float, y_coord: float, z_coord: float):
        super().__init__(name, x_coord, y_coord)
        self.z_coord = z_coord

    def __str__(self):
        return f'Точка "{self.name}" с координатами X={self.x_coord}, Y={self.y_coord}, Z={self.z_coord}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.x_coord!r}, {self.y_coord!r}, {self.z_coord})'

    def move(self, x_move: float, y_move: float, z_move: float):
        """Метод наследует перемещение точки по координатам X и Y и перегружается перемещением точки по координате Z"""
        super().move(x_move, y_move)
        self.z_coord += z_move

    def move_to_zero(self):
        """Метод возвращает точку в начало коориданат"""
        super().move_to_zero()
  # пустая строка