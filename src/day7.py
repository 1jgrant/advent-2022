test_input = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

with open('src/inputs/day7_input.txt', 'r', encoding='utf-8') as text:
    actual_input = text.read()
puzzle_input = actual_input

terminal_lines = puzzle_input.splitlines()
dir_hash = {}
current_path = ''
current_dir = ''
depth = 0

for line in terminal_lines:
    if line == '$ ls':
        continue
    if line == '$ cd ..':
        current_dirs = current_path.split('/')
        current_dir = current_dirs[-3] if len(current_dirs) > 3 else '/'
        current_path = f'{"/".join(current_dirs[:-2])}/'
        depth -= 1
        continue
    if line.startswith('$ cd'):
        current_dir = line.split(' ')[-1]
        if current_dir == '/':
            current_dir = ''
        current_path += f'{current_dir}/'
        if current_path not in dir_hash:
            dir_hash[current_path] = {'path': current_path,
                                      "subdirs": [],
                                      "depth": depth,
                                      "subdirs_size": 0,
                                      "files_size": 0,
                                      "total_size": 0,
                                      'seen': False}
        depth += 1
        continue
    if line.startswith('dir'):
        [_, subdir] = line.split(' ')
        dir_hash[current_path]['subdirs'].append(f'{current_path}{subdir}/')
        continue
    [file_size, _] = line.split(' ')
    dir_hash[current_path]['files_size'] += int(file_size)

dirs_list = list(dir_hash.values())
depth_sorted_dirs = sorted(dirs_list, key=lambda dir: dir['depth'], reverse=True)

for dir_ref in depth_sorted_dirs:
    target_dir = dir_ref['path']
    for subdir in dir_ref['subdirs']:
        dir_hash[target_dir]['subdirs_size'] += dir_hash[subdir]['files_size'] + dir_hash[subdir]['subdirs_size']
    dir_hash[target_dir]['total_size'] = dir_hash[target_dir]['subdirs_size'] + dir_hash[target_dir]['files_size']

max_size = 100000
under_max = [item['total_size'] for item in dir_hash.values() if item['total_size'] < max_size]
print('part 1:', sum(under_max))

disk_space = 70000000
required_space = 30000000
unused_space = disk_space - dir_hash['/']['total_size']

smallest_option = min([dir['total_size'] for dir in dir_hash.values() if
                      unused_space + dir['total_size'] > required_space])
print('part 2:', smallest_option)
