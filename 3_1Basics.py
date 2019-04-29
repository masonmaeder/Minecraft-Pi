from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()

x,y,z=mc.player.getPos()
mc.setBlocks(x+1, y, z, x+10, y+20, z+5, 46)
minecraft.op masoncreeps
