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
**At the top of the script you will find 3 groups of variables**:
- out_name      = *string*	:	the output file name
- gif_name      = *string*	:	the input file name

- frame_ms      = *number*	:	tells to Marlin frame duration in ms
- auto_ms       = *boolean* : set to true to let the script determine from the 1st frame's duration
- auto_ms_mult  = *number*	:	set multiplier for auto_ms 	
- total_loops   = *number*	:	set number of loops

- out_width     = *number*	:	output resized width
- out_heigh	    = *number*	:	output resized height
- invert        = *boolean* : set to True to invert the colors

### Note
I included a bit of ASCII art for the 'eye-candy'
