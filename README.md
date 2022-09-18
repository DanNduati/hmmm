<h1 align="center">HMMMMMMM</h1>

[![Project Status: WIP – Initial development is in progress.](https://www.repostatus.org/badges/latest/wip.svg)]()

## <b>Description</b>
Is there a correlation between my [smart watch](https://www.mi.com/global/mi-smart-band-5/) vitals and sleep analysis data and my code stats on [Wakatime](https://wakatime.com/)?

## <b>Prerequisites</b>
- Python3
- [Wakatime account](https://wakatime.com/)

## <b>Setup</b>
```bash
$ git clone https://github.com/DanNduati/hmmm.git
$ cd hmmm/
```

## <b>Install dependencies</b>
Create a python virtual environment activate it and install dependencies:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Create a `.env` file similar to [`.env.example`](./.env.example) with your Wakatime [API Key](https://wakatime.com/settings/api-key).

## <b>Get user coding activity</b>
```bash
$ python3 main.py | jq
```
Output:
```json
{
  "cummulative_total": {
    "decimal": "2.08",
    "digital": "2:05",
    "seconds": 7514.0,
    "text": "2 hrs 5 mins"
  },
  "data": [
    {
      "categories": [
        {
          "decimal": "2.08",
          "digital": "2:05:14",
          "hours": 2,
          "minutes": 5,
          "name": "Coding",
          "percent": 100.0,
          "seconds": 14,
          "text": "2 hrs 5 mins",
          "total_seconds": 7514.0
        }
      ],
      "editors": [
        {
          "decimal": "2.07",
          "digital": "2:04:48",
          "hours": 2,
          "minutes": 4,
          "name": "Neovim",
          "percent": 99.66,
          "seconds": 48,
          "text": "2 hrs 4 mins",
          "total_seconds": 7488.539119
        },
        {
          "decimal": "0.00",
          "digital": "0:00:25",
          "hours": 0,
          "minutes": 0,
          "name": "VS Code",
          "percent": 0.34,
          "seconds": 25,
          "text": "25 secs",
          "total_seconds": 25.460881
        }
      ],
      "grand_total": {
        "decimal": "2.08",
        "digital": "2:05",
        "hours": 2,
        "minutes": 5,
        "text": "2 hrs 5 mins",
        "total_seconds": 7514.0
      },
      "languages": [
        {
          "decimal": "1.90",
          "digital": "1:54:10",
          "hours": 1,
          "minutes": 54,
          "name": "Go",
          "percent": 91.16,
          "seconds": 10,
          "text": "1 hr 54 mins",
          "total_seconds": 6850.0
        },
        {
          "decimal": "0.15",
          "digital": "0:09:05",
          "hours": 0,
          "minutes": 9,
          "name": "Python",
          "percent": 7.25,
          "seconds": 5,
          "text": "9 mins",
          "total_seconds": 545.0
        },
        {
          "decimal": "0.02",
          "digital": "0:01:43",
          "hours": 0,
          "minutes": 1,
          "name": "JSON",
          "percent": 1.37,
          "seconds": 43,
          "text": "1 min",
          "total_seconds": 103.0
        },
        {
          "decimal": "0.00",
          "digital": "0:00:16",
          "hours": 0,
          "minutes": 0,
          "name": "Bash",
          "percent": 0.21,
          "seconds": 16,
          "text": "16 secs",
          "total_seconds": 16.0
        }
      ],
      "machines": [
        {
          "decimal": "2.08",
          "digital": "2:05:14",
          "hours": 2,
          "machine_name_id": "**",
          "minutes": 5,
          "name": "dan",
          "percent": 100.0,
          "seconds": 14,
          "text": "2 hrs 5 mins",
          "total_seconds": 7514.0
        }
      ],
      "operating_systems": [
        {
          "decimal": "2.08",
          "digital": "2:05:14",
          "hours": 2,
          "minutes": 5,
          "name": "Linux",
          "percent": 100.0,
          "seconds": 14,
          "text": "2 hrs 5 mins",
          "total_seconds": 7514.0
        }
      ],
      "projects": [
        {
          "color": null,
          "decimal": "1.90",
          "digital": "1:54:10",
          "hours": 1,
          "minutes": 54,
          "name": "portfolio",
          "percent": 91.16,
          "seconds": 10,
          "text": "1 hr 54 mins",
          "total_seconds": 6850.0
        },
        {
          "color": null,
          "decimal": "0.18",
          "digital": "0:11:04",
          "hours": 0,
          "minutes": 11,
          "name": "smart_sleep",
          "percent": 8.84,
          "seconds": 4,
          "text": "11 mins",
          "total_seconds": 664.0
        }
      ],
      "range": {
        "date": "2022-09-18",
        "end": "2022-09-18T20:59:59Z",
        "start": "2022-09-17T21:00:00Z",
        "text": "Today",
        "timezone": "Africa/Nairobi"
      }
    }
  ],
  "end": "2022-09-18T20:59:59Z",
  "start": "2022-09-17T21:00:00Z"
}
```

## <b>License and Copyright</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)
Copyright 2022 Daniel Chege Nduati
