from files import AnnotationsFiles
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", required=True, type=str)

args = parser.parse_args()

if __name__ == '__main__':
    annotations = AnnotationsFiles(args.path)
    files = annotations.generate_coco_labels()
