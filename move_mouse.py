import pyautogui
import time

# Espera 5 segundos antes de começar para você ter tempo de mudar para a janela que deseja
time.sleep(5)

# Mover o mouse para a posição (x=100, y=100)
pyautogui.moveTo(100, 100, duration=1)  # Move em 1 segundo

# Mover o mouse em relação à posição atual
pyautogui.moveRel(200, 0, duration=1)  # Move 200 pixels para a direita

# Mover o mouse para outra posição
pyautogui.moveTo(300, 300, duration=2)  # Move em 2 segundos