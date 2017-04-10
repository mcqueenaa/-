import os
import shutil

s = input('Введите предложение на англ языке: ')
s_name = s.replace(' ', '\\')
os.makedirs(s_name)
