# Arcade DB Downloader

Downloads arcade db files with support for internetarchive auth credentials. If IA is behaving properly, you should just use update_all, not this!

## Instructions:

```sh
# get to your Scripts folder
$ cd /media/fat/Scripts

# download the python script from this repo
$ curl -LOs --cacert /etc/ssl/certs/cacert.pem https://raw.githubusercontent.com/tamagokun/arcade_db_downloader/main/downloader.py

# install the `ia` command line tool: https://archive.org/developers/internetarchive/cli.html
$ curl -LOs --cacert /etc/ssl/certs/cacert.pem https://archive.org/download/ia-pex/ia
$ chmod +x ia
$ ./ia configure

# run this bad boy
$ python downloader.py
```
