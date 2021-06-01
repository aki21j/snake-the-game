UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIAGONALLY_UP_LEFT = (1,1)
DIAGONALLY_DOWN_RIGHT = (-1,-1)
class Snake:

  def __init__(self, init_body: tuple, init_direction: tuple) -> None:
    self.body = init_body
    self.direction = init_direction

  def take_step(self, position) -> None:
    self.body.append(position)
    self.body.pop(0)

  def set_direction(self, direction) -> None:
    self.direction = direction

  def head(self):
    return self.body[-1]


class Apple:
  def __init__(self) -> None:
      pass



class Game:
  def __init__(self, width, height) -> None:
      self.width = width
      self.height = height
      self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], UP)

  def board_matrix(self):
    return [[" " for i in range(self.width)] for i in range(self.height)]

  def render(self):
    snake_body = self.snake.body
    snake_head = self.snake.head()
    print(snake_head)

    matrix = self.board_matrix()
    x_borders = "+" + "-" * (self.width + 1) + "+"
    print(x_borders)
    for row in range(0, self.height):
      line = "|"
      for col in range(0, self.width):
        if (row, col) == snake_head:
          line += "" + str(1)
        elif (row, col) in snake_body:
          line += "" + str(0)
        else:
          line += "" + str(matrix[row][col])
      line += " |"
      print(line)

    print(x_borders)

  
x = Game(5, 4)

x.render()