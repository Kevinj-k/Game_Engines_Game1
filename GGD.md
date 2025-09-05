# GGD 
goblin game

The player is a goblin and your goal is to kill as many villagers in a specific amount of time. Originally I thought of when you kill the villagers and they drop coins but that seemed a little out of my scope of time.



Assets
Goblin - https://opengameart.org/content/lpc-goblin
Sword slash - https://opengameart.org/content/pixel-art-sword-slash-effect
Villager - https://opengameart.org/content/person-man-png
Village background - https://openclipart.org/detail/265290/crooked-village-01



The goblin is the player. He has an animation set for moving left,right,up, and down.This sprite is there from start to finish,

The slash is just that: a slash that displays depending on the direction of the goblin model. Its born on a timer; it stays for a few frames and then disappears until the player presses space again. It can collide with villagers to kill them and give the player points.

Villager sprite walks from left to right, granted he floats, but moves left to right. When he gets hit by the slash he resets and gives the player a point.
     




