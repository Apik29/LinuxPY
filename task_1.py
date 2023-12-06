import subprocess


def my_func(cmd, text):
    result = subprocess.run(cmd, shell=True,
                            stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        print('True')
        return True
    else:
        print('False')
        return False


if __name__ == '__main__':
    my_func('ls /', 'lib')