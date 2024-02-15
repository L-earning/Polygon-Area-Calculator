import math

class Rectangle:

  def __init__(self, width, height):
    self.set_width(width)
    self.set_height(height)

  def __str__(self):
    return f'Rectangle(width={self._width}, height={self._height})'
     
  
  def set_width(self, width):
    self._width = width

  def set_height(self, height):
    self._height = height

  def get_area(self):
    return (self._width * self._height)

  def get_perimeter(self):
    return (2 * self._width + 2 * self._height)

  def get_diagonal(self):
    return ((self._width ** 2 + self._height ** 2) ** .5)

  def get_picture(self):
    result = ""
    height = self._height
    width = self._width
    if height > 50 or width > 50:
      return 'Too big for picture.'
    while height > 0:
      result += '*'*width
      result+= '\n'
      height -= 1
    return result

  #how many times can the other shape fit inside the original shape without rotations
  def get_amount_inside(self, other):
    original_height = self._height
    original_width = self._width
    other_height = other._height
    other_width = other._width

    #if the shape to have other shapes inside it is too small for the shape to 
    #be fitted, return 0
    if original_height < other_height or original_width < other_width:
      return 0
    else:
      width_fit = math.floor(original_width/other_width)
      height_fit = math.floor(original_height/other_height)
      return width_fit*height_fit
      

class Square(Rectangle):

  def __init__(self, side_length):
    self.set_side(side_length)
    self.set_height(side_length)
    self.set_width(side_length)

  def __str__(self):
    return f'Square(side={self._side_length})'    

  def set_side(self, side_length):
    self._side_length = side_length
    self._height = side_length
    self._width = side_length

  def set_width(self, side_length):
    self._height = side_length
    self._width = side_length
    self._side_length = side_length

  def set_height(self, side_length):
    self._height = side_length
    self._width = side_length
    self._side_length = side_length
