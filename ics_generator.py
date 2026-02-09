import json
from datetime import datetime, timedelta

class ICSGenerator:
    def __init__(self, calendar_name):
        self.calendar_name = calendar_name
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def generate_ics(self):
        ics_lines = []
        ics_lines.append("BEGIN:VCALENDAR")
        ics_lines.append("VERSION:2.0")
        ics_lines.append(f"CALSCALE:GREGORIAN")
        ics_lines.append(f"X-WR-CALNAME:{self.calendar_name}")

        for event in self.events:
            ics_lines.append("BEGIN:VEVENT")
            ics_lines.append(f"UID:{event['id']}")
            ics_lines.append(f"DTSTAMP:{event['dtstamp']}")
            ics_lines.append(f"DTSTART:{event['dtstart']}")
            ics_lines.append(f"DTEND:{event['dtend']}")
            ics_lines.append(f"SUMMARY:{event['summary']}")
            ics_lines.append(f"DESCRIPTION:{event['description']}")
            ics_lines.append("END:VEVENT")

        ics_lines.append("END:VCALENDAR")
        return '\n'.join(ics_lines)

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        generator = ICSGenerator(data['calendar_name'])
        for event in data['events']:
            generator.add_event(event)
        return generator
