from abc import ABC, abstractmethod


class Robots(ABC):
    """Базовый абстрактный класс робртов, с него начинается роботостроение"""

    def __init__(self, name, health=1, armor=0, weapon=None, step=1, vision=5, mod=None):
        self.name = name
        self.health = health
        self.armor = armor
        self.weapon = weapon
        self.step = step
        self.vision = vision
        self.mod = mod


class Weapons(ABC):
    """Базовый абстрактный класс оружия, с него начинается стройка оружия"""

    def __init__(self, name, type_w, temp=1, damage=1):
        self.name = name
        self.type_w = type_w
        self.temp = temp
        self.damage = damage

#class Enemies(Robots):
    #"""Класс для врагов"""
    #def __init__(self):