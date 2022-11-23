import os
from pathlib import Path
from openpyxl import load_workbook
import xlwt

work_dir = r"C:\Users\gilyazev\PycharmProjects\store\upload\Электросамокаты"
serianame =[]


# Initialize a workbook
book = xlwt.Workbook()

# Add a sheet to the workbook

sheet1 = book.add_sheet("Sheet1")


img_types = ('*.jpg', '*.png')
index = 0
for pathname in os.listdir(work_dir):
    serianame.append(pathname)
    next_dir = work_dir + "\\" +pathname
    #index +=1
    for path in os.listdir(next_dir):
        #product_name.append(path)
        index +=1
        row = sheet1.row(index)
        tmp= path.split(" ")
        if len(tmp) > 2:
            tmp2 = tmp[1] + " " + tmp[2]
        else:
            tmp2 = tmp[1]
        row.write(0, path)
        row.write(1, tmp2)
        target_path = next_dir + "\\" + path
        ind =6
        for type in img_types:
            pathlist = Path(target_path).glob(type)
            for pat in pathlist:

                img = str(pat).replace('\\', '|').split('|')[-1]
                path_img = pathname + "\\" + path + "\\" + img

                ind += 1
                row.write(ind ,path_img)
        txt_files = Path(target_path).glob('*.txt')
        col_id = 1
        for txt_file in txt_files:
            col_id +=1
            f = open(txt_file, 'r').readline()
            f.replace('\n', '|||')
            row.write(col_id, f)

book.save("spreadsheet.xls")





