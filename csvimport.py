import csv
import mysql.connector
import my_settings

from django.db import connection


db_settings = my_settings.DATABASES
options = db_settings['default'].get('OPTIONS', None)

if options and 'read_default_file' in options:
    db = mysql.connector.connect(read_default_file=options['read_default_file'])
else:
    db_default = db_settings['default']
    db = mysql.connector.connect(host= db_default.get('HOST'),
                         user= db_default.get('USER'),
                         passwd= db_default.get('PASSWORD'),
                         db= db_default.get('NAME'))

cursor = db.cursor()
cursor.execute(f"DELETE FROM heart_time")
cursor.execute(f"DELETE FROM clothes")
cursor.execute(f"DELETE FROM clothes_icon")
cursor.execute(f"DELETE FROM temp_icon")

with open('merge_data.csv') as csv_files:
    reader = csv.DictReader(csv_files)

    for row in reader:
        print(f"row == {row['item_id']}")

        sql = f"""INSERT INTO clothes (
            item_id,
            user_gender,
            img_ref,
            page_ref,
            temp_min,
            temp_max
        ) VALUES (
            %(item_id)s,
            %(user_gender)s,
            %(img_ref)s,
            %(page_ref)s,
            %(temp_min)s,
            %(temp_max)s
        )"""

        cursor.execute(sql, row)

db.commit()

with open('clothes_data_4.csv') as csv_files:
    reader = csv.DictReader(csv_files)

    for row in reader:
        print(f"row == {row['id']}")
        
        sql = f"""INSERT INTO clothes_icon (
            id,
            clothes_des,
            naver_ref
        ) VALUES (
            %(id)s,
            %(clothes_des)s,
            %(naver_link)s
        )"""

        cursor.execute(sql, row)

db.commit()

with open('temp_cat3.csv') as csv_files:
    reader = csv.DictReader(csv_files)

    for row in reader:
        print(",".join(row))
        
        sql = f"""INSERT INTO temperature (
            temp_id,
            temp_min,
            temp_max
        ) VALUES (
            %(temp_id)s,
            %(temp_min)s,
            %(temp_max)s
        )"""

        cursor.execute(sql, row)

db.commit()

with open('mtm.csv') as csv_files:
    reader = csv.DictReader(csv_files)

    for row in reader:
        print(",".join(row))
        
        sql = f"""INSERT INTO temp_icon (
            temp_id,
            icon_id
        ) VALUES (
            %(temperaturecriteria_id)s,
            %(clothesicon_id)s
        )"""

        cursor.execute(sql, row)

db.commit()
db.close()
