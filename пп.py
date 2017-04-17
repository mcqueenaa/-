Хождение по папкам

for root, dirs, files in os.walk('.'):
    print(root, dirs)

путь к файлу чтобы его открыть
os.path.join(root, fname)

file_tree = os.walk('.')
for d in file_tree:
    print(d)

for root, dirs, files in os.walk('.'):
    print(root) - идем в по папкам, если в одной из папок есть еще папки - сначала идем вглубь, затем к следующим папкам
можно идти снизу вверх
for root, dirs, files in os.walk('.', topdown=False):
    print(root)

смотрим файлы

