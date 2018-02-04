# -*- coding: utf-8 -*-

""" 
 Sencilla demo gráfica
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
# Importamos una biblioteca de funciones llamada 'pygame'
import pygame
 
# Inicializamos el motor de juegos
pygame.init()
 
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
 
PI = 3.141592653
 
# Establecemos el largo y alto de la pantalla
dimensiones = (400, 500)
pantalla = pygame.display.set_mode(dimensiones)
 
pygame.display.set_caption("Divertido Juego del Profesor Craven")
 
#Iteramos hasta que el usuario haga click sobre el botón de salida.
hecho = False
reloj = pygame.time.Clock()
 
# Iteramos en el bucle hasta que hecho == False
while not hecho:
   
    for evento in pygame.event.get(): # El usuario realizó alguna acción
        if evento.type == pygame.QUIT: # Si el usuario hizo click sobre salir
            hecho = True # Marcamos que hemos acabado y abandonamos este bucle
 
    # Todo el código de dibujo sucede después del bucle for y dentro del bucle
    # while not hecho.
     
    # Limpiamos la pantalla y establecemos su fondo.    
    pantalla.fill(BLANCO)
 
    # Dibujamos sobre la pantalla una línea verde de 5 píxeles de ancho
    # que vaya desde (0,0) hasta (100,100).    
    pygame.draw.line(pantalla, VERDE, [0, 0], [100, 100], 5)
 
    # Usando un bucle for, dibujamos sobre la pantalla varias líneas rojas de 5 píxeles 
    # de ancho, que vayan desde (0,10) hasta (100,110).    
    for desplazar_y in range(0, 100, 10):
        pygame.draw.line(pantalla, ROJO, [0, 10 + desplazar_y], [100, 110 + desplazar_y], 5)
 
 
    # Dibujamos un rectángulo    
    pygame.draw.rect(pantalla, NEGRO, [20, 20, 250, 100], 2)
     
    # Dibujamos una elipse, usando un rectángulo para fijar sus bordes exteriores    
    pygame.draw.ellipse(pantalla, NEGRO, [20, 20, 250, 100], 2) 
 
    # Dibujamos un arco como parte de una elipse. 
    # Usamos radianes para determinar qué ángulo tenemos que dibujar.    
    pygame.draw.arc(pantalla, NEGRO, [20, 220, 250, 200], 0, PI / 2, 2)
    pygame.draw.arc(pantalla, VERDE, [20, 220, 250, 200], PI / 2, PI, 2)
    pygame.draw.arc(pantalla, AZUL, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
    pygame.draw.arc(pantalla, ROJO, [20, 220, 250, 200], 3 * PI / 2, 2 * PI, 2)
     
    # Aquí dibujamos un triángulo empleando el comando polygon.    
    pygame.draw.polygon(pantalla, NEGRO, [[100, 100], [0, 200], [200, 200]], 5)
 
    # Elegimos que tipo de fuente usar; fuente por defecto, y de 25 puntos.    
    fuente = pygame.font.Font(None, 25)
 
    # Creamos el texto. "True" significa texto con antialiasing. 
    # El color es negro. Esto nos crea una imagen de las letras, pero no las coloca 
    # sobre la pantalla.    
    texto = fuente.render("Mi texto", True, NEGRO)
 
    # Coloca la imagen del texto en pantalla sobre las coordenadas 250x250.    
    pantalla.blit(texto, [250, 250])
 
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    # Esto DEBE suceder después del resto de comandos de dibujo.    
    pygame.display.flip()
 
    # Aquí limitamos el bucle while a un máximo de 60 veces por segundo.
    #Lo dejamos aquí y usamos toda la CPU que podamos.    
    reloj.tick(60)
     
 
# Pórtate bien con el IDLE
pygame.quit()