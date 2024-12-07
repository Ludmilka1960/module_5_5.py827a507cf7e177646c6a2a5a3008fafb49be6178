
import time



class User:

    def __init__(self,nickname,password,age,):
        self.nickname = nickname
        self.password = hash(password)
        self.age =  age

    def __str__(self):
        return self.nickname
        # f'User(Имя: {self.nickname},возраст: {self.age})'
    def __eq__(self, other):
        return other.nickname == self.nickname

    def __get__info(self):
        return self.nickname,self.password

class Video:

    def  __init__(self,title,duration,adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

class UrTube:


    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self,login,password):
        for user in self.users:
            if (login,hash(password)) == user_get_info():
                self.current_user = user
            return user

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print('Пользователь уже существует ')

    def log_out(self):
         self.current_user = None

    def add(self,* videos:Video):
        for video in videos:
            if video not in self.videos:
                print('Неверный никнейм или пароль')
                self.videos.append(video)


    def get_videos(self,search):
        titles = []
        for video in self.videos:
            if search.lower() in str(video).lower():
                titles.append(video)
            print(f'Ничего не найдено')
        return titles



    def watch_video(self,title):
        if self.current_user is None:
            print('Войдите в аккаунт для просмотра видео')
            return
        for video in self.videos:
            if title == 'video.title':
                if video.adult_mode and self.current_user.age >= 18:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now,end='')
                        time.sleep(1)
                    video.time_now = 0
                    print('Конец видео.')
                else:
                    print('Вам нет 18 лет.Вы не можете просматривать видео')
                    break

ur=UrTube()
user1 = User('Lisa',3233,'19')
user2 = User('Volk',8978,'12')
print(user1)
print(user2)
video1 = Video('Приколы нашего UU',23)
video2 = Video('Позитив и юмор-наше кредо',30,adult_mode=True)
print(video1)
print(video2)
#добавление видео
ur.add(video1,video2)
#проверка поиска
print(ur.get_videos('пРик'))
print(ur.get_videos('кред'))
#проверка на вход и возраст
ur.watch_video('Позитив и юмор-наше кредо')
ur.register('Volk',8978,12)
ur.watch_video('Позитив и юмор-наше кредо')
#проверка входа в другой аккаунт
ur.register('Klest',648,12)
print(ur.current_user)
#попытка воспроизведения несуществующего видео
ur.watch_video("Был бы повод")









