import json
import zipfile

PACK_NAME = 'LethalLicks'

if __name__ == '__main__':
    
    with open('manifest.json', 'r') as manifest_file:
        manifest = json.load(manifest_file)

    with open('modlist.txt', 'r') as modlist_file:
        mods = list(map(lambda s: s.strip(), modlist_file.readlines()))

    manifest['dependencies'] = mods

    with zipfile.ZipFile(f'{PACK_NAME}.zip', 'w') as archive:    
        archive.write('README.md')
        archive.writestr('manifest.json', json.dumps(manifest, indent=4))
        archive.write('icon.png')