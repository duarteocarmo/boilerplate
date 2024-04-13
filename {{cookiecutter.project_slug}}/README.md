# {{cookiecutter.project_title}}

{{cookiecutter.project_description}}

## Development

Note: We use [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started) for installing things, make sure you have it.

1. Make sure you are running in a virtual environment (e.g., `python3 -m venv .env`)
2. Activate it (e.g. `source .env/bin/activate`)

```shell
(.env) $ make install-dev
```

3. Run the tests

```shell
(.env) $ make test
```

4. Run the API

```shell
(.env) $ make api
```

5. For more help:
```shell
(.env) $ make help
```
