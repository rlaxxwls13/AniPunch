import pygame
import sys
import random
import time
from enum import Enum


rgb = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'BLUE': (0, 0, 255),
    'GREEN': (0, 255, 0),
    'RED': (255, 0, 0),
    'YELLOW': (255, 255, 0),
    'PINK' : (255, 125, 125)
}

# 스크린 크기
screen_width = 480
screen_height = 640

target_spawn_delay = 1500  # target 생성 주기


# 충돌인지 확인하는 함수
def check_collision(m, t):
    missile_rect = m.missile.get_rect()
    missile_rect.x = m.x
    missile_rect.y = m.y

    target_rect = t.target.get_rect()
    target_rect.x = t.x
    target_rect.y = t.y

    if missile_rect.colliderect(target_rect) and t.status == m.status:
        return True

    return False


class Skill(Enum):
    KITTY = 0
    BUNNY = 1
    PUPPY = 2


class Observer:
    def update(self, game):
        pass


# target speed를 증가시키는 observer
class SpeedObserver(Observer):
    def update(self, game):  # 점수가 10점 높아질 때마다 target speed 1 증가(20일 때 제외)
        if game.previous_count % 10 == 9 and game.shoot_count % 10 == 0 and game.shoot_count != 20:
            game.target_speed += 1


# skill을 추가시키는 observer
class WeightObserver(Observer):
    def update(self, game):  # 점수가 20점 이상이 되면 skill 하나 추가
        if game.shoot_count >= 20:
            game.animal_type = 3
            game.fish_weight = 0.33
            game.carrot_weight = 0.33
            game.bone_weight = 0.34


class User:
    def __init__(self):
        self.user = pygame.image.load('user_kitty.png')
        self.user_size = self.user.get_rect()
        self.user_width = self.user_size.width
        self.user_height = self.user_size.height * 1.5

        self.userX = 0

        self.x = screen_width * 0.5 - self.user_width / 2
        self.y = screen_height - self.user_height


class Missile:
    def __init__(self, x=0, y=0):
        self.missile = pygame.image.load('kitty.png')
        self.x = x
        self.y = y
        self.status = Skill.KITTY

    # Prototype Pattern
    def clone(self, x, y):
        # pygame.surface는 deepcopy가 적용 안됨. 따라서 새로운 객체를 생성하고 pygame.surface 객체는 따로 copy를 해줘야함
        # (안그러면 원본 pygame.surface객체와 동일한 객체를 참조하게 됨)
        cloned_missile = Missile(x, y)
        cloned_missile.missile = self.missile.copy()
        return cloned_missile


class TargetBuilder:
    def __init__(self):
        self.x = None
        self.y = None
        self.status = None
        self.speed = None

    def set_status(self, status):
        self.status = status
        return self

    def set_xy(self, x, y):
        self.x = x
        self.y = y
        return self

    def set_speed(self, speed):
        self.speed = speed
        return self

    def build(self):
        if self.status == Skill.KITTY:
            fish = Fish(self.x, self.y, self.status, self.speed)
            return fish
        elif self.status == Skill.BUNNY:
            carrot = Carrot(self.x, self.y, self.status, self.speed)
            return carrot
        else:
            bone = Bone(self.x, self.y, self.status, self.speed)
            return bone


class Target:
    def __init__(self, x, y, status, speed):
        self.target = None
        self.status = status
        self.x = x
        self.y = y
        self.speed = speed


class Fish(Target):
    def __init__(self, x, y, status, speed):
        super().__init__(x, y, status, speed)
        self.target = pygame.image.load('fish.png')


class Carrot(Target):
    def __init__(self, x, y, status, speed):
        super().__init__(x, y, status, speed)
        self.target = pygame.image.load('carrot.png')


class Bone(Target):
    def __init__(self, x, y, status, speed):
        super().__init__(x, y, status, speed)
        self.target = pygame.image.load('bone.png')


