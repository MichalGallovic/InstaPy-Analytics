# InstaPy Analytics

InstaPy Analytics allows you to **read** analytical data from `instapy.db` produced by [InstaPy](https://github.com/timgrossmann/InstaPy) and **send** them to Analytical server. 

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```
python send_analytics.py 
    --username instagram_account 
    --database path_to_instapy.db
    --host analytics_server_url
    [ --container_name docker_container name]
    [ --token analytics_server_api_token ]
    
# --container_name - if you need to extract instapy.db from docker container
```

## Currently supports:
 - *profile activity* (`recordsActivity`)
 - *profile progress* (`accountsProgress`)

## Server endpoints
Analytical Server endpoints can be configured in `config.json`.
