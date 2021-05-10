import cmath
import numpy as np
from PIL import Image

def mandelbrot_simple(x,y,times):
  c = complex(x,y)
  z = complex(0,0)
  for i in range(1,times):
    z = (z*z)+c
    if abs(z) >2:
      return i
  if abs(z)<2:
    return 0

def mandelbrot_exp(x,y,times):
  c = cmath.exp(complex(x,y))
  z = complex(0,0)
  for i in range(1,times):
    z = (z*z)+c
    if abs(z)>2:
      return i
      break
  if abs(z)<=2:
    return 0

def mandelbrot_sin(x,y,times):
  c = cmath.sin(complex(x,y))
  z = complex(0,0)
  for i in range(1,times):
    z = (z*z)+c
    if abs(z)>2:
      return i
      break
  if abs(z)<=2:
    return 0

def fractal_maker(tamanho,nome,times,tipo):
  functions = {
    'simple': mandelbrot_simple,
    'exp':   mandelbrot_exp,
    'sin': mandelbrot_sin
  }
  x = np.linspace(-2,2,num = tamanho)
  y = np.linspace(-2,2,num=tamanho)
  z = np.dstack((x,y))[0]
  img2 = Image.new('RGB',(tamanho ,tamanho))
  for x in range(tamanho):
    for y in range(tamanho):
      #t = mandelbrot_simple(z[x][0],z[y][0],times)
      t = functions[tipo](z[x][0],z[y][0],times)
      compare = float(t)
      if compare<=10:
        img2.putpixel((x,y),(0, 0, 0))
      if compare<=25 and compare >10:
        img2.putpixel((x,y),(0, 255, 0))
      if compare >25 and compare<=50:
        img2.putpixel((x,y),(0,0,255))
      if compare >50 and compare <=100:
        img2.putpixel((x,y),(255, 0, 0))
      if compare == 0:
        img2.putpixel((x,y),(255, 255, 255))

  img2.save((nome+".png"))

fractal_maker(1700,"fractal",100,'sin')






