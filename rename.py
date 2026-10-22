import re
from pathlib import Path

path = 'D:\\Movies\\' + 'sss'


def natural_sort_key(s):
    """مرتب‌سازی طبیعی (1, 2, 10 به جای 1, 10, 2)"""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', str(s))]


def rename_files_in_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print(f"❌ فولدر پیدا نشد: {folder}")
        return

    parent_name = folder.name

    # ---------- فایل‌های مستقیم داخل فولدر اصلی ----------
    files = [f for f in folder.iterdir() if f.is_file()]
    files.sort(key=lambda x: natural_sort_key(x.name))

    print(f"\n📁 فولدر اصلی: {parent_name}")
    print(f"تعداد فایل‌ها: {len(files)}")

    for index, file in enumerate(files, start=1):
        new_name = f"{parent_name}{index:02d}{file.suffix}"
        new_path = folder / new_name

        if file.name == new_name:
            print(f"  ✔️  از قبل درست بود: {file.name}")
            continue

        print(f"  {file.name}  →  {new_name}")
        file.rename(new_path)

    # ---------- زیرپوشه‌ها ----------
    subfolders = [d for d in folder.iterdir() if d.is_dir()]

    for subfolder in subfolders:
        sub_name = subfolder.name
        sub_files = [f for f in subfolder.iterdir() if f.is_file()]
        sub_files.sort(key=lambda x: natural_sort_key(x.name))

        print(f"\n📂 زیرپوشه: {sub_name}")
        print(f"تعداد فایل‌ها: {len(sub_files)}")

        for index, file in enumerate(sub_files, start=1):
            new_name = f"{parent_name}{sub_name}E{index:02d}{file.suffix}"
            new_path = subfolder / new_name

            if file.name == new_name:
                print(f"  ✔️  از قبل درست بود: {file.name}")
                continue

            print(f"  {file.name}  →  {new_name}")
            file.rename(new_path)

    print("\n✅ کار تموم شد!")


rename_files_in_folder(path)
