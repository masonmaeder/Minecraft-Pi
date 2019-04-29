from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

hitCount=0
while hitCount<=20:
   hit= mc.player.getPos()
   print("Hits:"+ str(hitCount))
   #loop to change the block
   for hit in mc.events.pollBlockHits():
      mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, 46)
      hitCount=hitCount+1
      sleep(0.1)
else:
   mc.postToChat("You punched 20 woods!")

   '''checked off on devin's computer'''
