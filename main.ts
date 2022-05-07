controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    animation.runImageAnimation(kirby, [img`
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 2 2 . . . . . . . . . 
                        . . . . . 2 2 . . . . . . . . . 
                        . . . . . 2 2 . . . . . . . . . 
                        . . 3 3 . 3 3 f 3 3 3 . . . . . 
                        . . 3 3 3 3 f 3 f 3 3 3 . . . . 
                        . . 3 3 3 3 f 3 f 3 3 3 . . . . 
                        . . 3 3 3 3 3 3 3 3 3 3 3 3 3 . 
                        . . . . 3 3 3 3 3 3 3 3 3 3 3 . 
                        . . . . 3 3 3 3 3 3 3 3 . 3 3 . 
                        . . . . . 3 3 3 3 3 3 . . 3 3 . 
                        . . . . . . . . 2 2 . . . . . . 
                        . . . . . . . . 2 2 . . . . . . 
                        . . . . . . . . 2 2 . . . . . .
            `, img`
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . 3 3 3 3 3 3 . . . . . . 
                        . . . 3 3 3 3 3 3 3 3 . . . . . 
                        3 3 3 3 3 3 3 3 3 3 3 3 3 3 . . 
                        3 3 3 3 3 3 f 3 f 3 3 3 3 3 . . 
                        . . . 3 3 3 f 3 f 3 3 3 3 3 . . 
                        . . . 3 3 3 3 3 3 3 3 . . . . . 
                        . . . . 3 3 3 f 3 3 . . . . . . 
                        . . . . 2 2 . . 2 2 . . . . . . 
                        . . . . 2 2 . . 2 2 . . . . . . 
                        . . . . . . . . 2 2 . . . . . .
            `, img`
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            `], 200, true)
})
function levelstart() {
    if (currentlevel == 1) {
        tiles.setCurrentTilemap(tilemap`
            level9
        `)
        scene.setBackgroundColor(7)
    } else if (currentlevel == 2) {
        kirby.setPosition(52, 77)
        tiles.setCurrentTilemap(tilemap`
            level10
        `)
    } else if (currentlevel == 4) {
        kirby.setPosition(73, 90)
        tiles.setCurrentTilemap(tilemap`
            level5
        `)
        scene.setBackgroundColor(12)
    } else if (currentlevel == 5) {
        kirby.setPosition(143, 9)
        tiles.setCurrentTilemap(tilemap`
            level6
        `)
        scene.setBackgroundColor(9)
    } else if (currentlevel == 6) {
        kirby.setPosition(140, 102)
        tiles.setCurrentTilemap(tilemap`
            level7
        `)
        scene.setBackgroundColor(15)
    } else {
        
    }
    
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    star = sprites.createProjectileFromSide(img`
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 5 5 . . 5 . . . . 
                    . . . . 5 5 . . 5 . 5 5 . . . . 
                    . . . . . . 5 . 5 5 5 . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . 5 5 5 5 5 5 5 5 5 5 5 5 . 
                    . . . . . . 5 5 5 5 5 . . . . . 
                    . . . . . . 5 5 5 . 5 . . . . . 
                    . . . . . 5 5 . 5 . . . . . . . 
                    . . . . 5 5 . . 5 . . . . . . . 
                    . . . . 5 . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        `, 50, 50)
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.brick, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    
    currentlevel += 3
    levelstart()
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    animation.runImageAnimation(kirby, assets.animation`
        walk
    `, 200, true)
})
controller.right.onEvent(ControllerButtonEvent.Released, function on_right_released() {
    animation.runImageAnimation(kirby, [img`
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 3 3 3 3 3 . . . . . . 
                        . . . . 3 3 3 3 3 3 3 . . . . . 
                        . 3 3 3 3 3 3 f 3 f 3 3 3 3 . . 
                        . 3 3 3 3 3 3 f 3 f 3 3 3 3 . . 
                        . 3 3 3 3 3 3 3 3 3 3 3 3 3 . . 
                        . . . . 3 3 3 3 f 3 3 . . . . . 
                        . . 2 2 2 3 3 3 3 3 3 2 2 . . . 
                        . 2 2 2 2 . . . . . 2 2 2 2 . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            `, img`
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . 3 3 3 3 3 . . . . . 
                        . . . . . 3 3 3 3 3 3 3 . . . . 
                        . . 3 3 3 3 3 3 f 3 f 3 3 3 3 . 
                        . . 3 3 3 3 3 3 f 3 f 3 3 3 3 . 
                        . . 3 3 3 3 3 3 3 3 3 3 3 3 3 . 
                        . . . . . 3 3 3 3 f 3 3 . . . . 
                        . . . 2 2 3 3 3 3 3 2 2 2 . . . 
                        . . 2 2 2 2 . . . . 2 2 2 2 . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            `], 200, true)
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.oceanDepths9, function on_overlap_tile2(sprite2: Sprite, location2: tiles.Location) {
    
    currentlevel += 4
    levelstart()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.darkGroundCenter, function on_overlap_tile3(sprite3: Sprite, location3: tiles.Location) {
    
    currentlevel += 1
    levelstart()
})
controller.down.onEvent(ControllerButtonEvent.Repeated, function on_down_repeated() {
    animation.runImageAnimation(kirby, [img`
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 3 3 3 3 3 . . . . . . 
                        . . . . 3 3 3 3 3 3 3 . . . . . 
                        . 3 3 3 3 3 3 3 3 3 3 3 3 3 . . 
                        . 3 3 3 3 3 f 3 f 3 3 3 3 3 . . 
                        . 3 3 3 3 3 f 3 f 3 3 . . . . . 
                        . . . . 3 3 3 3 3 3 3 . . . . . 
                        . . . . . 3 3 f 3 3 . . . . . . 
                        . . . . . 2 2 . 2 2 . . . . . . 
                        . . . . . . . . 2 2 . . . . . .
            `, img`
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . 3 3 3 3 3 3 . . . . . . 
                        . . . 3 3 3 3 3 3 3 3 . . . . . 
                        3 3 3 3 3 3 3 3 3 3 3 3 3 3 . . 
                        3 3 3 3 3 3 f 3 f 3 3 3 3 3 . . 
                        . . . 3 3 3 f 3 f 3 3 3 3 3 . . 
                        . . . 3 3 3 3 3 3 3 3 . . . . . 
                        . . . . 3 3 3 f 3 3 . . . . . . 
                        . . . . 2 2 . . 2 2 . . . . . . 
                        . . . . 2 2 . . 2 2 . . . . . . 
                        . . . . . . . . 2 2 . . . . . .
            `], 200, true)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestOpen, function on_overlap_tile4(sprite4: Sprite, location4: tiles.Location) {
    
    currentlevel += 5
    levelstart()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleInsignia, function on_overlap_tile5(sprite5: Sprite, location5: tiles.Location) {
    
    currentlevel += 2
    levelstart()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap(sprite6: Sprite, otherSprite: Sprite) {
    game.over(false)
})
let Dark_puff : Sprite = null
let star : Sprite = null
let currentlevel = 0
let kirby : Sprite = null
kirby = sprites.create(img`
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . 3 3 3 3 3 3 . . . . . 
            . . . . 3 3 3 3 3 3 3 3 . . . . 
            . . . . 3 3 f 3 f 3 3 3 . . . . 
            . 3 3 3 3 3 f 3 f 3 3 3 3 3 3 . 
            . 3 3 3 3 3 f 3 f 3 3 3 3 3 3 . 
            . 3 3 3 3 3 3 3 3 3 3 3 3 3 3 . 
            . . . . 3 3 3 f 3 3 3 3 . . . . 
            . . . . . 3 3 3 3 3 3 . . . . . 
            . . . 2 2 3 3 3 2 2 2 2 . . . . 
            . . 2 2 2 2 2 . 2 2 2 2 2 . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    `, SpriteKind.Player)
controller.moveSprite(kirby)
currentlevel += 1
levelstart()
scene.cameraFollowSprite(kirby)
let projectile = sprites.createProjectileFromSide(img`
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . 5 . . . . 5 . . 
            . . . . 5 5 . . 5 . . . 5 5 . . 
            . . . . . 5 . . 5 . . 5 . . . . 
            . . . . . 5 5 . 5 . 5 5 . . . . 
            . . . . . . 5 5 5 5 . . 5 5 . . 
            . . . . 5 5 5 5 5 5 5 5 5 . . . 
            . . . . . . 5 5 5 5 . . . . . . 
            . . . . . 5 5 . 5 5 5 . . . . . 
            . . . . 5 5 . . 5 . . . . . . . 
            . . . . . . . . 5 . . . . . . . 
            . . . . . . . . 5 . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    `, 50, 50)
forever(function on_forever() {
    Dark_puff.setVelocity(-50, 0)
    Dark_puff.setFlag(SpriteFlag.AutoDestroy, true)
})
game.onUpdateInterval(500, function on_update_interval() {
    
    Dark_puff = sprites.create(img`
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . . f f f f f f f . . . . . 
                    . f f f f f 1 f 1 f f f f f . . 
                    . f f f f f 1 f 1 f f f f f . . 
                    . f f f f f f f f f f f f f . . 
                    . . . . f f f 1 f f f . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . f f f f . f f f f . . . . 
                    . . f f f f f . f f f f f . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        `, SpriteKind.Enemy)
    Dark_puff.setPosition(scene.screenWidth(), randint(3, scene.screenHeight()))
})
