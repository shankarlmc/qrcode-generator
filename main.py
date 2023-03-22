import csv
from segno import helpers

destination = ''

with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_num = 0
    for row in csv_reader:
        if line_num == 0:
            print(f'Column names are {", ".join(row)}')
            line_num += 1

        qr_code_name = row['full_name'].replace(" ", "-") + '.png'

        destination = 'result/' + qr_code_name

        qrcode = helpers.make_vcard(
            name=row["full_name"], displayname=row["full_name"],
            nickname=row["id_num"],
            phone=row["contact_num"],
            email=row["email"],
        )
        print('Creating QR Code for ' + row['full_name'] + '...')
        qrcode.save(destination, scale=4)
        line_num += 1

print(f'Processed {line_num} lines.')
