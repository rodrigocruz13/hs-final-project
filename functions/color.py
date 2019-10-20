#!/usr/bin/python3
"""
x = 0
for i in range(24):
  colors = ""
  for j in range(5):
    code = str(x+j)
    colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
  print(colors)
  x=x+5

from sty import fg, bg, ef, rs

foo = fg.red + 'This is red text!' + fg.rs
bar = bg.blue + 'This has a blue background!' + bg.rs
baz = ef.italic + 'This is italic text' + rs.italic
qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs

# Add custom colors:

from sty import Style, RgbFg

fg.orange = Style(RgbFg(255, 150, 50))
buf = fg.orange + 'Yay, Im orange.' + fg.rs
print(foo, bar, baz, qux, qui, buf, sep='\n')
"""

print("\033[0;37;40m Normal text\n")
print("\033[2;37;40m Underlined text\033[0;37;40m \n")
print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
print("\033[5;37;40m Negative Colour\033[0;37;40m\n")
 
print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")
