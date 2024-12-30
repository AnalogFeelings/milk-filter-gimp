from random import random
from gimpfu import *
from array import array

def apply_milk_filter(image, layer, game):
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
	layerName = layer.name
	
	# Clear the temp layer.
	pdb.gimp_edit_clear(newLayer)
	newLayer.flush()
	
description = "Convert an image to something you would find in the milk inside/outside games!"

register(
	"analog-milk-filter",
	description,
	description,
	"LucaSinUnaS, Analog Feelings",
	"MIT License",
	"2024",
	"Milk Filter",
	"RGB, RGB*",
	[
		(PF_IMAGE, "image", "Input image", None),
		(PF_DRAWABLE, "layer", "Input layer", None),
		(PF_OPTION, "game", "Milk Game", 0, ["Milk Inside", "Milk Outside"])
	],
	[],
	apply_milk_filter,
	menu = "<Image>/Filters/Artistic/"
)

main()