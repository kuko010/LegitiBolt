execute anchored eyes positioned ^ ^ ^ run function #bs.raycast:run {with:
    {
        blocks: "function #bs.hitbox:callback/get_block_shape",
        ignored_blocks: "#air", 
        on_targeted_block:"function logicsim:raycast/on_hit"
    }
}