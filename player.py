import pygame.sprite

# inizializzazione di ogni player 
class Player(pygame.sprite.Sprite):

    def __init__(self, image, pos): #inizializzazione di ogni membro di questa classe, è il setup delle variabili
        super().__init__() #funzione speciale che richiama le funzioni del padre
        self.image = image #inizializzo
        self.rect = self.image.get_rect() #disegna automaticamente un rettangolo grande quanto l'immagine, e lo lega all'immagine
        self.rect.topleft = pos # il suo punto in alto a sinistra deve essere uguale alla posizione. questo perchè in pygame il centro dell'immagine è in alto a sinistra
        self.size = 256 #grandezza pixel mario


    def update(self):
        #qua si gestiscono tutti i cambiamenti di stato dello sprite.
        self.size -= 1
        self.image = pygame.transform.scale(self.image, (self.size,self.size)) #un sacco di mario che rimpiccioliscono

    def update(self):
        self.rect.x -= 1

        