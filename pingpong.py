import pygame
pygame.init()
from random import randint

colb = (56, 30, 4)
b = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Пинг Понг")

clock = pygame.time.Clock()

end_time = 0
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = colb

        if color:
            self.fill_color = color

    def addcolor(self, newcolor):
        self.fill_color = newcolor

    def fillcolor(self):
        pygame.draw.rect(b, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def text(self, text, fsize=35, text_color=(255, 0, 0)):
        self.image = pygame.font.Font(None, fsize).render(
            text, True, text_color
        )

    def write(self, shift_x=0, shift_y=0):
        pygame.draw.rect(b, self.fill_color, self.rect)
        b.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):
    def __init__(self, name, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)

        self.image = pygame.image.load(name)
        self.image = pygame.transform.scale(self.image,(width, height))

    def draw(self):
        b.blit(self.image,(self.rect.x, self.rect.y))


speed_x = 3
speed_y = 3

game = True


platform1 = Area(20, 200, 20, 100, (30, 60, 120))
platform2 = Area(460, 200, 20, 100, (30, 60, 120))


ball = Picture("ball11.png", 225, 225, 50, 50)


move_up1 = False
move_down1 = False

move_up2 = False
move_down2 = False

t1 = Area(85, 250, 1, 1, (56, 30, 4))

t2 = Area(7, 10, 1, 1, (56, 30, 4))
t3 = Area(110, 10, 1, 1, (56, 30, 4))

t4 = Area(350, 10, 1, 1, (56, 30, 4))
t5 = Area(453, 10, 1, 1, (56, 30, 4))

finish = False
score1 = 0

p1_sp = 7
p2_sp = 7


score2 = 0
while game:
    b.fill(colb)

    if finish!=True:
        t2.text("Счет 1п:", text_color=(255, 255, 255))
        t3.text(str(score1), text_color=(255, 255, 255))
        t2.write(10, 10)
        t3.write(10, 10)

        t4.text("Счет 2п:", text_color=(255, 255, 255))
        t5.text(str(score2), text_color=(255, 255, 255))
        t4.write(10, 10)
        t5.write(10, 10)

        for e in pygame.event.get():


            if e.type == pygame.QUIT:
                game = False

            if e.type == pygame.KEYDOWN:

                if e.key == pygame.K_1:

                    bonus = randint(1, 4)

                    if bonus == 1:
                        platform1.rect.height = 150

                    elif bonus == 2:
                        platform2.rect.height = 150

                    elif bonus == 3:
                        speed_x *= 2
                        speed_y *= 2

                    elif bonus == 4:
                        platform1_speed = 12


            if e.type == pygame.KEYDOWN:


                if e.key == pygame.K_w:
                    move_up1 = True

                if e.key == pygame.K_s:
                    move_down1 = True


                if e.key == pygame.K_UP:
                    move_up2 = True

                if e.key == pygame.K_DOWN:
                    move_down2 = True

            if e.type == pygame.KEYUP:


                if e.key == pygame.K_w:
                    move_up1 = False

                if e.key == pygame.K_s:
                    move_down1 = False


                if e.key == pygame.K_UP:
                    move_up2 = False

                if e.key == pygame.K_DOWN:
                    move_down2 = False

        if move_up1 and platform1.rect.y > 0:
            platform1.rect.y -= p1_sp

        if move_down1 and platform1.rect.y < 400:
            platform1.rect.y += p1_sp


        if move_up2 and platform2.rect.y > 0:
            platform2.rect.y -= p2_sp

        if move_down2 and platform2.rect.y < 400:
            platform2.rect.y += p2_sp


        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if ball.rect.top <= 0:
            ball.rect.top = 0
            speed_y *= -1


        if ball.rect.bottom >= 500:
            ball.rect.bottom = 500
            speed_y *= -1


        if ball.colliderect(platform1.rect) and speed_x < 0:

            ball.rect.left = platform1.rect.right

            speed_x *= -1



        if ball.colliderect(platform2.rect) and speed_x > 0:

            ball.rect.right = platform2.rect.left

            speed_x *= -1

        if ball.rect.right < 0:
            score2+=1
            ball.rect.left = platform1.rect.right
            speed_x *= -1

        if ball.rect.left > 500:
            score1+=1
            ball.rect.right = platform2.rect.left
            speed_x *= -1

        if score1>=2:
            t1.text("Победила 1-ая платформа", text_color=(0, 255, 0))
            end_time = pygame.time.get_ticks()+5000
            finish = True
        if score2>=2:
            t1.text("Победила 2-ая платформа", text_color=(0, 255, 0))
            finish = True
            end_time = pygame.time.get_ticks()+5000




        platform1.fillcolor()
        platform2.fillcolor()
        ball.draw()
    if end_time!=0:
        t1.write(10, 10)
        if pygame.time.get_ticks()>=end_time:
            game=False


    pygame.display.update()

    clock.tick(100)
