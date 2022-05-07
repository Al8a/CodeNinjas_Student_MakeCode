def on_up_pressed():
    animation.run_image_animation(kirby,
        [img("""
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
            """),
            img("""
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
            """),
            img("""
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
            """)],
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def levelstart():
    if currentlevel == 1:
        tiles.set_current_tilemap(tilemap("""
            level9
        """))
        scene.set_background_color(7)
    elif currentlevel == 2:
        kirby.set_position(52, 77)
        tiles.set_current_tilemap(tilemap("""
            level10
        """))
    elif currentlevel == 4:
        kirby.set_position(73, 90)
        tiles.set_current_tilemap(tilemap("""
            level5
        """))
        scene.set_background_color(12)
    elif currentlevel == 5:
        kirby.set_position(143, 9)
        tiles.set_current_tilemap(tilemap("""
            level6
        """))
        scene.set_background_color(9)
    elif currentlevel == 6:
        kirby.set_position(140, 102)
        tiles.set_current_tilemap(tilemap("""
            level7
        """))
        scene.set_background_color(15)
    else:
        pass

def on_a_pressed():
    global star
    star = sprites.create_projectile_from_side(img("""
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
        """),
        50,
        50)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    global currentlevel
    currentlevel += 3
    levelstart()
scene.on_overlap_tile(SpriteKind.player, sprites.builtin.brick, on_overlap_tile)

def on_left_pressed():
    animation.run_image_animation(kirby, assets.animation("""
        walk
    """), 200, True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    animation.run_image_animation(kirby,
        [img("""
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
            """),
            img("""
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
            """)],
        200,
        True)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_overlap_tile2(sprite2, location2):
    global currentlevel
    currentlevel += 4
    levelstart()
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.ocean_depths9,
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    global currentlevel
    currentlevel += 1
    levelstart()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.dark_ground_center,
    on_overlap_tile3)

def on_down_repeated():
    animation.run_image_animation(kirby,
        [img("""
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
            """),
            img("""
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
            """)],
        200,
        True)
controller.down.on_event(ControllerButtonEvent.REPEATED, on_down_repeated)

def on_overlap_tile4(sprite4, location4):
    global currentlevel
    currentlevel += 5
    levelstart()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_open,
    on_overlap_tile4)

def on_overlap_tile5(sprite5, location5):
    global currentlevel
    currentlevel += 2
    levelstart()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile5)

def on_on_overlap(sprite6, otherSprite):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

Dark_puff: Sprite = None
star: Sprite = None
currentlevel = 0
kirby: Sprite = None
kirby = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(kirby)
currentlevel += 1
levelstart()
scene.camera_follow_sprite(kirby)
projectile = sprites.create_projectile_from_side(img("""
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
    """),
    50,
    50)

def on_forever():
    Dark_puff.set_velocity(-50, 0)
    Dark_puff.set_flag(SpriteFlag.AUTO_DESTROY, True)
forever(on_forever)

def on_update_interval():
    global Dark_puff
    Dark_puff = sprites.create(img("""
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
        """),
        SpriteKind.enemy)
    Dark_puff.set_position(scene.screen_width(), randint(3, scene.screen_height()))
game.on_update_interval(500, on_update_interval)
