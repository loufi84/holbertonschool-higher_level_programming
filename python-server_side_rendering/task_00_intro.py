#!/usr/bin/python
import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
"""
This module generate an invitation, based on the given template.
"""


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        logging.error("Template must be a string!")
        return

    if not isinstance(attendees, list):
        logging.error("Attendees must be a list")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("All attendees must be dictionaries")
        return

    if not template:
        logging.error("Template is empty")
        return

    if not attendees:
        logging.error("Attendees is empty")
        return

    for i, attendee in enumerate(attendees, 1):
        invitation = template

        for placeholder in ["name", "event_title", "event_date",
                            "event_location"]:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{placeholder}}}", str(value))

        output = f"output_{i}.txt"
        with open(output, 'w') as f:
            f.write(invitation)
