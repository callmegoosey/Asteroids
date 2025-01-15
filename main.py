
from engine import Engine

def main():
    engine = Engine()
    try:
        engine.game_loop()
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()