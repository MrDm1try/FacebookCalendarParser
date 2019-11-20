import config
import facebook
import googlecalendar

fb_events = facebook.get_events(config.facebook_token)

googlecalendar.clear(config.target_calendar)

for fb_event in fb_events:
    status = googlecalendar.create_event(fb_event, config.target_calendar)
    if status != 'confirmed':
        break
