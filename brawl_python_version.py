import time
import random


players = {'Mystic_Yarik': {'coins': '∞', 'brawlers': ['Shelly']}}


class BrawlStars:

    def __init__(self, nickname=None):
        if nickname in players.keys():
            print('Logged in!\n')
            self.nickname = nickname
            brawlers_rare = ['Poco', 'El Primo', 'Barley', 'Rosa']
            brawlers_super_rare = ['Carl', 'Penny', 'Derryl', 'Jacky', 'Rico']
            brawlers_epic = ['Pam', 'Bibi', 'Frank', 'Bea', 'Nani']
            brawlers_mythic = ['Mortis', 'Sprout', 'Gene', 'Tara', 'Mr.P', 'Max']
            brawlers_legendary = ['Crow', 'Leon', 'Spike', 'Sandy']
            brawlers_chromatic = ['Surge', 'Gale']
            self.rares = brawlers_rare
            self.sp_rares = brawlers_super_rare
            self.epics = brawlers_epic
            self.mythics = brawlers_mythic
            self.legendaries = brawlers_legendary
            self.chroma = brawlers_chromatic
        else:
            print('Seems, like you dont have a BrawlStars account yet! Create one and then come back!')
            exit(1)

    def stop(self):
        print('You cannot open boxes anymore, because you have all Brawlers!')
        return True

    def get_brawlers(self):
        acc = players[self.nickname]
        brawlers = acc['brawlers']
        len_brawlers = len(brawlers)
        for i in brawlers:
            if i in self.rares:
                self.rares.remove(i)
            if i in self.sp_rares:
                self.sp_rares.remove(i)
            if i in self.epics:
                self.epics.remove(i)
            if i in self.mythics:
                self.mythics.remove(i)
            if i in self.legendaries:
                self.legendaries.remove(i)
            if i in self.chroma:
                self.chroma.remove(i)
        brawler_chance = ['Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Nothing!', 'Nothing!', 'Nothing!', 'Nothing!',
                          'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                          'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                          'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                          'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                          'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                          'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!', 'Rare!',
                          'Rare!', 'Rare!',
                          'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                          'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                          'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                          'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                          'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                          'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                          'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!', 'SuperRare!',
                          'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!',
                          'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!', 'Epic!',
                          'Epic!', 'Epic!', 'Epic!', 'Epic!',
                          'Mythic!', 'Mythic!', 'Mythic!', 'Mythic!', 'Mythic!', 'Mythic!', 'Mythic!',
                          'Mythic!', 'Mythic!', 'Mythic!',
                          'Legendary!', 'Legendary!',
                          'Chromatic!', 'Chromatic!']
        '''nothing = brawler_chance.count('Nothing!')
        epic = brawler_chance.count('Epic!')
        mythic = brawler_chance.count('Mythic!')
        rare = brawler_chance.count('Rare!')
        sp_rare = brawler_chance.count('SuperRare!')
        print(f'nothing {nothing}')
        print(f'epic {epic}')
        print(f'mythic {mythic}')
        print(f'rare {rare}')
        print(f'sp_rare {sp_rare}\n')'''
        print('\nOpening.')
        time.sleep(0.5)
        print('\nOpening..')
        time.sleep(0.5)
        print('\nOpening...')
        time.sleep(0.5)
        brawler_got = random.choice(brawler_chance)
        print('\nAnd you got.......')
        time.sleep(2)
        if len_brawlers == 27:
            self.stop()

        elif brawler_got == 'Nothing!':
            print('Nothing! Better luck next time!')
            print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')
            time.sleep(1)
            # self.get_brawlers()
            while True:
                answ = input('\nWould you like to continue opening boxes? Y/N')

                if answ.upper() == 'Y':
                    print('\nok!')
                    self.get_brawlers()
                    break
                if answ.upper() == 'N':
                    print('\nok!')
                    time.sleep(1)
                    break
                else:
                    print('Please, print properly.')
        elif brawler_got == 'Rare!':
            if self.rares == []:
                print('Nothing! Better luck next time!')
                print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')
                while True:
                    answ = input('\nWould you like to continue opening boxes? Y/N')

                    if answ.upper() == 'Y':
                        print('\nok!')
                        self.get_brawlers()
                        break
                    if answ.upper() == 'N':
                        print('\nok!')
                        time.sleep(1)
                        break
                    else:
                        print('Please, print properly.')

            else:
                brawler_name = random.choice(self.rares)
                acc['brawlers'].append(brawler_name + str(f' {len_brawlers}'))
                len_brawlers += 1
                self.rares.remove(brawler_name)
                # self.acc['brawlers'].append(brawler_name)
                print(f'{brawler_name}!(Rare) Congrats!\n')
                print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')
                while True:
                    answ = input('\nWould you like to continue opening boxes? Y/N')

                    if answ.upper() == 'Y':
                        print('\nok!')
                        self.get_brawlers()
                        break
                    if answ.upper() == 'N':
                        print('\nok!')
                        time.sleep(1)
                        break
                    else:
                        print('Please, print properly.')
        elif brawler_got == 'SuperRare!':
            if self.sp_rares == []:
                print('Nothing! Better luck next time!')
                print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')

                while True:
                    answ = input('\nWould you like to continue opening boxes? Y/N')

                    if answ.upper() == 'Y':
                        print('\nok!')
                        self.get_brawlers()
                        break
                    if answ.upper() == 'N':
                        print('\nok!')
                        time.sleep(1)
                        break
                    else:
                        print('Please, print properly.')
            else:
                brawler_name = random.choice(self.sp_rares)
                acc['brawlers'].append(brawler_name + str(f' {len_brawlers}'))
                len_brawlers += 1
                self.sp_rares.remove(brawler_name)
                print(f'{brawler_name}!(SuperRare) Congrats!\n')
                print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')
                while True:
                    answ = input('\nWould you like to continue opening boxes? Y/N')

                    if answ.upper() == 'Y':
                        print('\nok!')
                        self.get_brawlers()
                        break
                    if answ.upper() == 'N':
                        print('\nok!')
                        time.sleep(1)
                        break
                    else:
                        print('Please, print properly.')
        elif brawler_got == 'Epic!':
            if self.epics == []:
                print('Nothing! Better luck next time!')
                print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')

                while True:
                    answ = input('\nWould you like to continue opening boxes? Y/N')

                    if answ.upper() == 'Y':
                        print('\nok!')
                        self.get_brawlers()
                        break
                    if answ.upper() == 'N':
                        print('\nok!')
                        time.sleep(1)
                        break
                    else:
                        print('Please, print properly.')
            else:
                brawler_name = random.choice(self.epics)
                acc['brawlers'].append(brawler_name + str(f' {len_brawlers}'))
                len_brawlers += 1
                self.epics.remove(brawler_name)
                print(f'{brawler_name}!(Epic) Congrats!\n')
                print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')
                while True:
                    answ = input('\nWould you like to continue opening boxes? Y/N')

                    if answ.upper() == 'Y':
                        print('\nok!')
                        self.get_brawlers()
                        break
                    if answ.upper() == 'N':
                        print('\nok!')
                        time.sleep(1)
                        break
                    else:
                        print('Please, print properly.')
        elif brawler_got == 'Mythic!':
            if self.mythics == []:
                print('Nothing! Better luck next time!')
                print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')
                while True:
                    answ = input('\nWould you like to continue opening boxes? Y/N')

                    if answ.upper() == 'Y':
                        print('\nok!')
                        self.get_brawlers()
                        break
                    if answ.upper() == 'N':
                        print('\nok!')
                        time.sleep(1)
                        break
                    else:
                        print('Please, print properly.')
            else:
                brawler_name = random.choice(self.mythics)
                acc['brawlers'].append(brawler_name + str(f' {len_brawlers}'))
                len_brawlers += 1
                self.mythics.remove(brawler_name)
                print(f'{brawler_name}!(Mythic) Congrats!\n')
                print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')
                while True:
                    answ = input('\nWould you like to continue opening boxes? Y/N')

                    if answ.upper() == 'Y':
                        print('\nok!')
                        self.get_brawlers()
                        break
                    if answ.upper() == 'N':
                        print('\nok!')
                        time.sleep(1)
                        break
                    else:
                        print('Please, print properly.')
        elif brawler_got == 'Legendary!':
            if self.legendaries == []:
                print('Nothing! Better luck next time!')
                print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')

                while True:
                    answ = input('\nWould you like to continue opening boxes? Y/N')

                    if answ.upper() == 'Y':
                        print('\nok!')
                        self.get_brawlers()
                        break
                    if answ.upper() == 'N':
                        print('\nok!')
                        time.sleep(1)
                        break
                    else:
                        print('Please, print properly.')
            else:
                brawler_name = random.choice(self.legendaries)
                acc['brawlers'].append(brawler_name + str(f' {len_brawlers}'))
                len_brawlers += 1
                self.legendaries.remove(brawler_name)
                print(f'{brawler_name}!(Legendary) Congrats!\n')
                print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')
                while True:
                    answ = input('\nWould you like to continue opening boxes? Y/N')

                    if answ.upper() == 'Y':
                        print('\nok!')
                        self.get_brawlers()
                        break
                    if answ.upper() == 'N':
                        print('\nok!')
                        time.sleep(1)
                        break
                    else:
                        print('Please, print properly.')
        elif brawler_got == 'Chromatic!':
            if self.chroma == []:
                print('Nothing! Better luck next time!')
                print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')

                while True:
                    answ = input('\nWould you like to continue opening boxes? Y/N')

                    if answ.upper() == 'Y':
                        print('\nok!')
                        self.get_brawlers()
                        break
                    if answ.upper() == 'N':
                        print('\nok!')
                        time.sleep(1)
                        break
                    else:
                        print('Please, print properly.')
            else:
                brawler_name = random.choice(self.chroma)
                acc['brawlers'].append(brawler_name + str(f' {len_brawlers}'))
                len_brawlers += 1
                self.chroma.remove(brawler_name)
                print(f'{brawler_name}!(Chromatic) Congrats!\n')
                print(f'Your Brawlers: {brawlers} ({len_brawlers}/27)\n')

                while True:
                    answ = input('\nWould you like to continue opening boxes? Y/N')

                    if answ.upper() == 'Y':
                        print('\nok!')
                        self.get_brawlers()
                        break
                    if answ.upper() == 'N':
                        print('\nok!')
                        time.sleep(1)
                        break
                    else:
                        print('Please, print properly.')


brawler = BrawlStars('Mystic_Yarik')
brawler.get_brawlers()
