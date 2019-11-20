import requests
# import yaml


def get_events(token):
    ans = requests.get("https://graph.facebook.com/v5.0/me?fields=events&access_token={}".format(token))
    events = ans.json()['events']['data']

    # with open('temp.txt', 'w') as f:
    #     f.write(yaml.dump(events))
    # with open('temp.txt', 'r') as f:
    #     events = yaml.safe_load(f)

    return events
