import requests
import json
import csv


class DataRetrive:
    def __init__(self):
        pass

    def dataGet(self):
        response = requests.get("https://hpb.health.gov.lk/api/get-current-statistical")
        data = response.json()
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def jsonToCsv(self):
        with open('data.json') as f:
            json_data = json.load(f)

        daily_pcr = json_data['data']['daily_pcr_testing_data']
        csv_columns = ['date', 'count']

        with open('daily_pcr.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in daily_pcr:
                writer.writerow(data)

        hospital_data = json_data['data']['hospital_data']
        csv_columns = ['id', 'hospital_id', 'cumulative_local', 'cumulative_foreign', 'treatment_local',
                       'treatment_foreign', 'created_at', 'updated_at', 'deleted_at', 'cumulative_total',
                       'treatment_total', 'hospital']

        with open('hospital_data.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in hospital_data:
                writer.writerow(data)


if __name__ == '__main__':
    dr = DataRetrive()
    dr.dataGet()
    dr.jsonToCsv()
