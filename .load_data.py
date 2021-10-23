import csv

def load_data(filename):
    with open(filename,'r') as f:
        next(f)
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            client = Client(
                first_name=row[0].strip(),
                last_name=row[1].strip(),
                email=row[2].strip(),
                ip_address=row[3].strip(),
                city=row[4].strip(),
                driving_licence=row[5].strip(),
            )
            client.save()
            print(client)
