from chalice import Chalice, NotFoundError
import boto3, json, os

app = Chalice(app_name='Cloud9')

env = os.environ.get('env')

dynamodb = boto3.client('dynamodb')

@app.route('/')
def index():
    print('Error!')
    raise NotFoundError('Nothing in this path!')

@app.route('/users', methods=['POST'])
def create_user():
    user_as_json = app.current_request.json_body
    response = dynamodb.update_item(TableName=f'users-{env}',
        Key={'UserName': {'S': user_as_json['name']}},
        UpdateExpression='SET UserData=:d',
        ExpressionAttributeValues={':d': {'S': json.dumps(user_as_json)}})
    return {'user': user_as_json}

@app.route('/users/{name}')
def get_user(name):
    response = dynamodb.get_item(TableName=f'users-{env}', Key={'UserName': {'S': name}})
    return {'user': response['Item']}
