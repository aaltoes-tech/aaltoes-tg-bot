import aiohttp
import logging
from typing import List, Dict, Any
from datetime import datetime

class EventsRepository:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.lu.ma/public/v1"
        self.headers = {
            "accept": "application/json",
            "x-luma-api-key": api_key
        }

    async def get_upcoming_events(self) -> List[Dict[str, Any]]:
        """Fetch upcoming events from Luma calendar"""
        try:
            async with aiohttp.ClientSession() as session:
                # Get current time in ISO 8601 format
                current_time = datetime.utcnow().isoformat() + "Z"
                url = f"{self.base_url}/calendar/list-events"
                params = {
                    "after": current_time
                }
                
                async with session.get(url, headers=self.headers, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        return self._format_events(data.get("entries", []))
                    else:
                        error_data = await response.json()
                        logging.error(f"Failed to fetch events: {error_data}")
                        return []

        except Exception as e:
            logging.error(f"Error fetching events: {e}")
            return []

    def _format_events(self, events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Format events into a more readable structure"""
        formatted_events = []

        for event_data in events:
            try:
                # Extract the actual event data from the nested structure
                event = event_data.get('event', {})
                if not event:
                    continue
                    
                start_time = datetime.fromisoformat(event["start_at"].replace("Z", "+00:00"))
                formatted_events.append({
                    "id": event["api_id"],
                    "title": event["name"],
                    "description": event.get("description", ""),
                    "start_time": start_time,
                    "url": event.get("url", ""),
                    "location": event.get("geo_address_json", {}).get("full_address", ""),
                    "image_url": event.get("cover_url", "")
                })
            except Exception as e:
                logging.error(f"Error formatting event {event.get('api_id')}: {e}")
                continue
        
        return formatted_events 