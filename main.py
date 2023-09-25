import pygame
import sys
from CONST import *
from player import Player
from plataforma import Plataforma
from enemy import Enemy
from money import Money
import sqlite3
import json
from others import saveScoreInDataBase,top_five_score
from button import Button
###############

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()


pygame.mixer.init()
sound = pygame.mixer.Sound('music/Introduccion.mp3')
sound.set_volume(0.1)
sound.play(-1)



clock = pygame.time.Clock()
delta_ms = 0
#DB
score = 0
font_score = pygame.font.Font('font/Metal Slug Latino Regular.ttf', 36)
font_life = pygame.font.Font('font/Metal Slug Latino Regular.ttf', 36)
font_lvl = pygame.font.Font('font/Valorant-Font.ttf',100)
font = pygame.font.Font('font/Valorant-Font.ttf',30)

# Conexión a la base de datos
# Crea la tabla si no existe
connection = sqlite3.connect("puntajes.db")
cursor = connection.cursor()
create_table = '''
    CREATE TABLE IF NOT EXISTS score_player (
        name CHAR(10),
        score INTEGER
    )
'''
cursor.execute(create_table)
#input_name_player = pygame_textinput.TextInput(font_family="Arial", font_size=24)

name_player = 'Kakaroto'

# Guardar los cambios y cerrar la conexión
connection.commit()
connection.close()
nivel = 1
init_game = False
run_level = False
run = True
is_game_over = False

def on_click(parametro):
    print(f'Value param: {parametro}')


#Instancia de bottones
button_play = Button(screen,700,400,100,50,TRANSPARENTE,on_click,init_game,'Play','font/Valorant-Font.ttf',20,BLANCO)
button_score = Button(screen,700,450,100,50,TRANSPARENTE,on_click,False,'Score','font/Valorant-Font.ttf',20,BLANCO)
button_back = Button(screen,0 ,500,100,50,TRANSPARENTE,on_click,False,'Back','font/Valorant-Font.ttf',20,BLANCO)


def init_screen():
    imagen_fondo = pygame.transform.scale(pygame.image.load(f"image/Fondo.jpeg"),(ANCHO_VENTANA,ALTO_VENTANA))
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    if button_score.on_click_button:
        if button_back.on_click_button:
            button_score.on_click_button = not button_score.on_click_button
            button_back.on_click_button = button_score.on_click_button
        else:
            position_x = ANCHO_VENTANA / 2
            position_y = 50
            for registro_name,registro_score in top_five_score(cursor):
                texto = font.render(f'{registro_name} : {registro_score}',True,BLANCO,TRANSPARENTE)
                screen.blit(texto,(position_x,position_y))
                position_y += 40
            button_back.update(events)
            button_back.draw()
    else:
        button_play.update(events)
        button_play.draw()
        button_score.update(events)
        button_score.draw()

while run:
    events = pygame.event.get()
    pygame.time.delay(50) #Normaliza velocidad de juego.
    keys = pygame.key.get_pressed()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.can_shoot = True
            if event.key == pygame.K_UP:
                player.can_jump = True
        
            
    plataforma_image = pygame.transform.scale(pygame.image.load(f"image/plataforma.png"),(ANCHO_VENTANA,ALTO_VENTANA))

    if button_play.on_click_button:
        if not run_level:
            
            plataformas = []
            enemys = []
            monies = []
            imagen_fondo = pygame.transform.scale(pygame.image.load(f"image/score.jpeg"),(ANCHO_VENTANA,ALTO_VENTANA))
            screen.blit(imagen_fondo,imagen_fondo.get_rect())
            if nivel <= 3:
                #Lectura de arhivo JSON
                with open(f'datos_json/nivel_{nivel}.json', 'r') as archivo:
                    elements = json.load(archivo)
                init_text = font_lvl.render(f'Mision {nivel}', True, BLANCO)
                init_text_rect = init_text.get_rect()
                init_text_rect.center = imagen_fondo.get_rect().center
                press_text = font.render('Presionar Enter para continuar...',True, BLANCO)
                press_text_rect = init_text.get_rect()
                press_text_rect.center = imagen_fondo.get_rect().midbottom
                screen.blit(init_text, init_text_rect)
                screen.blit(press_text, press_text_rect)
            
            if keys[pygame.K_RETURN] and nivel <= 3:
                player = Player(x=0,y=0,speed=10,gravity=10,jump=20,jump_power=5,jump_height=100)
                run_level = True
                proyectiles = pygame.sprite.Group()
                
                #Plataformas
                for element in elements['nivel']['plataformas']:
                    plataformas.append(Plataforma(element['x'],element['y']))
                #Enemigos
                for element in elements['nivel']['enemigos']:
                    enemys.append(Enemy(element['x'],element['y'],element['time_animation'],element['speed'],element['position_wall_l'],element['position_wall_r']))
                #Mooney
                index = 0
                for element in elements['nivel']['monies']:
                    monies.append(Money(element['x'],element['y'],index))
                    index+=1                  
                imagen_fondo = pygame.transform.scale(pygame.image.load(f"image/nivel_{nivel}/background.jpg"),(ANCHO_VENTANA,ALTO_VENTANA))
        else:
            screen.blit(imagen_fondo,imagen_fondo.get_rect())
            if run_level:
                plataforma_image.set_colorkey(VERDE)
                screen.blit(plataforma_image,plataforma_image.get_rect())
            
            #Game Over
            if Player.life <= 0:
                if keys[pygame.K_RETURN]:
                    is_game_over = True
                press_text = font.render('Presionar Enter para continuar...',True, BLANCO)
                press_text_rect = init_text.get_rect()
                press_text_rect.center = imagen_fondo.get_rect().midtop
                screen.blit(GAME_OVER,GAME_OVER.get_rect()) 
                player._image.set_alpha(0)
                plataformas = [] 
                enemys = []
                monies = []
            
            #Pasar de nivel
            if len(monies) == 0 and Player.life > 0:
                nivel += 1
                run_level = False

            #Mostrar score
            score_text = font_score.render("Score: " + str(player.score), True, BLANCO)
            screen.blit(score_text, (10, 10))
            
            #Mostrar vida
            life_text = font_life.render("Lifes: " + str(player.life), True, BLANCO)
            screen.blit(life_text, (ANCHO_VENTANA-150, 10))
            
            player.events(keys,proyectiles,plataformas)
            player.update(plataformas,enemys,monies)
            proyectiles.update(player,enemys)    
                
            player.draw(screen)

            for plataforma in plataformas:
                    plataforma.draw(screen)


            for enemy in enemys:
                enemy.update()
                enemy.draw(screen)
            for proyectil in proyectiles:
                proyectil.draw(screen)

            for money in monies:
                money.draw(screen)
    else:
        init_screen()
        
    #Reinicia el Juego
    if is_game_over or nivel >= 4:
        saveScoreInDataBase(cursor,name_player,Player.score)
        Player.score = 0
        Player.life = 3
        button_play.on_click_button = False
        nivel = 1
        is_game_over = False

    pygame.display.flip()
    
    delta_ms += clock.tick(FPS)

    






