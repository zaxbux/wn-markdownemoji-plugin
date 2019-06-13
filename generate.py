import json
import os.path
import urllib.request


def get_categorized(data):
    categorized = {}

    for emoji in data:
        category = emoji['category']
        if not category in categorized:
            categorized[category] = []
        categorized[category].append(emoji)
    return categorized


def main():
    if not os.path.isfile('emoji.json'):
        confirm = input('emoji.json does not exist! Download? [Y/n]: ')

        if confirm.lower() != 'n':
            print("Downloading...")
            urllib.request.urlretrieve('https://raw.githubusercontent.com/iamcal/emoji-data/master/emoji.json', 'emoji.json')
        else:
            print("Exiting...")
            exit()

    with open('emoji.json', 'r') as fp:
        print('Parsing JSON...')
        data = json.load(fp)

    with open('emoji.php', 'w') as fp:
        print('Writing "emoji.php"...')
        fp.write("<?php\n\n$emojiUnicode = [")

        for emoji in data:
            fp.write("\n\t'{}' => '{}',".format(emoji['short_name'], emoji['unified']))
        fp.write("\n];\n")

    with open('emoji.md', 'w') as fp:
        print('Writing "emoji.md"...')
        categorized = get_categorized(data)

        for category, items in categorized.items():
            fp.write('| {} | {} | {} |\n| --- | --- | --- |\n'.format(category, category, category))

            max_count = len(items)

            for i in range(0, max_count, 3):
                for j in range(i, i+3):
                    if j < max_count:
                        sn = items[j]['short_name']
                        fp.write('| `:{}:` '.format(sn))
                    else:
                        fp.write('| ')
                fp.write('|\n')
            fp.write('\n\n')
    print('Done!')


if __name__ == "__main__":
    main()
