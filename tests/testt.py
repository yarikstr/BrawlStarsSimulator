from flask import Flask, render_template, redirect
app = Flask(__name__)


class Test:

    def __init__(self, nickname):
        self.nickname = nickname

    def kdpfew(self):
        self.nickname = 'lol'

    def fdfkwp(self):
        print(self.nickname)


player = Test('kek')
player.kdpfew()
player.fdfkwp()
