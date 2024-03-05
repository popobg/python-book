"""Parse and rename the files of a given directory.
Original format: "{name} - {number}.ext"
Willing format: "{number}-{name}.ext"
"""

import os

class RenameFiles:

    def __init__(self, path_dir: str, separator: str = "-"):
        self.path_dir = path_dir
        self.separator = separator
        os.chdir(self.path_dir)

    @classmethod
    def change_name_file(cls, path_file: str, separator: str = "-"):
        cls = cls(path_file, separator)
        for file in os.listdir():
            list_file_name, file_extension = cls._parse_name(file, separator)
            new_name = cls._new_name(list_file_name, file_extension)
            print(new_name)
            os.rename(file, new_name)

    @classmethod
    def _parse_name(cls, file: str, separator: str) -> tuple[list[str], str]:
        """parse the name file and extract name, number and extension"""
        # split the string into name and extension
        file_name, file_ext = os.path.splitext(file)
        list_file_name = file_name.strip().split(separator)

        for i, name in enumerate(list_file_name):
            name = name.strip()
            list_file_name[i] = name

        return list_file_name, file_ext

    @staticmethod
    def _new_name(list: list[str], extension:str) -> str:
        """return the format number_name.ext"""
        number = "".join(["" + char for char in list[-1] if char.isdigit()])

        # if len(list) > 2:
        #     name = "-".join(list[:-1])
        # else:
        #     name = list[0]

        return f"{number}- {list[0]}{extension}"


if __name__ == "__main__":
    path_file = os.path.join(os.getcwd(), "example_folder")
    dir_to_rename = RenameFiles.change_name_file(path_file, "-")