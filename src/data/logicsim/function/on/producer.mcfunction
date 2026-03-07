execute if block ~ ~ ~ furnace[lit=true]:
    summon minecraft:armor_stand ~0.5 ~ ~0.5 {Invisible:1b,Marker:1b,NoGravity:1b}
    execute if block ~ ~ ~ minecraft:furnace[facing=north] run function logicsim:look/north
    execute if block ~ ~ ~ minecraft:furnace[facing=west] run say west
    execute if block ~ ~ ~ minecraft:furnace[facing=east] run say east
    execute if block ~ ~ ~ minecraft:furnace[facing=south] run say east


#  summon minecraft:armor_stand ~0.5 ~ ~0.5 {Invisible:1b,Marker:1b,NoGravity:1b}

# -- /execute as @e[type=minecraft:armor_stand,distance=1..2,limit=1] run data modify entity @s Rotation set from block
# /execute if block 32 61 20 minecraft:furnace[facing=north] run say yes
#  execute as @a if block 32 61 20 minecraft:furnace[facing=north] run return run say e

