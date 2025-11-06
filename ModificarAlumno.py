import boto3

def lambda_handler(event, context):
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']

    nuevo_nombre = event['body'].get('nombre')
    nueva_edad = event['body'].get('edad')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    update_expression = []
    expression_values = {}

    if nuevo_nombre:
        update_expression.append("nombre = :n")
        expression_values[":n"] = nuevo_nombre
    if nueva_edad:
        update_expression.append("edad = :e")
        expression_values[":e"] = nueva_edad

    if not update_expression:
        return {
            'statusCode': 400,
            'message': "No se proporcionaron campos para actualizar."
        }

    update_expression_str = "SET " + ", ".join(update_expression)

    response = table.update_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        UpdateExpression=update_expression_str,
        ExpressionAttributeValues=expression_values,
        ReturnValues="ALL_NEW"  # Devuelve el ítem actualizado
    )

    return {
        'statusCode': 200,
        'message': f"Alumno {alumno_id} actualizado correctamente.",
        'alumno_actualizado': response['Attributes']
    }
