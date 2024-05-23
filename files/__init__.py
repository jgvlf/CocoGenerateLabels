class AnnotationsFiles:
    def __init__(self, path: str):
        import os
        self._path = path
        self._path = os.path.abspath(self._path)
        self._export_path = os.path.abspath(".")
        self._sub_folders = list()
        self._get_annotation_files()

    def show_path(self):
        print(self._path)

    def _get_annotation_files(self):
        import os
        os.chdir(self._path)
        self._sub_folders = os.listdir(self._path)
        for sub_folder in self._sub_folders:
            sub_path = os.path.join(self._path, sub_folder)
            for file in os.listdir(sub_path):
                if not file.lower().endswith(".json"):
                    file_path = os.path.join(sub_path, file)
                    os.remove(file_path)

    def generate_coco_labels(self):
        from .to_coco import ToCOCO
        generator = ToCOCO(self._path, self._export_path)
        generator.transform_json()
