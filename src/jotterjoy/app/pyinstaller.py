from glob import glob
from os import path
import PyInstaller.__main__


def get_data_files():
    files = glob("src/jotterjoy/prompts/*.txt")
    result = []
    for d in files:
        data_directory = path.dirname(d)
        import_line = f"--add-data={d}:{data_directory}"
        result.append(import_line)
    return result


def install():
    data = get_data_files()
    params = [
        "./src/jotterjoy/app/main.py",
        "--noconfirm",
        "--onefile",
        "--console",
        "--clean",
        "--name=jotterjoy",
    ]
    params.extend(data)

    PyInstaller.__main__.run(params)


if __name__ == "__main__":
    install()
