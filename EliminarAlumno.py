import boto3  # import Boto3
from boto3.dynamodb.conditions import Key  # import Boto3 conditions

# eliminar alumno
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
    
    if response['Count'] == 0:
        return {
            'statusCode': 404,
            'message': 'Alumno no encontrado'
        }

    # Eliminar el alumno
    table.delete_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'message': 'Alumno eliminado exitosamente'
    }
