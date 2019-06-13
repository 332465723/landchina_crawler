# -*- coding: utf-8 -*-

def concat(f1_path, f2_path):
    with open(f1_path, 'r') as fp:
        f1_lines = []
        for line in fp.readlines():
            info_arr = line.strip().split('|')
            f1_lines.append((info_arr[0]+info_arr[6], info_arr))

    f1_padding = ['' for i in info_arr]

    with open(f2_path, 'r') as fp:
        f2_lines = []
        for line in  fp.readlines():
            info_arr = line.strip().split('|')
            f2_lines.append((info_arr[0]+info_arr[2], info_arr))

    f2_padding = ['' for i in info_arr]

    header_line = []
    header_line.extend(f1_lines[0][1])
    header_line.extend(f2_lines[0][1])

    key1_set = set([f1_lines[i][0] for i in range(1,len(f1_lines))])
    key2_set = set([f2_lines[i][0] for i in range(1,len(f2_lines))])

    interset = key1_set & key2_set
    print interset
    unionset = key1_set | key2_set
    print unionset

    output_lines = []
    output_lines.append(header_line)

    for key in unionset:
        tmp_lines = []
        if key in interset:
            for obj in f1_lines:
                if key == obj[0]:
                    tmp_lines.extend(obj[1])
                    break
            for obj in f2_lines:
                if key == obj[0]:
                    tmp_lines.extend(obj[1])
                    break
        elif key in key1_set:
            for obj in f1_lines:
                if key == obj[0]:
                    tmp_lines.extend(obj[1])
                    break
            tmp_lines.extend(f2_padding)
        elif key in key2_set:
            tmp_lines.extend(f1_padding)
            for obj in f2_lines:
                if key == obj[0]:
                    tmp_lines.extend(obj[1])
                    break
        else:
            print 'error key found:', key

        output_lines.append(tmp_lines)

    with open('./output/concat_output.txt', 'w') as fp:
        for line in output_lines:
            fp.write('|'.join(line) + '\n')

if __name__ == '__main__':
    f1_path = './input/churang_output.txt'
    f2_path = './input/jieguo_output.txt'
    concat(f1_path, f2_path)