class Framework:
    def __init__(self):

        self.pygame = pygame
        self.screen = 0
        self.clock = 0
        self.elapsed_time = 0
        self.background = None
        self.background = pygame.image.load('background_pixel.png')

        self.missile_list = []
        self.target_list = []
        self.user = User()
        self.skill = Skill.KITTY
        self.missile = Missile()

        self.target_speed = 2
        self.shoot_count = 0
        self.previous_count = 0
        self.miss_count = 0

        # sound
        self.pygame.mixer.init()
        self.shoot_sound = pygame.mixer.Sound('Coin 1.mp3')
        self.missile_sound = pygame.mixer.Sound('Woosh Sound.mp3')
        self.leveup_sound = pygame.mixer.Sound('Glow 3.mp3')
        self.gameover_sound = pygame.mixer.Sound('12322.mp3')
        self.miss_sound = pygame.mixer.Sound('Error 10.mp3')
        pygame.mixer.music.load('8bittownthemesong-59266.mp3')

        self.animal_type = 2
        self.fish_weight = 0.5
        self.carrot_weight = 0.5
        self.bone_weight = 0.0

        self.LEVEL_UP = False

        self.observers = []
    
    # Observer Pattern
    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def set_display(self):
        pass

    def print_start(self):  # 시작화면 출력
        pass

    def game_start(self):   # 클릭시 게임 시작
        pass

    def ready(self):
        self.pygame.init()

    def handle_event(self):     # 사용자의 입력 감지
        pass

    def update_user_loc(self):  # user 위치 업데이트
        pass

    def update_skill(self):     # 스킬 변경
        pass

    def generate_target(self):  # target 생성
        pass

    def del_target_missile(self):   # 충돌한 target과 missile 제거
        pass

    def blit(self):     # 객체를 화면에 출력
        pass

    def level_up(self):
        pass

    def game_over(self):
        pass


