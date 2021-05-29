class Snake:

  def __init__(self) -> None:
      pass


class Apple:
  def __init__(self) -> None:
      pass



class Game:
  def __init__(self, width, height) -> None:
      self.width = width
      self.height = height

  def board_matrix(self):
    return [[0 for i in range(5)] for i in range(5)]

  def render(self):
    matrix = self.board_matrix()
    x_borders = ["-" for i in range(12)]
    lines = []
    lines.append("".join(x_borders))
    for row in matrix:
      line = "|"
      for col in row:
        line += " " + str(col)
      line += "|"
      lines.append(line)

    lines.append("".join(x_borders))

    print("\n".join(lines))



  
x = Game(5, 4)

x.render()