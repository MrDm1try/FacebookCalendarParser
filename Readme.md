Missing configuraion files:
* config.py

    Should contain "facebook_token" and "target_calendar" vars
    
    To get your long-lived user access facebook token:
    * Get your short-lived token [here](https://developers.facebook.com/tools/explorer/)
    * Then update it to a long-lived token by executing
      ```
      curl -i -X GET "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&
        client_id=APP-ID&
        client_secret=APP-SECRET&
        fb_exchange_token=SHORT-LIVED-USER-ACCESS-TOKEN"
      ```

* google_credentials.json

    Should contain credentials for google API
    
* token.pickle

    Should contain google token. Can be created automatically if running on an OS with GUI.