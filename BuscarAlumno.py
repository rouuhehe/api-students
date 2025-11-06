import boto3  # import Boto3
from boto3.dynamodb.conditions import Key  # import Boto3 conditions

# buscar alumno
def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.query(
        KeyConditionExpression=Key('tenant_id').eq(tenant_id) & Key('alumno_id').eq(alumno_id)
    )
    items = response.get('Items', [])
    alumno = items[0] if items else None
    # Salida (json)
    return {
        'statusCode': 200,
        'alumno': alumno
    }