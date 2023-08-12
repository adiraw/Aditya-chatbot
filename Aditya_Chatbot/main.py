from chat.dialogues import chat_conversation
from chat.connection import connection as mp_func


def main():
    chat_conversation.greeting()
    while True:
        data = input(f'Aditya: ')
        mp_func(data)
    

if __name__ == "__main__":
    main()