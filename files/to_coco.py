class ToCOCO:
    def __init__(self, path, export_dir):
        import os
        self._path = path
        self._export_dir = export_dir

    def transform_json(self):
        import os
        from labelme2coco import convert
        export_dir = os.path.join(self._export_dir, "output/")
        convert(self._path, export_dir)

