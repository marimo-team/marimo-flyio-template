# marimo fly.io Template

This template provides a basic setup for deploying a [marimo](https://marimo.io) app to [fly.io](https://fly.io).

## Requirements

- Python 3.12 or higher
- uv package manager
- fly.io account

## Setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

2. Create a virtual environment and install dependencies:

```bash
uv sync
```

3. Run locally:

```bash
uv run marimo edit
```

## Deployment

1. Install the [fly.io CLI](https://fly.io/docs/hands-on/install-flyctl/)

2. Login to fly.io:

```bash
fly auth login
```

3. Create a new app (first time only):

```bash
fly launch
```

4. Deploy:

```bash
fly deploy --remote-only
# REQUIRED! You must scale to 1 container
# because marimo is stateful.
fly scale count 1
```

## GitHub Actions Deployment

To enable automatic deployments via GitHub Actions:

1. Create a fly.io API token:

```bash
fly auth token
```

2. Add the token as a GitHub secret named `FLY_API_TOKEN`

3. Push to the main branch to trigger deployment

## Development

- Edit `src/app.py` to modify your marimo app
- The app runs on port 2718 by default
- fly.io will automatically assign a public URL

## Local Development with uv

For development, you can use uv's pip commands:

```bash
# Install a new package
uv add package-name

# Update dependencies
uv sync
```
