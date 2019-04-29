count = 1
while count <= 5:
   print
   count = count + 1

from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

grass = 2
flower = 38
while True:
    x, y, z = mc.player.getPos()
    this_block=mc.getBlock(x, y-1, z)

    if this_block == grass:
        mc.setBlock(x, y, z, flower)
    elif this_block == 1:
        mc.setBlock(x, y-1, z, 95.8)
