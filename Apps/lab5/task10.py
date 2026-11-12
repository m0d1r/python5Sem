import argparse


def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name, encoding='utf-8-sig') as file:
            lines = file.read().splitlines()
    except (OSError, UnicodeError) as error:
        return str(error)

    if frame_height <= 0 or frame_width <= 0:
        return ''

    result = []
    for line in lines:
        parts = [line[i:i + frame_width] for i in range(0, len(line), frame_width)] or ['']
        for part in parts:
            result.append(part)
            if len(result) == frame_height:
                return '\n'.join(result)
    return '\n'.join(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame-height', type=int, required=True)
    parser.add_argument('--frame-width', type=int, required=True)
    parser.add_argument('file_name')
    args = parser.parse_args()
    print(format_text_block(args.frame_height, args.frame_width, args.file_name))
