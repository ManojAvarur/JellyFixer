import os
import os.path as os_path
from delete_imgs import DeleteImages

DEFAULT_CONFIGS_LOC: str = os_path.join(os_path.dirname(os_path.abspath(__file__)), 'configs')

def scan(path: str, *args):
    for file in os.listdir(path=path):
        file_loc: str = f"{path}/{file}"

        if os_path.isdir(file_loc):
            scan(file_loc, *args)

        for arg in args:
            arg.process(file_loc)


if __name__ == '__main__':
    delete_imgs = DeleteImages(f"{DEFAULT_CONFIGS_LOC}/delete_config.json")

    scan(os.getcwd(), delete_imgs)

    delete_imgs.close()
