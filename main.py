from pathlib import Path
import lesson_7.seminar as sem
import lesson_7.homework as hw

if __name__ == '__main__':
    # sem.fill_int_float('data_num.txt', 15)
    # sem.gen_names('data_names.txt')
    # sem.gen_files('dat', files_count=6)
    # sem.gen_files_with_mul_ext({'txt': 2, 'xml': 4})
    dir = Path.cwd() / 'tmp'
    sem.gen_files_to_dir({'txt': 2, 'xml': 4, 'jpg': 2,
                         'ogg': 3, 'wav': 2, 'bmp': 4}, target_dir=dir)
    sem.group_files_by_ext(dir)
    hw.group_rename('xmlx', 'xml', (0, 5), 2, dir, pref_name='new')
