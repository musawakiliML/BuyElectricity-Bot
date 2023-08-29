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
