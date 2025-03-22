#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

import gi

gi.require_version('Gimp', '3.0')
from gi.repository import Gimp

gi.require_version('GimpUi', '3.0')
from gi.repository import GimpUi

from gi.repository import GObject
from gi.repository import GLib
from gi.repository import Gtk

import random
import traceback
import sys

plugin_proc = "plug-in-analogfeelings-py3-milk-filter"
plugin_binary = "milk-filter.py"
plugin_authors = "AnalogFeelings, LucaSinUnaS"

def probably(chance):
	return random.random() < chance

def milk_filter_run(procedure, run_mode, image, drawables, config, data):
	targetLayer = drawables[0]

	if not isinstance(targetLayer, Gimp.Layer):
		return procedure.new_return_values(Gimp.PDBStatusType.CALLING_ERROR, GLib.Error(f"Procedure '{plugin_proc}' works with layers only."))

	if run_mode == Gimp.RunMode.INTERACTIVE:
		GimpUi.init(plugin_binary)

		dialog = GimpUi.ProcedureDialog.new(procedure, config, "Milk Filter")
		dialog.fill([ "game", "punt" ])

		if not dialog.run():
			dialog.destroy()

			return procedure.new_return_values(Gimp.PDBStatusType.CANCEL, GLib.Error())

		dialog.destroy()

	game = config.get_property("game")
	punt = config.get_property("punt")

	# Get layer position and parent.
	parent = targetLayer.get_parent()
	position = image.get_item_position(targetLayer)

	# Push context and set up undo group.
	Gimp.context_push()
	image.undo_group_start()

	# Create a temporary layer to save the results.
	newLayer = Gimp.Layer.new(image, targetLayer.name + " temp", targetLayer.width, targetLayer.height,
							targetLayer.type, targetLayer.opacity, targetLayer.mode)
	
	image.insert_layer(newLayer, parent, position)
	newLayer.set_offsets(targetLayer.offsets[0], targetLayer.offsets[1])
	
	# Clear the temp layer.
	newLayer.edit_clear()
	newLayer.update(0, 0, targetLayer.width, targetLayer.height)
	
	# try:
	# 	tileWidth = Gimp.tile_width()
	# 	tileHeight = Gimp.tile_height()

	# 	tileNumberX = int(targetLayer.width / tileWidth)
	# 	if (targetLayer.width % tileWidth > 0):
	# 		tileNumberX += 1

	# 	tileNumberY = int(targetLayer.height / tileHeight)
	# 	if (targetLayer.height % tileHeight > 0):
	# 		tileNumberY += 1
		
	# 	for i in range(tileNumberX):
	# 		for j in range(tileNumberY):
	# 			srcTile = layer.get_tile(False, j, i)
	# 			dstTile = newLayer.get_tile(False, j, i)
				
	# 			for x in range(srcTile.ewidth):
	# 				for y in range(srcTile.eheight):
	# 					pixel = srcTile[x, y]
	# 					brightness = (ord(pixel[0]) + ord(pixel[1]) + ord(pixel[2])) / 3
	# 					puntilism = 0
	# 					result = ""
						
	# 					if(punt == 0):
	# 						puntilism = 100
	# 					else:
	# 						puntilism = 70
				
	# 					if(game == 0):
	# 						if brightness <= 25:
	# 							result += chr(0) + chr(0) + chr(0)
	# 						if brightness > 25 and brightness <= 70:
	# 							if probably(puntilism / 100):
	# 								result += chr(0) + chr(0) + chr(0)
	# 							else:
	# 								result += chr(102) + chr(0) + chr(31)
	# 						if brightness > 70 and brightness < 120:
	# 							if probably(puntilism / 100):
	# 								result += chr(102) + chr(0) + chr(31)
	# 							else:
	# 								result += chr(0) + chr(0) + chr(0)
	# 						if brightness >= 120 and brightness < 200:
	# 							result += chr(102) + chr(0) + chr(31)
	# 						if brightness >= 200 and brightness < 230:
	# 							if probably(puntilism / 100):
	# 								result += chr(137) + chr(0) + chr(146)
	# 							else:
	# 								result += chr(102) + chr(0) + chr(31)
	# 						if brightness >= 230:
	# 							result += chr(137) + chr(0) + chr(146)
	# 					else:
	# 						if brightness <= 25:
	# 							result += chr(0) + chr(0) + chr(0)
	# 						if brightness > 25 and brightness <= 70:
	# 							if probably(punt/100):
	# 								result += chr(0) + chr(0) + chr(0)
	# 							else:
	# 								result += chr(92) + chr(36) + chr(60)
	# 						if brightness > 70 and brightness < 90:
	# 							if probably(punt/100):
	# 								result += chr(92) + chr(36) + chr(60)
	# 							else:
	# 								result += chr(0) + chr(0) + chr(0)
	# 						if brightness >= 90 and brightness < 150:
	# 							result += chr(92) + chr(36) + chr(60)
	# 						if brightness >= 150 and brightness < 200:
	# 							if probably(punt/100):
	# 								result += chr(203) + chr(43) + chr(43)
	# 							else:
	# 								result += chr(92) + chr(36) + chr(60)
	# 						if brightness >= 200:
	# 							result += chr(203) + chr(43) + chr(43)
						
	# 					if(len(pixel) == 4):
	# 						result += pixel[3]
	# 					dstTile[x, y] = result
					
	# 	newLayer.flush()
	# 	newLayer.merge_shadow(True)
	# 	newLayer.update(0, 0, newLayer.width, newLayer.height)
	
	# 	image.remove_layer(layer)
		
	# 	newLayer.name = layerName
	# except Exception:
	#  	return procedure.new_return_values(Gimp.PDBStatusType.CALLING_ERROR, GLib.Error("Error processing milk filter: " + traceback.format_exc()))
	
	Gimp.displays_flush()

	image.undo_group_end()
	Gimp.context_pop()

	return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, None)

class MilkFilter(Gimp.PlugIn):
	def do_query_procedures(self):
		return [ plugin_proc ]
	
	def do_create_procedure(self, name):
		procedure = None

		if name == plugin_proc:
			procedure = Gimp.ImageProcedure.new(self, name, Gimp.PDBProcType.PLUGIN, milk_filter_run, None)

			procedure.set_image_types("RGB, RGB*");
			procedure.set_sensitivity_mask(Gimp.ProcedureSensitivityMask.DRAWABLE)

			procedure.set_menu_label("_Milk Filter")
			procedure.set_attribution(plugin_authors, plugin_authors, "2024")
			procedure.add_menu_path("<Image>/Filters/Artistic")
			procedure.set_documentation("Convert a layer to something you would find in the milk games.", None, None)

			milk_choice = Gimp.Choice.new()
			milk_choice.add("inside", 0, "Milk Inside", "")
			milk_choice.add("outside", 1, "Milk Outside", "")

			procedure.add_choice_argument("game", "Milk Game", "The game to use.", milk_choice, "inside", GObject.ParamFlags.READWRITE)
			procedure.add_boolean_argument("punt", "Puntilism", "Should the filter use puntilism.", False, GObject.ParamFlags.READWRITE)

		return procedure

Gimp.main(MilkFilter.__gtype__, sys.argv)
