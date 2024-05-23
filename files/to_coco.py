class ToCOCO:
    def __init__(self, path, export_dir, sub_folders):
        import os
        self._path = path
        self._export_dir = export_dir
        self._sub_folders = sub_folders

    def transform_json(self):
        import os
        from labelme2coco import get_coco_from_labelme_folder, save_json
        for sub_folder in self._sub_folders:
            sub_path = str(os.path.join(self._path, sub_folder))
            export_dir = os.path.join(self._export_dir, f"output/{sub_folder}")
            coco = get_coco_from_labelme_folder(sub_path)
            save_json(coco.json, f"{export_dir}/instances_{sub_folder}2017.json")

