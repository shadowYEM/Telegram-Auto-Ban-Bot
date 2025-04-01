from telethon import TelegramClient, events
from telethon.tl.functions.channels import GetParticipantRequest, GetAdminLogRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator, ChannelAdminLogEvent

# API credentials
# Replace these placeholders with your own API ID and Hash from my.telegram.org
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

# Bot token
# Replace this placeholder with your bot token obtained from BotFather
bot_token = 'YOUR_BOT_TOKEN'

# Channel ID
# Replace this with the ID of the channel where the bot will operate
channel_id = -1001510842176

# Create the client and connect
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

async def check_bot_permissions():
    """Check if the bot has the necessary permissions to ban users."""
    participant = await client(GetParticipantRequest(
        channel=channel_id,
        participant='me'
    ))

    if isinstance(participant.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)):
        print("Bot has the necessary permissions to ban users.")
        await ban_recently_left_users()
    else:
        print("Bot does not have the necessary permissions to ban users.")

async def ban_recently_left_users():
    """Ban users who left the channel before the bot became an admin."""
    # Fetch recent admin log events
    admin_log = await client(GetAdminLogRequest(
        channel=channel_id,
        limit=100  # Adjust the limit as needed
    ))

    for event in admin_log.events:
        if isinstance(event.action, ChannelAdminLogEvent) and hasattr(event.action, 'user_id') and event.action.user_id:
            user_id = event.action.user_id
            await client.edit_permissions(channel_id, user_id, view_messages=False)
            print(f"Banned {user_id} for leaving the channel before the bot became admin.")

@client.on(events.ChatAction())
async def handler(event):
    """Handle chat actions and ban users who leave the channel."""
    if event.user_left or event.user_kicked:
        user = await event.get_user()
        await client.edit_permissions(channel_id, user.id, view_messages=False)
        print(f"Banned {user.id} for leaving the channel.")

# Run the client
with client:
    client.loop.run_until_complete(check_bot_permissions())
    client.run_until_disconnected()
