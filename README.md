# InstaPy Analytics

InstaPy Analytics allows you to **read** analytical data from `instapy.db` produced by [InstaPy](https://github.com/timgrossmann/InstaPy) and **send** them to Analytical server. 

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
python send_analytics.py 
    --username instagram_account 
    --database path_to_instapy.db
    --host analytics_server_url
    [ --token analytics_server_api_token ]
```

## Currently supports:
 - *profile activity* (`recordsActivity`)
 - *profile progress* (`accountsProgress`)

## Server endpoints
Analytical Server endpoints can be configured in `config.json`.
