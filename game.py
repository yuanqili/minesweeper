from gamedriver import GameDriver

if __name__ == '__main__':
    driver = GameDriver()
    while not driver.finished():
        driver.next()
