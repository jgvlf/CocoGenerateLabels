class FileFoundException(Exception):
    pass

class FoldersPatternException(Exception):
    pass


class AnnotationsFiles:
    def __init__(self, path: str):
        import os
        self._path = path
        self._path = os.path.abspath(self._path)
        self._export_path = os.path.normpath(self._path + os.sep + os.pardir)
        self._sub_folders = list()
        self._get_annotation_files()

    def show_path(self):
        print(self._path)

    def _get_annotation_files(self):
        import os
        folders = ['test', 'train', 'val']
        for sub_folder in os.listdir(self._path):
            if os.path.isfile(os.path.join(self._path, sub_folder)):
                raise FileFoundException(
                    f"The \"{sub_folder}\" is a file present on the folder and this is not allowed. Please, remove this file.")
        if os.listdir(self._path) != folders:
            raise FoldersPatternException(f"On the directory has the following folders: {os.listdir(self._path)} and pattern isn't allowed. The right pattern is: {folders}")
        self._sub_folders = os.listdir(self._path)
        for sub_folder in self._sub_folders:
            if not os.path.exists(f"{self._export_path}/img/{sub_folder}/"):
                os.makedirs(f"{self._export_path}/img/{sub_folder}/")
            sub_path = os.path.join(self._path, sub_folder)
            for file in os.listdir(sub_path):
                if not file.lower().endswith(".json"):
                    file_path = os.path.join(sub_path, file)
                    # abs_img_path = os.path.abspath(f"img/{sub_folder}/")
                    img_path = os.path.join(f"{self._export_path}/img/{sub_folder}/", file)
                    os.replace(file_path, img_path)

    def generate_coco_labels(self):
        from .to_coco import ToCOCO
        generator = ToCOCO(self._path, self._export_path, self._sub_folders)
        generator.transform_json()
