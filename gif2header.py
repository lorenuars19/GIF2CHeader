from PIL import Image, ImageSequence
import PIL
import os


filename = "_Bootscreen.h"
gif_name = 'anim.gif'
frame_ms = 800
out_width = 128
out_height = 64


def printHeader():
    print (
        "* **************************************************************************************************** *" + '\n'
        "*  BY :                                                                                                *" + '\n'  
        "*  _______  ______    _______  _______  ___   _  __   __  _     _  _______  __   __  _______  _______  *" + '\n'
        "* |       ||    _ |  |       ||   _   ||   | | ||  | |  || | _ | ||   _   ||  | |  ||       ||       | *" + '\n'
        "* |    ___||   | ||  |    ___||  |_|  ||   |_| ||  |_|  || || || ||  |_|  ||  |_|  ||    ___||  _____| *" + '\n'
        "* |   |___ |   |_||_ |   |___ |       ||      _||       ||       ||       ||       ||   |___ | |_____  *" + '\n'
        "* |    ___||    __  ||    ___||       ||     |_ |_     _||       ||       ||       ||    ___||_____  | *" + '\n'
        "* |   |    |   |  | ||   |___ |   _   ||    _  |  |   |  |   _   ||   _   | |     | |   |___  _____| | *" + '\n'
        "* |___|    |___|  |_||_______||__| |__||___| |_|  |___|  |__| |__||__| |__|  |___|  |_______||_______| *" + '\n'
        "*                                                                                                      *" + '\n'
        "* **************************************************************************************************** *" + '\n'
        )

    os.remove(filename)
    f = open(filename, "x")
    f.write(
        "/*" + '\n'
        "* **************************************************************************************************** *" + '\n'
        "* BY :                                                                                                 *" + '\n'
        "*  _______  ______    _______  _______  ___   _  __   __  _     _  _______  __   __  _______  _______  *" + '\n'
        "* |       ||    _ |  |       ||   _   ||   | | ||  | |  || | _ | ||   _   ||  | |  ||       ||       | *" + '\n'
        "* |    ___||   | ||  |    ___||  |_|  ||   |_| ||  |_|  || || || ||  |_|  ||  |_|  ||    ___||  _____| *" + '\n'
        "* |   |___ |   |_||_ |   |___ |       ||      _||       ||       ||       ||       ||   |___ | |_____  *" + '\n'
        "* |    ___||    __  ||    ___||       ||     |_ |_     _||       ||       ||       ||    ___||_____  | *" + '\n'
        "* |   |    |   |  | ||   |___ |   _   ||    _  |  |   |  |   _   ||   _   | |     | |   |___  _____| | *" + '\n'
        "* |___|    |___|  |_||_______||__| |__||___| |_|  |___|  |__| |__||__| |__|  |___|  |_______||_______| *" + '\n'
        "*                                                                                                      *" + '\n'
        "****************************************************************************************************** *" + '\n'
        "*/" + '\n' * 2
        )
    f.write (
     "/**" + "\n"
     "* Marlin 3D Printer Firmware" + "\n"
     "* Copyright (c) 2020 MarlinFirmware [https://github.com/MarlinFirmware/Marlin]" + "\n"
     "*" + "\n"
     "* Based on Sprinter and grbl." + "\n"
     "* Copyright (c) 2011 Camiel Gubbels / Erik van der Zalm" + "\n"
     "*" + "\n"
     "* This program is free software: you can redistribute it and/or modify" + "\n"
     "* it under the terms of the GNU General Public License as published by" + "\n"
     "* the Free Software Foundation, either version 3 of the License, or" + "\n"
     "* (at your option) any later version." + "\n"
     "*" + "\n"
     "* This program is distributed in the hope that it will be useful," + "\n"
     "* but WITHOUT ANY WARRANTY; without even the implied warranty of" + "\n"
     "* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the" + "\n"
     "* GNU General Public License for more details." + "\n"
     "*" + "\n"
     "* You should have received a copy of the GNU General Public License" + "\n"
     "* along with this program.  If not, see <http://www.gnu.org/licenses/>." + "\n"
     "*" + "\n"
     "*/" + "\n"
    "#pragma once" + "\n"
    + "\n"
    "/**" + "\n"
    " * Animated boot screen example" + "\n"
    " */" + "\n"
    "" + "\n"
    "#define CUSTOM_BOOTSCREEN_ANIMATED" + "\n"
    "#define CUSTOM_BOOTSCREEN_FRAME_TIME " + str(frame_ms) + "// (ms)" + "\n"
    "#define CUSTOM_BOOTSCREEN_BMPWIDTH   " + str(out_width) + ('\n' * 2))

    gif = Image.open('anim.gif')
    fr_num = 0

    for frame in ImageSequence.Iterator(gif):
        bw = frame.convert("1")
        final = bw.resize((out_width, out_height), PIL.Image.NEAREST)

        if fr_num == 0:
            f.write ("const unsigned char custom_start_bmp[] PROGMEM = {\n\t")
        else:
            f.write ("const unsigned char custom_start_bmp" + str(fr_num) + "[] PROGMEM = {\n\t")        

        i = 1
        data = list(final.getdata(0))

        for elem in data:
            elbin = bin(elem)
            f.write (format(elem, '#04X'))
            if i < len(data):
                f.write (',')
            if i % out_width == 0:
                f.write ("\n\t")
                i = 0
            i = i + 1
        f.write ("\n};\n")

        if fr_num == 0:
            print("> " + str(fr_num) + "\tframe written to \t'" + filename + "'\t\t input.size : " + str(frame.size) + "\tfinal.size : " + str(final.size))
        print("> " + str(fr_num + 1) + "\tframe(s) written to \t'" + filename + "'\t\t input.size : " + str(frame.size) + "\tfinal.size : " + str(final.size))
        fr_num = fr_num + 1

    f.write("const unsigned char * const custom_bootscreen_animation[] PROGMEM = {")
    fr_tot = fr_num
    fr_num = 0
    while fr_num <= fr_tot:
        f.write("custom_start_bmp" + str(fr_num))
        f.write(",\n\t")
        fr_num = fr_num + 1
    f.write("custom_start_bmp")
    f.write("\n};\n")
    print ("\n> " + str(fr_tot) + " name(s) of frame(s) in array written to " + filename)
    f.write(('\n' * 2) +
        "/*" + '\n'
        "* **************************************************************************************************** *" + '\n'
        "* BY :                                                                                                 *" + '\n'
        "*  _______  ______    _______  _______  ___   _  __   __  _     _  _______  __   __  _______  _______  *" + '\n'
        "* |       ||    _ |  |       ||   _   ||   | | ||  | |  || | _ | ||   _   ||  | |  ||       ||       | *" + '\n'
        "* |    ___||   | ||  |    ___||  |_|  ||   |_| ||  |_|  || || || ||  |_|  ||  |_|  ||    ___||  _____| *" + '\n'
        "* |   |___ |   |_||_ |   |___ |       ||      _||       ||       ||       ||       ||   |___ | |_____  *" + '\n'
        "* |    ___||    __  ||    ___||       ||     |_ |_     _||       ||       ||       ||    ___||_____  | *" + '\n'
        "* |   |    |   |  | ||   |___ |   _   ||    _  |  |   |  |   _   ||   _   | |     | |   |___  _____| | *" + '\n'
        "* |___|    |___|  |_||_______||__| |__||___| |_|  |___|  |__| |__||__| |__|  |___|  |_______||_______| *" + '\n'
        "*                                                                                                      *" + '\n'
        "****************************************************************************************************** *" + '\n'
        "*/"
        )

    print ("\n\n<<< closing " + str(gif))
    gif.close()
    print ("> SUCCESS <")
    print("<<< closing" + filename)
    f.close()
    print ("> SUCCESS <")

printHeader()

