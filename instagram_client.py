import logging
import time
from instagrapi import Client
from config import (
    INSTAGRAM_USERNAME, 
    INSTAGRAM_PASSWORD, 
    INSTAGRAM_APP_ID, 
    INSTAGRAM_APP_SECRET
)
from utils import random_delay

class InstagramClient:
    def __init__(self):
        self.client = Client()
        self.client.set_settings({
            "app_id": INSTAGRAM_APP_ID,
            "app_secret": INSTAGRAM_APP_SECRET
        })

    def login(self):
        random_delay(30, 60)
        try:
            self.client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
            logging.info("✅ Logged into Instagram successfully.")
        except Exception as e:
            logging.error(f"❌ Instagram login failed: {e}")
            raise e

    def fetch_unread_threads(self):
        try:
            inbox_threads = self.client.direct_threads(selected_filter='unread')
            unread_threads = [thread for thread in inbox_threads if thread.messages]
            logging.info(f"📩 Found {len(unread_threads)} threads with unread messages.")
            return unread_threads
        except Exception as e:
            logging.error(f"❌ Error fetching threads: {e}")
            return []

    def send_message(self, thread_id, message, hold=False):
        try:
            self.client.direct_send(message, thread_ids=[thread_id])
            if hold:
                time.sleep(1)  # Hold for 1 second
            logging.info(f"✉️ Sent message in thread {thread_id}.")
        except Exception as e:
            logging.error(f"❌ Error sending message in thread {thread_id}: {e}")

    def get_following_list(self):
        """Returns a list of user IDs you are following."""
        try:
            following = self.client.user_following(self.client.user_id)
            following_ids = list(following.keys())
            logging.info(f"👥 Found {len(following_ids)} accounts you are following.")
            return following_ids
        except Exception as e:
            logging.error(f"❌ Error fetching following list: {e}")
            return []

    def get_user_stories(self, user_id):
        """Retrieves active stories for a given user ID."""
        try:
            stories = self.client.user_stories(user_id)
            logging.info(f"📖 User {user_id} has {len(stories)} active stories.")
            return stories
        except Exception as e:
            logging.error(f"❌ Error fetching stories for user {user_id}: {e}")
            return []

    def like_story(self, story_id):
        """Likes a single story given its ID."""
        try:
            self.client.story_like(story_id)
            logging.info(f"❤️ Liked story {story_id}.")
        except Exception as e:
            logging.error(f"❌ Error liking story {story_id}: {e}")

    def mark_thread_as_seen(self, thread_id):
        try:
            self.client.direct_thread_seen(thread_id)
            logging.info(f"✅ Marked thread {thread_id} as seen.")
        except Exception as e:
            logging.error(f"❌ Error marking thread {thread_id} as seen: {e}")
            
    def super_react(self, thread_id, reaction="❤️"):
        """Send a super reaction with tab and hold"""
        try:
            # Send initial reaction
            self.client.direct_send(reaction, thread_ids=[thread_id])
            # Simulate tab press and hold for super react
            self.client.direct_send("\t", thread_ids=[thread_id])
            time.sleep(1)  # Hold for effect
            # Send final confirmation
            self.client.direct_send(reaction, thread_ids=[thread_id], hold=True)
        except Exception as e:
            logging.error(f"❌ Error sending super reaction in thread {thread_id}: {e}")
