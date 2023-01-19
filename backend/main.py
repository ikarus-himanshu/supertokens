
import nest_asyncio
nest_asyncio.apply()



from supertokens_python import init, InputAppInfo
import config
from supertokens_python.recipe.thirdpartyemailpassword.asyncio import get_user_by_id

from supertokens_python import get_all_cors_headers
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python.recipe.session.asyncio import get_session
from fastapi.requests import Request

from supertokens_python.recipe.thirdpartyemailpassword.interfaces import EmailPasswordSignInWrongCredentialsError

from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.session import SessionContainer
from fastapi import Depends
from fastapi.responses import PlainTextResponse
from supertokens_python.recipe.thirdpartyemailpassword.syncio import get_user_by_id, emailpassword_sign_in, update_email_or_password
from supertokens_python.recipe.session.syncio import revoke_all_sessions_for_user
import schemas

init(
    app_info=InputAppInfo(
        app_name="Ikarus_Nest",
        api_domain="http://localhost:8000",
        website_domain="http://localhost:3000",
        api_base_path="/auth",
        website_base_path="/auth"
    ),
    supertokens_config=config.supertokens_config,
    framework='fastapi',
    recipe_list=config.recipe_list,
    mode='asgi'   # use wsgi if you are running using gunicorn
    )

app = FastAPI()
app.add_middleware(get_middleware())

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)
@app.get('/') 
async def index(session: SessionContainer = Depends(verify_session())):
    user_id = session.get_user_id()
    info =  get_user_by_id(user_id)
    return f'Welcome! {info.email}'


@app.get('/get_user') 
async def get_user(request: Request):
    session = await get_session(request)
    if session is None:
        raise Exception("User Not Logged In")
    user_id = session.get_user_id()
    print(user_id)
    return user_id

# @app.post('/change_pass')
# async def change_pass(request:schemas.changepassword):
#     session=await get_session(request)
#     user_id = session.get_user_id()
#     users_info = get_user_by_id(user_id)
#     if users_info is None:
#         raise Exception("Should never come here")

#     # call signin to check that the input password is correct
#     isPasswordValid = emailpassword_sign_in(users_info.email, request.json["oldPassword"])

#     if isinstance(isPasswordValid, EmailPasswordSignInWrongCredentialsError):
#         # TODO: handle incorrect password error
#         return
#     # update the users password
#     update_email_or_password(user_id, password=request.json["newPassword"])


#     # revoke all sessions for the user
#     revoke_all_sessions_for_user(user_id)
    
#     # revoke the user's current session, we do this to remove the auth cookies, logging out the user on the frontend
#     session.sync_revoke_session()

#     # TODO: send successful password update response

@app.get('/get_user_info_api') 
async def get_user_info_api(session: SessionContainer = Depends(verify_session())):
    user_id = session.get_user_id()
    info =  get_user_by_id(user_id)
    return info


@app.get('/signout')
async def sign_out(session: SessionContainer = Depends(verify_session())):
    await session.revoke_session() # This will delete the session from the db and from the frontend (cookies)
    return PlainTextResponse(content='success')