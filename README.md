# GDToT Bypasser

A web scraper to convert GDToT links to Google Drive and direct download links

### Installation
Clone this repository
```
git clone https://github.com/viperadnan-git/gdtot-bypasser
cd gdtot-bypasser
```

Install python3.x
```
apt install python3
```

Install required python packages
```
pip install -r requirements.txt
```

### Configuration

Add these config's in environment variables or [`.env`]("./.env.sample") file
- `HOST`: Host to listen on (Default 0.0.0.0)
- `PORT`: Host to listen on (Default 8000)
- `PHPSESSID`: Get it from cookies in GDToT website after logging in
- `CRYPT`: Get it from cookies in GDToT website after logging in
- `GDOWN_URL`: Google Drive download by File ID index's base URL

**Multiple Cookies**
To use multiple cookies add your all cookies in [`config.json`]("./config.json.sample")

### Deploying
Run [`run.py`]("./run.py") module via python3
```
python3 run.py
```

### Deployin on Docker

Build docker image
```
docker build -t gdtot-bypasser .
```

Start docker container
```
docker run -dp 3000:3000 gdtot-bypasser
```

### Deploying on Caprover
```
tar -cvf gdtot-bypasser.tar .
```

This will generate a `gdtot-bypasser.tar` file, use it on caprover's deployment dashboard to deploy.