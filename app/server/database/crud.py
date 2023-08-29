from bson.objectid import ObjectId

from app.server.database.db_connection import user_sessions

from app.server.serializers.user_sessions import user_session_serializer

# get all sessions

async def get_all_user_sessions():
    user_sessions_data = []
    async for session in user_sessions.find():
        user_sessions_data.append(user_session_serializer(session))
        return user_sessions_data

# get single session

async def get_single_session(id: str):
    user_session = await user_sessions.find_one({"_id":ObjectId(id)})
    if user_session:
        return user_session_serializer(user_session)

# Add user session

async def add_user_session(user_session_data: dict):
    user_session = await user_sessions.insert_one(user_session_data)
    new_user_session = await user_sessions.find_one({"_id":user_session.inserted_id})
    return user_session_serializer(new_user_session)
