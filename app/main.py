from dotenv import load_dotenv
from modules.get_action import ActionsEnum, get_actions


def main():
    a_repo, b_repo, action = get_actions()
    if action == ActionsEnum:
        a_repo.move_to(b_repo)
    elif action == ActionsEnum.COPY_TO:
        a_repo.copy_to(b_repo)


if __name__ == '__main__':
    load_dotenv()
    main()
