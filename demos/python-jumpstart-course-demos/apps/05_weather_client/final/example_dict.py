def main():
    d = {
        'city': 'Portland',
        'state': 'ME',
        'details': ['Cold', 'Snowy', 'Winter']
    }

    print(d.get('country', 'USA'))
    d['country'] = 'AU'
    print(d.get('country', 'USA'))
    print(d)

    w = {
        "weather": {
            "description": "scattered clouds",
            "category": "Clouds"
        },
        "wind": {
            "speed": 2.42,
            "deg": 221
        },
        "units": "imperial",
        "forecast": {
            "temp": 64.08,
            "feels_like": 63.86,
            "pressure": 1023,
            "humidity": 69,
            "low": 60.01,
            "high": 68
        },
        "location": {
            "city": "Portland",
            "country": "US",
            "state": "OR"
        },
        "rate_limiting": {
            "unique_lookups_remaining": 49,
            "lookup_reset_window": "1 hour"
        }
    }

    print(w.get('forecast').get('temp'))


if __name__ == '__main__':
    main()
