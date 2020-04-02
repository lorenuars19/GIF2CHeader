# GIF2CHeader
Simple Python script to make `_Bootscreen.h` from `anim.gif`
Useful for converting animation into custom [Marlin 2.x](https://marlinfw.org/) Bootscreen
For good results I recommend to use with 2:1 size ratio file (default size is 128x64 px)

You will need to install : 
Pillow by `pip install Pillow`for the script to work.
## Usage

Use any software to make a 2:1 size ratio gif of approx. 6 frames (you can do more if you have enough memory on your board)

 1. Put `anim.gif` in the same folder as the `gif2header.py`
 2. Run the script from terminal `<python executable> gif2header.py`
 3. Now should have a `_Bootscreen.h` in the folder

Enjoy .

## Settings
**At the top of the script you will find 5 variables**:
- *filename*	:	the output filename
- *gif_name*	:	the input file name
- *frame_ms*	:	tells to Marlin how many milliseconds per frame (I advise you to set this between 500 and 1500, over or under will be too short or too long)
- *out_width*	:	output resized width
- *out_heigh*	:	output resized height

### Note
I included a bit of ASCII art for the 'eye-candy' 