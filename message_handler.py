
import logging
from utils import random_delay

def like_unread_messages(instagram_client):
    unread_threads = instagram_client.fetch_unread_threads()
    for thread in unread_threads:
        try:
            for message in thread.messages:
                instagram_client.client.direct_send("❤️", thread_ids=[thread.id])
                random_delay(5, 15)
        except Exception as e:
            logging.error(f"❌ Error liking messages in thread {thread.id}: {e}")

def reply_to_unread_messages(instagram_client):
    unread_threads = instagram_client.fetch_unread_threads()
    for thread in unread_threads:
        try:
            # Reply to all messages in the thread
            for message in thread.messages:
                instagram_client.client.direct_send("❤️", thread_ids=[thread.id])
                random_delay(2, 5)
            
            # Additional reply if needed
            instagram_client.send_message(thread.id, "❤️")
            
            # Open thread messages and mark as seen
            instagram_client.client.direct_thread_mark_seen(thread.id)
            logging.info(f"👁️ Opened messages in thread {thread.id}")
            
            # Super react with tab and hold
            instagram_client.super_react(thread.id, "❤️")
            logging.info(f"💫 Sent super reaction in thread {thread.id}")
            
            random_delay(5, 15)
        except Exception as e:
            logging.error(f"❌ Error replying in thread {thread.id}: {e}")
