You can actually access most of the urls in a web browser as well. There is a nice web-format provided.

1) API 

To be able to execute http you must install httpie with command: "pip install httpie" . 


http --json POST 127.0.0.1:8000/api-token-auth/ username=“mauno“ password=“foobarfoo“
Add Pictures with token
http -f POST http://127.0.0.1:8000/uusapp/addimage/ title="peeter" image@~\test.jpg "Authorization: Token b85bd5705373081b09bcc59a20d97052cbc566fa" -v
Register user
http --json POST http://127.0.0.1:8000/uusapp/register/ username="sinuema" password=“foobarfoo“ -v
Get pictures through security check 
http --json GET 127.0.0.1:8000/uusapp/getimage/?id="3" "Authorization: Token b85bd5705373081b09bcc59a20d97052cbc566fa" -v
Get url - if the checurity check doesnt work out
http --json GET 127.0.0.1:8000/uusapp/getimageurl/?id="3" "Authorization: Token b85bd5705373081b09bcc59a20d97052cbc566fa" -v
GetGroupImages 
http --json GET 127.0.0.1:8000/uusapp/groupimages/?id="3" "Authorization: Token b85bd5705373081b09bcc59a20d97052cbc566fa" -v
GetUserGroups
http --json GET 127.0.0.1:8000/uusapp/usergroups/ "Authorization: Token b85bd5705373081b09bcc59a20d97052cbc566fa" -v
AddUserGroup for current user 
http --json POST 127.0.0.1:8000/uusapp/usergroups/ title="Test" duration="10"  "Authorization: Token b85bd5705373081b09bcc59a20d97052cbc566fa" -v


2) to run the django project against what to test you api  you need: 

coreapi==2.1.1
Django==1.10.3
djangorestframework==3.5.3
itypes==1.1.0
Pillow==3.4.2
psycopg2==2.6.2
requests==2.12.3
uritemplate==3.0.0

also, as psql server. But you can set the project up with sql-lite. In that case you need to set it up with different parameters. 
Currently the code in settings.py ... The "linux" check is there for the cases when i deploy the code to aws.
if(sys.platform == "linux"):
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': "ebdb",
			'USER': "administraator",
			'PASSWORD': "kalsssds",
			'HOST': "aaghowdt333l1r.cbfuxup0zpv7.us-west-2.rds.amazonaws.com",
			'PORT': 5432,
		}
	}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'uus',
            'USER': 'admin',
            'PASSWORD': 'Nossuonbeebi92',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }	



