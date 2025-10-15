
class minotauro:
    alive = True
    vel = 1
    detect = False

    #ALIVE
    def set_die(self):#mata o minotauro
        if self._alive == True:
            self._alive = False

    def get_die(self):#olha se está morto
        if self._alive == False:
            return True

    #DETECTAR MODIFICA A VELOCIDADE
    def get_cheiro(self):#verifica se está sentindo cheiro
        return self._detect

    def set_cheiro_true(self):#faz sentir o cheiro
        if self._detect == False:
            self._detect = True
            self._vel = 2

    def set_cheiro_false(self):#faz esquecer o cheiro
        if self._detect == True:
            self._detect = False
            self._vel = 1

    def get_minos_vel(self):
        return self._vel




class entrante():
    alive = True
    vel = 1
    save = False
    food = 0

    #history

    def set_isSafe(self):
        self._save = True

    def set_food(self, marmita):
        self._food = marmita

    def get_food(self):
        return self._food


    #history





minos = minotauro()
teseu = entrante()

print(minos.get_minos_vel())
minos.set_cheiro_true()
print(minos.get_minos_vel())

#print(teseu.)
#print(teseu.)