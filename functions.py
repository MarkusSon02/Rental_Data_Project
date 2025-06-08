import boto3
import json
import datetime

def get_current_time() -> str:
    now = datetime.datetime.now()
    str_now = str(now)
    str_now = str_now.split(' ')
    str_now_date = str_now[0]
    str_now_time = str_now[1].split(':')
    str_now_time = str_now_time[0] + '-' + str_now_time[1] + '-' + str_now_time[2].split('.')[0]
    str_now = str_now_date + '_' + str_now_time
    
    str_now_date_split = str_now_date.split('-')
    year = str_now_date_split[0]
    month = str_now_date_split[1]
    
    return str_now, year, month


def upload_data(data: dict, location:str, bucket: str) -> None:
    """
    Uploads JSON data to S3 using a partitioned path:
    s3://<bucket>/raw_data/rental_data/location=<location>/year=YYYY/month=MM/rental_data<location>_<now>.json
    """
    now, year, month = get_current_time()
    
    s3 = boto3.client("s3")

    key = f"raw_data/rental_data/location={location}/year={year}/month={month}/rental_data_{location}_{now}.json"

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(data),
        ContentType="application/json"
    )

    print(f"Uploaded to s3://{bucket}/{key}")


def start_glue_job(location: str) -> None:
    glue = boto3.client('glue', region_name='ap-southeast-2')

    response = glue.start_job_run(
        JobName='process_weather-api-data-son_json_into_parquets',
        Arguments={
            '--location': location
        }
    )
    
    print(f"Started Glue job: {response['JobRunId']}")