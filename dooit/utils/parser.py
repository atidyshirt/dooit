from typing import Dict
import appdirs
import yaml
from pathlib import Path
from os import mkdir

HOME = Path.home()
XDG_CONFIG = Path(appdirs.user_config_dir("dooit"))
XDG_DATA = Path(appdirs.user_data_dir("dooit"))
PLUGINS = XDG_CONFIG / "plugins"


class Parser:
    """
    Parser class to manage and parse dooit's config and data
    """

    def __init__(self) -> None:
        self.check_files()

    @classmethod
    def save(cls, data):
        """
        Save the todos to data file
        """

        obj = cls()
        with open(obj.todo_yaml, "w") as stream:
            yaml.safe_dump(data, stream, sort_keys=False)

    @classmethod
    def load(cls) -> Dict:
        """
        Retrieves the todos from data file
        """

        obj = cls()
        with open(obj.todo_yaml, "r") as stream:
            data = yaml.safe_load(stream)

        return data

    def check_files(self) -> None:
        """
        Checks if all the files and folders are present
        to avoid any errors
        """

        def check_folder(f: Path):
            if not Path.is_dir(f):
                mkdir(f)

        check_folder(XDG_CONFIG)
        check_folder(PLUGINS)
        check_folder(XDG_DATA)

        self.todo_yaml = XDG_DATA / "todo.yaml"

        if not Path.is_file(self.todo_yaml):
            with open(self.todo_yaml, "w") as f:
                yaml.safe_dump(dict(), f)
