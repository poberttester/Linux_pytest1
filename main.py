import subprocess
import pytest


class Command():
    def func(linux_command: str) -> object:
        """
        Функция принемает на вход команду Linux и возвращает к поток данных.
        """
        result = subprocess.run(linux_command, shell=True, stdout=subprocess.PIPE,
                                encoding='utf-8')
        return result.stdout


def test_command_is_work():
    assert Command.func('cat /home/b/Educational_materials/Auto_test_Python_for_Linux/seminars/file1.txt') == 'Homework №1'


if __name__ == '__main__':
    pytest.main(['-v'])

