from PIL import Image, ImageSequence
import PIL
import os
import sys


out_name        = "_Bootscreen.h"
gif_name        = "anim.gif"

frame_ms        = 800
auto_ms         = True
auto_ms_mult    = 10

total_loops     = 2

out_width       = 128
out_height      = 64
invert          = False

def printHeader():

    try:
        gif = Image.open(gif_name)
    except FileNotFoundError:
        print ("IO ERROR : File " + gif_name + " not found")
        sys.exit(1)

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

    if os.path.exists(out_name):
        os.remove(out_name)
    try:
        f = open(out_name, "x")
    except:
        print ("IOError : Can't create " + out_name)
        sys.exit(1)

    if auto_ms:
        frame_ms = gif.info['duration'] * auto_ms_mult

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
    "#define CUSTOM_BOOTSCREEN_FRAME_TIME " + str(frame_ms) + " // (ms)" + "\n"
    "#define CUSTOM_BOOTSCREEN_BMPWIDTH   " + str(out_width) + ('\n' * 2))

    frame_index = 0
    for frame in ImageSequence.Iterator(gif):
        bw = frame.convert("1")
        final = bw.resize((out_width, out_height), PIL.Image.BILINEAR)

        if frame_index == 0:
            f.write ("const unsigned char custom_start_bmp[] PROGMEM = {\n\t")
        else:
            f.write ("const unsigned char custom_start_bmp" + str(frame_index) + "[] PROGMEM = {\n\t")

        data = list(final.getdata(0))
        i = 1
        x = 0
        y = 0
        while y < out_height:
            x = 0
            while x < out_width:
                n = 0
                combine = 0
                f.write('B')
                while n <= 8 and x < out_width:
                    test = final.getpixel((x,y))
                    if test == invert:
                        f.write('0')
                    else:
                        f.write('1')
                    n = n + 1
                    x = x + 1
                # while n < 8:
                #     f.write ('0')
                #     n = n + 1
                if x < out_width:
                    f.write (',')
                x = x + 1
            y = y + 1
            if y < out_height:
                f.write ("\n\t")
            else:
                f.write ("\n")
        f.write ("};\n")
        print("> frame " + str(frame_index) + "\twritten to \t'" + out_name + "'\t\t input.size : " + str(frame.size) + "\tfinal.size : " + str(final.size))
        frame_index = frame_index + 1

    f.write("\nconst unsigned char * const custom_bootscreen_animation[] PROGMEM = {\n\t")
    fr_tot = frame_index
    frame_index = 0
    loop_num = 0

    while loop_num <= total_loops:
        frame_index = 0
        while frame_index <= fr_tot:
            f.write("custom_start_bmp" + str(frame_index))
            f.write(", ")
            frame_index = frame_index + 1
        f.write("custom_start_bmp,\n")

        if loop_num < total_loops:
            f.write('\t')
        loop_num = loop_num + 1
    f.write("};\n")

    print ("\n> (" + str(fr_tot) + " frames * " + str(total_loops) + " loops) = " + str(fr_tot * total_loops) + " total frame(s) in array written to '" + out_name + "'\n")
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

    print ("<<< closing " + str(gif) + " a.k.a. '" + gif_name + "'")
    gif.close()
    print ("> SUCCESS <")
    print("<<< closing '" + out_name + "'")
    f.close()
    print ("> SUCCESS <")

printHeader()
sys.exit(0)
