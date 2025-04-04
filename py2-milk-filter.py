#!/usr/bin/env python

# MIT License
#
# Copyright (c) 2024 LucaSinUnaS, Analog Feelings
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random
import traceback
from gimpfu import *

def probably(chance):
	return random.random() < chance

def apply_milk_filter(image, layer, game, punt):
	# Set up undo group.
	pdb.gimp_image_undo_group_start(image)
	
	# Get the layer position.
	position = 0
	for i in range(len(image.layers)):
		if(image.layers[i] == layer):
			position = i
			
	# Create a temporary layer to save the results.
	newLayer = gimp.Layer(image, layer.name + " temp", layer.width, layer.height, layer.type, layer.opacity, layer.mode)
	image.add_layer(newLayer, position)
	pdb.gimp_layer_set_offsets(newLayer, layer.offsets[0], layer.offsets[1])
	layerName = layer.name
	
	# Clear the temp layer.
	pdb.gimp_edit_clear(newLayer)
	newLayer.flush()
	
	try:
		tileNumberX = int(layer.width / gimp.tile_width())
		if (layer.width % gimp.tile_width() > 0):
			tileNumberX += 1
		tileNumberY = int(layer.height / gimp.tile_height())
		if (layer.height % gimp.tile_height() > 0):
			tileNumberY += 1
		
		for i in range(tileNumberX):
			for j in range(tileNumberY):
				srcTile = layer.get_tile(False, j, i)
				dstTile = newLayer.get_tile(False, j, i)
				
				for x in range(srcTile.ewidth):
					for y in range(srcTile.eheight):
						pixel = srcTile[x, y]
						brightness = (ord(pixel[0]) + ord(pixel[1]) + ord(pixel[2])) / 3
						puntilism = 0
						result = ""
						
						if(punt == 0):
							puntilism = 100
						else:
							puntilism = 70
				
						if(game == 0):
							if brightness <= 25:
								result += chr(0) + chr(0) + chr(0)
							if brightness > 25 and brightness <= 70:
								if probably(puntilism / 100):
									result += chr(0) + chr(0) + chr(0)
								else:
									result += chr(102) + chr(0) + chr(31)
							if brightness > 70 and brightness < 120:
								if probably(puntilism / 100):
									result += chr(102) + chr(0) + chr(31)
								else:
									result += chr(0) + chr(0) + chr(0)
							if brightness >= 120 and brightness < 200:
								result += chr(102) + chr(0) + chr(31)
							if brightness >= 200 and brightness < 230:
								if probably(puntilism / 100):
									result += chr(137) + chr(0) + chr(146)
								else:
									result += chr(102) + chr(0) + chr(31)
							if brightness >= 230:
								result += chr(137) + chr(0) + chr(146)
						else:
							if brightness <= 25:
								result += chr(0) + chr(0) + chr(0)
							if brightness > 25 and brightness <= 70:
								if probably(punt/100):
									result += chr(0) + chr(0) + chr(0)
								else:
									result += chr(92) + chr(36) + chr(60)
							if brightness > 70 and brightness < 90:
								if probably(punt/100):
									result += chr(92) + chr(36) + chr(60)
								else:
									result += chr(0) + chr(0) + chr(0)
							if brightness >= 90 and brightness < 150:
								result += chr(92) + chr(36) + chr(60)
							if brightness >= 150 and brightness < 200:
								if probably(punt/100):
									result += chr(203) + chr(43) + chr(43)
								else:
									result += chr(92) + chr(36) + chr(60)
							if brightness >= 200:
								result += chr(203) + chr(43) + chr(43)
						
						if(len(pixel) == 4):
							result += pixel[3]
						dstTile[x, y] = result
					
		newLayer.flush()
		newLayer.merge_shadow(True)
		newLayer.update(0, 0, newLayer.width, newLayer.height)
	
		image.remove_layer(layer)
		
		newLayer.name = layerName
	except Exception:
		gimp.message("Error processing milk filter: " + traceback.format_exc())
		
	pdb.gimp_image_undo_group_end(image)
	
name = "analog-milk-filter"
description = "Convert an image to something you would find in the milk inside/outside games!"
authors = "LucaSinUnaS, Analog Feelings"
license = "MIT License"
year = "2024"
label = "Milk Filter"

register(
	name,
	description,
	description,
	authors,
	license,
	year,
	label,
	"RGB, RGB*",
	[
		(PF_IMAGE, "image", "Input image", None),
		(PF_DRAWABLE, "layer", "Input layer", None),
		(PF_OPTION, "game", "Milk Game", 0, ["Milk Inside", "Milk Outside"]),
		(PF_OPTION, "punt", "Puntilism", 0, ["No", "Yes"])
	],
	[],
	apply_milk_filter,
	menu = "<Image>/Filters/Artistic/"
)

main()