class Anipunch(Framework):

    def set_display(self):
        self.screen = self.pygame.display.set_mode((screen_width, screen_height))
        self.pygame.display.set_caption('Anipunch')
        self.clock = self.pygame.time.Clock()

    def print_start(self):  # 시작화면 출력
        self.screen.blit(self.background, (0, 0))
        start_text = pygame.image.load('logo.png')
        startpos = start_text.get_rect()
        startpos.center = (screen_width / 2, screen_height / 2)

        font = pygame.font.Font('DungGeunMo.ttf', 20)
        click_text = font.render('[ click anywhere to begin ]', True, rgb['PINK'])
        clickpos = click_text.get_rect()
        clickpos.center = (screen_width / 2, 530)

        self.screen.blit(start_text, startpos)
        self.screen.blit(click_text, clickpos)
        pygame.display.update()

    def game_start(self):   # 클릭시 게임 시작
        click_event = False
        while not click_event:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.play(-1)
                    click_event = True

    def handle_event(self):     # 사용자의 입력 감지
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:  # user 위치 변경
                    self.user.userX -= 5

                elif event.key == pygame.K_RIGHT:   # user 위치 변경
                    self.user.userX += 5

                elif event.key == pygame.K_UP:     # 스킬 변경
                    self.skill = Skill((self.skill.value + 1) % self.animal_type)

                elif event.key == pygame.K_DOWN:   # 스킬 변경
                    self.skill = Skill((self.skill.value + self.animal_type - 1) % self.animal_type)

                elif event.key == pygame.K_SPACE:   # 미사일 발사
                    self.missile_sound.play()

                    # 미사일 위치(=user 위치)
                    x = self.user.x + self.user.user_width / 3
                    y = self.user.y

                    # 미사일 객체 생성(Prototype Pattern)
                    new_missile = self.missile.clone(x, y)
                    if self.skill == Skill.KITTY:
                        new_missile.status = Skill.KITTY
                        new_missile.missile = pygame.image.load('kitty.png')
                    elif self.skill == Skill.BUNNY:
                        new_missile.status = Skill.BUNNY
                        new_missile.missile = pygame.image.load('bunny.png')
                    else:
                        new_missile.status = Skill.PUPPY
                        new_missile.missile = pygame.image.load('puppy.png')
                    self.missile_list.append(new_missile)

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.user.userX = 0

    def update_user_loc(self):  # user 위치 업데이트
        self.user.x += self.user.userX
        if self.user.x < 0:
            self.user.x = 0
        elif self.user.x > screen_width - self.user.user_width:
            self.user.x = screen_width - self.user.user_width

    def update_skill(self):     # 스킬 변경
        if self.skill == Skill.KITTY:
            self.user.user = pygame.image.load('user_kitty.png')
        elif self.skill == Skill.BUNNY:
            self.user.user = pygame.image.load('user_bunny.png')
        else:
            self.user.user = pygame.image.load('user_puppy.png')

    def generate_target(self):  # target 생성
        # 생성할 타겟 랜덤으로 설정
        target_status = random.choices([Skill.KITTY, Skill.BUNNY, Skill.PUPPY],
                                       weights=[self.fish_weight, self.carrot_weight, self.bone_weight], k=1)[0]

        # 타겟 객체 생성(builder pattern)
        build_target = TargetBuilder()
        if self.elapsed_time >= target_spawn_delay:
            # 타겟의 x좌표 설정
            target_x = random.randrange(self.user.user_width // 3, screen_width - self.user.user_width * 2 // 3)
            new_target = build_target.set_status(target_status).set_xy(target_x, 0).set_speed(self.target_speed).build()
            self.target_list.append(new_target)
            self.elapsed_time = 0

    def del_target_missile(self):   # 충돌한 target과 missile 제거

        collided_missiles = []
        collided_targets = []

        active_missiles = []
        active_targets = []

        # 충돌 객체 저장
        for m in self.missile_list:
            for t in self.target_list:
                if check_collision(m, t):
                    self.shoot_sound.play()
                    self.shoot_count += 1
                    collided_missiles.append(m)
                    collided_targets.append(t)
                    break

        # 충돌 객체를 제거
        for m in collided_missiles:
            if m in self.missile_list:
                self.missile_list.remove(m)
        for t in collided_targets:
            if t in self.target_list:
                self.target_list.remove(t)

        # 화면을 벗어난 객체를 제거
        for m in self.missile_list:
            if m.y >= 0:
                m.y -= 10
                active_missiles.append(m)

        for t in self.target_list:
            if t.y <= screen_height:
                t.y += t.speed
                active_targets.append(t)
            else:
                self.miss_sound.play()
                self.miss_count += 1

        # 객체 리스트 갱신
        self.missile_list = active_missiles
        self.target_list = active_targets

    def blit(self):     # 객체를 화면에 출력

        # screen
        self.screen.blit(self.background, (0, 0))

        # user
        self.screen.blit(self.user.user, (self.user.x, self.user.y))

        # missile
        for m in self.missile_list:
            self.screen.blit(m.missile, (m.x, m.y))

        # target
        for n in self.target_list:
            self.screen.blit(n.target, (n.x, n.y))

        # life
        font = pygame.font.Font('DungGeunMo.ttf', 20)
        life_text = font.render('life: ', True, rgb['BLACK'])
        self.screen.blit(life_text, (5, 5))
        life_rect = life_text.get_rect()
        life_x = life_rect.width + 5

        if self.miss_count == 0:
            life = pygame.image.load("life_3.png")
            self.screen.blit(life, (life_x, 5))
        elif self.miss_count == 1:
            life = pygame.image.load("life_2.png")
            self.screen.blit(life, (life_x, 5))
        elif self.miss_count == 2:
            life = pygame.image.load("life_1.png")
            self.screen.blit(life, (life_x, 5))

        # score
        score_text = font.render(' score:   ', True, rgb['BLACK'])
        score_text_rect = score_text.get_rect()
        score = font.render(str(self.shoot_count), True, rgb['BLACK'])
        score_rect = score.get_rect()
        score_rect.right = screen_width - 5
        score_rect.y = 5
        self.screen.blit(score_text, (screen_width - score_text_rect.width, 5))
        self.screen.blit(score, score_rect)

        self.pygame.display.update()

    def level_up(self):
        if self.LEVEL_UP:
            if self.shoot_count != 20:
                speed_up = pygame.image.load('speedup.png')
                textpos = speed_up.get_rect()
                textpos.center = (screen_width / 2, screen_height / 2)
                self.screen.blit(speed_up, textpos)
            else:
                new_animal = pygame.image.load('newanimal.png')
                textpos = new_animal.get_rect()
                textpos.center = (screen_width / 2, screen_height / 2)
                self.screen.blit(new_animal, textpos)
            pygame.display.update()
            self.leveup_sound.play()
            self.target_list.clear()
            self.previous_count = self.shoot_count
            time.sleep(1)
            self.LEVEL_UP = False
        elif self.previous_count % 10 == 9 and self.shoot_count % 10 == 0:
            self.LEVEL_UP = True
            self.missile_list.clear()

        self.previous_count = self.shoot_count

    def game_over(self):
        pygame.mixer.music.stop()
        font = pygame.font.Font('DungGeunMo.ttf', 50)
        text = font.render('GAME OVER', True, rgb['PINK'])
        textpos = text.get_rect()
        textpos.center = (screen_width/2, screen_height/2)
        self.screen.blit(text, textpos)
        pygame.display.update()
        self.gameover_sound.play()
        time.sleep(4)


# Facade Pattern
class Start:
    def __init__(self):
        self.game = Anipunch()

    def start_anipunch(self):
        self.game.ready()
        self.game.set_display()
        self.game.print_start()
        self.game.game_start()

        speed_observer = SpeedObserver()
        weight_observer = WeightObserver()
        self.game.register_observer(speed_observer)
        self.game.register_observer(weight_observer)

        done = False
        while not done:
            self.game.handle_event()
            self.game.update_user_loc()
            self.game.update_skill()
            self.game.generate_target()
            self.game.del_target_missile()
            self.game.blit()

            self.game.notify_observers()

            # miss >= 3이면 게임 오버
            if self.game.miss_count == 3:
                self.game.game_over()
                done = True

            self.game.level_up()
            self.game.elapsed_time += self.game.clock.tick(60)


# 사용자가 종료키로 종료하기 전까지 무한 반복
while True:
    start = Start()
    start.start_anipunch()
    del start
