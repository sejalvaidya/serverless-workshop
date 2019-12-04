import json
import stripe
stripe.api_key = os.environ.get('STRIPE_TOKEN')

#json = jwt.decode(json.load(app.current_request.raw_body), os.environ.get('JWT_SECRET'), algorithms=['HS256'])
#decodeAmount = json['amount']
#decodeToken = json['token']

def handler(event, context):
	print('createCharge');
	print(event);
	requestBody = json.loads(event['body'])
	print(requestBody);

	#token = requestBody['token']['id'];
	#amount = requestBody['charge']['amount'];
	#currency = requestBody['charge']['currency'];
	'''
	charge = stripe.Charge.create(
		amount=amount,
		currency=currency,
		description="Serverless Stripe Test charge",
		source=token
	)
	'''
	charge = 
	if charge:
		response = {
		        "statusCode": 200,	# success

		        headers: {
		          'Access-Control-Allow-Origin': '*',
		        },
		        "body": json.dumps({
		          message: `Charge processed succesfully!`,
		          charge
		        })
		    }
	else:
		response = {
		        "statusCode": 500,	# failure

		        headers: {
		          'Access-Control-Allow-Origin': '*',
		        },
		        "body": json.dumps({
		          error: err.message,
		        })
		    }

    return response