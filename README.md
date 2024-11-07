# Demo Trestle-bot CLI using Click


Based off of https://github.com/jpower432/jpower432-go-cli/tree/feat/template-update

# Quickstart

```
pip install -r requirements.txt

python main.py autosync --working-dir "<DIR>"
```

# Config

To set the `workding-dir` via config, edit `.trestlebot/config.yml`:

``` yaml
working_dir: "<DIR>""
```

To set the `working-dir` via env var:

``` bash
export TRESTLEBOT_WOKRING_DIR=<DIR>
```
