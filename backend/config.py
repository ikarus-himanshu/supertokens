from supertokens_python.recipe.thirdpartyemailpassword import Google, Github, Apple
from supertokens_python import SupertokensConfig
from supertokens_python.recipe import thirdpartyemailpassword, session
from supertokens_python.recipe import dashboard
from supertokens_python.recipe import emailverification
from supertokens_python.recipe import thirdpartyemailpassword, session
from supertokens_python.recipe.emailpassword import InputFormField
from supertokens_python.recipe.thirdpartyemailpassword.interfaces import APIInterface, EmailPasswordAPIOptions, EmailPasswordSignUpPostOkResult
from typing import List, Dict, Any
from supertokens_python.recipe.emailpassword.types import FormField
from supertokens_python.recipe import usermetadata


def override_apis(original_implementation: APIInterface): 
    original_emailpassword_sign_up_post = original_implementation.emailpassword_sign_up_post
    async def emailpassword_sign_up_post(form_fields: List[FormField],
                                         api_options: EmailPasswordAPIOptions, user_context: Dict[str, Any]):
        # First we call the original implementation of sign_up_post
        response = await original_emailpassword_sign_up_post(form_fields, api_options, user_context)

        # Post sign up response, we check if it was successful
        if isinstance(response, EmailPasswordSignUpPostOkResult):
            if response.user is None:
                raise Exception("Should never come here")
            _ = response.user.user_id
            __ = response.user.email

            # TODO: use the input form fields values for custom logic
        return response
    original_implementation.emailpassword_sign_up_post = emailpassword_sign_up_post
    return original_implementation

supertokens_config=supertokens_config=SupertokensConfig(
        # These are the connection details of the app you created on supertokens.com
        connection_uri='http://localhost:3567',
        api_key="BM29seIwT0gOhdYl=6uR4N=mNBKO1H"
    )


providers=[
        # We have provided you with development keys which you can use for testing.
        # IMPORTANT: Please replace them with your own OAuth keys for production use.
        Google(
            client_id='1060725074195-kmeum4crr01uirfl2op9kd5acmi9jutn.apps.googleusercontent.com',
            client_secret='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'
        # ), Facebook(
        #     client_id='FACEBOOK_CLIENT_ID',
        #     client_secret='FACEBOOK_CLIENT_SECRET'
        ), Github(
            client_id='467101b197249757c71f',
            client_secret='e97051221f4b6426e8fe8d51486396703012f5bd'
        ),
        Apple(
            client_id="4398792-io.supertokens.example.service",
            client_key_id="7M48Y4RYDL",
            client_private_key="-----BEGIN PRIVATE KEY-----\nMIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgu8gXs+XYkqXD6Ala9Sf/iJXzhbwcoG5dMh1OonpdJUmgCgYIKoZIzj0DAQehRANCAASfrvlFbFCYqn3I2zeknYXLwtH30JuOKestDbSfZYxZNMqhF/OzdZFTV0zc5u5s3eN+oCWbnvl0hM+9IW0UlkdA\n-----END PRIVATE KEY-----",
            client_team_id="YWQCXGJRJL"
        )
    ]

sign_up_feature=thirdpartyemailpassword.InputSignUpFeature(
                form_fields=[InputFormField(id='name'), InputFormField(id='age'), InputFormField(id='country', optional=True)]
            )

override=thirdpartyemailpassword.InputOverrideConfig(
                apis=override_apis
            )

recipe_list=[
        emailverification.init(mode='REQUIRED'),
        session.init(), # initializes session features
        thirdpartyemailpassword.init(providers=providers,sign_up_feature=sign_up_feature,override=override),
        dashboard.init(api_key="supertokens"),
        usermetadata.init()
        
    ]


def override_apis(original_implementation: APIInterface): 
    original_emailpassword_sign_up_post = original_implementation.emailpassword_sign_up_post
    async def emailpassword_sign_up_post(form_fields: List[FormField],
                                         api_options: EmailPasswordAPIOptions, user_context: Dict[str, Any]):
        # First we call the original implementation of sign_up_post
        response = await original_emailpassword_sign_up_post(form_fields, api_options, user_context)

        # Post sign up response, we check if it was successful
        if isinstance(response, EmailPasswordSignUpPostOkResult):
            if response.user is None:
                raise Exception("Should never come here")
            _ = response.user.user_id
            __ = response.user.email

            # TODO: use the input form fields values for custom logic
        return response
    original_implementation.emailpassword_sign_up_post = emailpassword_sign_up_post
    return original_implementation