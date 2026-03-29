import pgzrun,random,pyautogui

print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()
TITLE="endless_shooter_game"

zombies=["zombanim_1", "zombanim_1.2"]
coins=[]
enemies=[]
index=0
powers=[]
score=0
lives=3
gamestate="start"
collected_coins=0
character=Actor("new-character1.png")
character.pos=(100,HEIGHT/2)



def create_enemies():
    if gamestate == "play":
        enemy=Actor("enemy.png")
        enemy.pos=(WIDTH,random.randint(0,HEIGHT-50))
        enemies.append(enemy)

def create_coins():
    if gamestate == "play":
        coin=Actor("goldcoin.png")
        coin.pos=(WIDTH,random.randint(0,HEIGHT-50))
        coins.append(coin)



def draw():
    screen.blit("background.png", (0,0))
    character.draw()
    if gamestate == "start":
        screen.draw.text("Press space to start the game \n Press up and down keys to control character \n Press space to shoot \n You have three lives \n shoot the zombies to score",center=(WIDTH//2,HEIGHT//2))
    elif gamestate == "play":    
        for i in enemies:
            i.draw()
        for i in powers:
            i.draw()
        for i in coins:
            i.draw()
        screen.draw.text(f"SCORE={score}",(50,50))
        screen.draw.text(f"LIVES={lives}",center=(WIDTH//2,50))
        screen.draw.text(f"COINS={collected_coins}",(WIDTH-200,50))
    else:
        screen.draw.text("Gameover",center = (WIDTH//2,HEIGHT//2), fontsize=40 )

    

def update():
    global score, lives, gamestate, collected_coins
    if keyboard.space and gamestate !="play":
        gamestate="play"
        score=0
        lives=3
    if gamestate == "play":

        if keyboard.up:
            character.y-=10
        if keyboard.down:
            character.y+=10
        if character.y < 0:
            character.y=HEIGHT
        if character.y > HEIGHT:
            character.y=0
        
        for i in powers:
            i.x+=4
            if i.x > WIDTH:
                powers.remove(i)
            for e in enemies:
                if e.colliderect(i):
                    enemies.remove(e)
                    powers.remove(i)
                    score+=1
                    break

        for i in enemies:
            i.x-=4
            if i.x < 0:
                enemies.remove(i)
            if character.colliderect(i):
                enemies.remove(i)
                if lives > 0:
                    lives-=1
                if lives==0:
                    gamestate="end"
        
        for i in coins:
            i.x-=4
            if i.x < 0:
                coins.remove(i)
            if character.colliderect(i):
                coins.remove(i)
                collected_coins+=1
        
def change_zombies():
    global index
    index = (index+1)%2
    for i in enemies:
        i.image=zombies[index]



clock.schedule_interval(change_zombies,0.5)   
clock.schedule_interval(create_enemies,2)
clock.schedule_interval(create_coins,2)

def on_key_down(key):
    if gamestate == "play" and key == keys.SPACE:
            projectile=Actor("projectile2.png")
            projectile.pos=character.x+60,character.y-60
            powers.append(projectile)


pgzrun.go()