from mcpi.minecraft import Minecraft
mc = Minecraft.create()

wool=35
clay=159
pos = mc.player.getPos()
x=pos.x+2
y=pos.y+10
z=pos.z+2
def creeper(hx, hy, hz):
    grid=[[13,13,13,13,13,13,13,13],
         [13,13,13,13,13,13,13,13],
         [13,15,15,13,13,15,15,13],
         [13,15,15,13,13,15,15,13],
         [13,13,13,15,15,13,13,13],
         [13,13,15,15,15,15,13,13],
         [13,13,15,15,15,15,13,13],
         [13,13,15,13,13,15,13,13],]
    for row in range(len(grid)): 
              for col in range(len(grid[row])):
                 mc.setBlock(hx, hy-row, hz+col, wool, grid[row][col])

def steve(hx, hy, hz, sz):
    grid=[[15,15,15,15,15,15,15,15],
         [15,15,15,15,15,15,15,15],
         [15,8,8,8,8,8,8,15],
         [8,8,8,8,8,8,8,8],
         [8,0,11,8,8,11,0,8],
         [8,8,8,12,12,8,8,8],
         [8,8,7,8,8,7,8,8],
         [8,8,7,7,7,7,8,8],]
    for row in range(len(grid)): 
              for col in range(len(grid[row])):
                 mc.setBlocks(hx, ((hy-((row)*sz))), (hz-((col)*sz)), hx, ((hy-((row+1)*sz-1))), (hz-((col+1)*sz-1)), clay, grid[row][col])

#creeper(x, y, z)
steve(x, y, z, 16)

