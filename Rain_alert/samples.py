# Sample response from Openweather API
wx_sample_response =  {
    "lat": 52.2297,
    "lon": 21.0122,
    "timezone": "Sakhile/Mars",
    "timezone_offset": 3600,
    "data": [
        {
        "dt": 1645888976,
        "sunrise": 1645853361,
        "sunset": 1645891727,
        "temp": 279.13,
        "feels_like": 276.44,
        "pressure": 1029,
        "humidity": 64,
        "dew_point": 272.88,
        "uvi": 0.06,
        "clouds": 0,
        "visibility": 10000,
        "wind_speed": 3.6,
        "wind_deg": 340,
        "weather": [
            {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01d"
            }
        ]
        }
    ]
}

sample_dict_wx_data = {
    "dt": 1645888976,
    "sunrise": 1645853361,
    "sunset": 1645891727,
    "temp": 279.13,
    "feels_like": 276.44,
    "pressure": 1029,
    "humidity": 64,
    "dew_point": 272.88,
    "uvi": 0.06,
    "clouds": 0,
    "visibility": 10000,
    "wind_speed": 3.6,
    "wind_deg": 340,
    "weather": [
        {
        "id": 800,
        "main": "Clear",
        "description": "clear sky",
        "icon": "01d"
        }
    ]   
}

# Sample response from Twilio
400 - BAD REQUEST - The data given in the POST or PUT failed validation. Inspect the response body for details.
{
  "code": 21608,
  "message": "The number +27082581XXXX is unverified. Trial accounts cannot send messages to unverified numbers; verify +27082581XXXX at twilio.com/user/account/phone-numbers/verified, or purchase a Twilio number to send messages to unverified numbers",
  "more_info": "https://www.twilio.com/docs/errors/21608",
  "status": 400
}