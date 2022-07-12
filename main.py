import argparse
from image_segmentation import get_scores_and_plot

def parse_argument():
    parser = argparse.ArgumentParser(description='Get GVI, SVF, BVF scores')
    parser.add_argument('-i', '--input', type=str, required=True,
                        help='Complete path and filename for the input image.')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_argument()
    if args.input:
        get_scores_and_plot(img=args.input)
