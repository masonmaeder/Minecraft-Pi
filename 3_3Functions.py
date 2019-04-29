from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()
#get user input for the number of floors and convert to an integer
numFloors=int(input("Enter the number of floors:"))
#----------------------------------------------------------------------------------------
size=12
def House():
    mc.setBlocks(hx, hy, hz, hx+size, hy+size/2, hz+size, 112)
    mc.setBlocks(hx+1, hy+1, hz+1, hx+size-1, hy+size/2-1, hz+size-1, 0)  
    #door code
    mc.setBlock(hx+size/2, hy+1, hz, 64, 7)
    mc.setBlock(hx+size/2, hy+2, hz, 64, 8)
    #window left of door
    mc.setBlocks(hx+2, hy+2, hz, hx+size/2-2, hy+size/2-2, hz, 102)
    #window right of door
    mc.setBlocks(hx+size/2+2, hy+2, hz, hx+size-2, hy+size/2-2, hz, 102)
    #windows on back wall
    mc.setBlocks(hx+2, hy+2, hz+size, hx+size/2-2, hy+size/2-2, hz+size, 102)
    mc.setBlocks(hx+size/2+2, hy+2, hz+size, hx+size-2, hy+size/2-2, hz+size, 102)
    #bed
    mc.setBlock(hx+1, hy+1, hz+size-1, 26, 8)
    mc.setBlock(hx+1, hy+1, hz+size-2, 26, 4)
    mc.setBlock(hx+size-1, hy+1, hz+size-1, 26, 8)
    mc.setBlock(hx+size-1, hy+1, hz+size-2, 26, 4)
    #flower under windows
    mc.setBlocks(hx+2, hy+1, hz-1, hx+size/2-2, hy+size/2-5, hz-1, 38)
    mc.setBlocks(hx+size/2+2, hy+1, hz-1, hx+size-2, hy+size/2-5, hz-1, 38)
    
def Roof():
    #terraced roof
    mc.setBlocks(hx-1,hy+size/2, hz-1, hx+size+1, hy+size/2, hz+size+1, 4)
    mc.setBlocks(hx,hy+size/2+1, hz, hx+size, hy+size/2+1, hz+size, 4)
    mc.setBlocks(hx+1,hy+size/2+2, hz+1, hx+size-1, hy+size/2+2, hz+size-1, 4)
    mc.setBlocks(hx+2,hy+size/2+3, hz+2, hx+size-2, hy+size/2+3, hz+size-2, 4)
   
def OtherFloor(oy):
    mc.setBlocks(hx, oy, hz, hx+size, oy+size/2, hz+size, 112)
    mc.setBlocks(hx+1, oy, hz+1, hx+size-1, oy+size/2-1, hz+size-1, 0)  
    #windows on front wall
    mc.setBlocks(hx+2, oy+2, hz, hx+size/2-2, oy+size/2-2, hz, 102)
    mc.setBlocks(hx+size/2+2, oy+2, hz, hx+size-2, oy+size/2-2, hz, 102)
    #windows on back wall
    mc.setBlocks(hx+2, oy+2, hz+size, hx+size/2-2, oy+size/2-2, hz+size, 102)
    mc.setBlocks(hx+size/2+2, oy+2, hz+size, hx+size-2, oy+size/2-2, hz+size, 102)
    
def Stairs(sy):
   #stairs up to next floor
   for a in range(int(size/2)+1):
     	mc.setBlocks(hx+size/2, sy+a, hz+size/2+a-1, hx+size/2+1, sy+a, hz+size/2+a-1, 67, 2)
     	#Creates the gap to walk
     	mc.setBlocks(hx+size/2, sy+1+a, hz+size/2+a-1, hx+size/2+1, sy+1+a, hz+size/2+a-1, 0)
     	mc.setBlocks(hx+size/2, sy+2+a, hz+size/2+a-1, hx+size/2+1, sy+2+a, hz+size/2+a-1, 0)
     	mc.setBlocks(hx+size/2, sy+3+a, hz+size/2+a-1, hx+size/2+1, sy+3+a,hz+size/2+a-1, 0)

def Trees():
    block = 17
    rand = random.randint (1,2)
    if rand ==1:
        x,y,z=mc.player.getPos()
        #leaves
        mc.setBlocks(x+11, y+4, z-2, x+7, y+3, z-2, 18)
        mc.setBlocks(x+10, y+4, z-4, x+8, y+3, z-4, 18)
        mc.setBlocks(x+10, y+4, z-1, x+8, y+3, z, 18)
        mc.setBlocks(x+11, y+4, z-2, x+7, y+3, z-1, 18)
        mc.setBlocks(x+11, y+4, z-2, x+7, y+3, z-3, 18)
        mc.setBlocks(x+10, y+5, z-1, x+8, y+5, z-3, 18)
        mc.setBlocks(x+9, y+6, z-1, x+9, y+6, z-3, 18)
        mc.setBlocks(x+10, y+6, z-2, x+8, y+6, z-2, 18)
        #trunk
        mc.setBlocks(x+9, y, z-2, x+9, y+5, z-2, 17)
    else:
        x,y,z=mc.player.getPos()
        #leaves
        mc.setBlocks(x+11, y+4, z-2, x+7, y+3, z-2, 18)
        mc.setBlocks(x+10, y+4, z-4, x+8, y+3, z-4, 18)
        mc.setBlocks(x+10, y+4, z-1, x+8, y+3, z, 18)
        mc.setBlocks(x+11, y+4, z-2, x+7, y+3, z-1, 18)
        mc.setBlocks(x+11, y+4, z-2, x+7, y+3, z-3, 18)
        mc.setBlocks(x+10, y+5, z-1, x+8, y+5, z-3, 18)
        mc.setBlocks(x+9, y+6, z-1, x+9, y+6, z-3, 18)
        mc.setBlocks(x+10, y+6, z-2, x+8, y+6, z-2, 18)
        #trunk
        mc.setBlocks(x+9, y, z-2, x+9, y+5, z-2, 17,2)
#-----------------------------------------------------------------------------------------
x, y, z = mc.player.getPos()
hx=x+5
hy=y-1
hz=z+5
House()
Stairs(hy)
for b in range(numFloors-1):
       hy=hy+size/2+1
       OtherFloor(hy)
       Stairs(hy)
Roof()
Trees()
