from upemtk import*
import time
#######################################################################################################
#---------------------------------------Les Fonctionss------------------------------------------------#
#######################################################################################################

#Dessine le Serpent
def dessiner_serpent(x,y,tag):
	cercle(x,y,6,tag=tag)
	cercle(x-1,y-1,1,tag=tag)
	cercle(x+2,y-1,1,tag=tag)
	cercle(x-10,y,4,tag=tag)
	cercle(x-18,y,3,tag=tag)
	
#affecte les touche 
def touche_ou_pas():
	evenement = donne_evenement()
	type_ev = type_evenement(evenement)
	if type_ev == 'Touche':
		return touche(evenement)
	else: 
		return 'pas touche'
		
#Deplace le Serpent
def deplacer_serpent(x_serpent,y_serpent):
	efface ('serpent')
	dessiner_serpent(x_serpent,y_serpent,tag='serpent')
              
            
#Affiche un texte avant le Depart
def affiche_texte_centre_et_attend_clic(pixel,largeur_fenetre, hauteur_fenetre):
	#texte(message,largeur_fenetre/4,hauteur_fenetre/2,)
	texte(300,220,"À vos marques.Prêt...Partez!",tag='message')
	attente_clic()
	efface_tout()
	
#delimite le terrain '''a revoir'''#############	
#def bordure(largeur_fenetre,hauteur_fenetre):###
#            i=0
#           bord=largeur_fenetre*hauteur_fenetre
#            while i<bord:
#                rect1 = rectangle(5, 5)
#                i+=1
	
##############################################	

#permet de faire bouger le serpent
def mise_a_jour_vitesse(nom_touche,vitesse,dx,dy):
	if nom_touche =='Right':
		dx=1
		dy=0
		return(dx,dy)
	elif nom_touche== 'Left':
		dx=-1
		dy=0
		return(dx,dy)
	elif nom_touche=='Up':
		dx=0
		dy=-1
		return(dx,dy)
	elif nom_touche=='Down':
		dx=0
		dy=1
		return(dx,dy)
	elif nom_touche=='pas touche':
		return(dx,dy)
#detecte les bords		
def detection_bords(x,y,largeur_fenetre, hauteur_fenetre):
	if x_serpent<0 or x_serpent>largeur_fenetre or y_serpent<0 or y_serpent>hauteur_fenetre:
		return True
	

 #creer une fenetre    
largeur_fenetre = 800
hauteur_fenetre = 600
cree_fenetre(largeur_fenetre, hauteur_fenetre)
#######################################################################################################
#----------------------------------Les Variables------------------------------------------------------#
#######################################################################################################

### affichage du message avant le depart du serpent ###
print("######################'Bienvenue'#################"'\n'
      "##Le but du Jeux est de faire bouger un serpent####"'\n'
      "##############Simple Mais Fun!!!Non?###############"'\n'
      "######################'Bon Jeux'####################")

# choix de la position de depart
x_serpent = 400
y_serpent = 500
pixel=0


# affichage du serpent au depart
message="À vos marques.Prêt...Partez!" 

# choix du deplacement du serpent
vitesse = 1
dx = 1
dy = 0


#message="À vos marques. Prêt? Partez!"

#######################################################################################################
#---------------------------------Corps Principal ----------------------------------------------------#
#######################################################################################################

affiche_texte_centre_et_attend_clic(largeur_fenetre,hauteur_fenetre,message)
# debut de la boucle
while x_serpent<800 and x_serpent>0 and y_serpent<600 and y_serpent>0:
	deplacer_serpent(x_serpent,y_serpent)
	mise_a_jour()
	z=touche_ou_pas()
	(dx,dy)=mise_a_jour_vitesse(z,1,dx,dy)
	x_serpent+=dx
	y_serpent+=dy
	pixel+=vitesse
	
	detection_bords(x_serpent,y_serpent,largeur_fenetre,hauteur_fenetre)
	time.sleep(0.005)
texte(largeur_fenetre/2,hauteur_fenetre/2,pixel)
print('la distance parcourue est de',pixel)
attente_clic()
# fin de la boucle
#######################################################################################################
#---------------------------------------Les appel de fonction-----------------------------------------#
#######################################################################################################
dessiner_serpent(x_serpent,y_serpent,'serpent')
deplacer_serpent(x_serpent,y_serpent)
touche_ou_pas()
attente_clic()
ferme_fenetre()

