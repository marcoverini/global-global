name: Monthly air data update

on:
  schedule:
    - cron: '0 0 1 * *'   # runs at midnight UTC on the 1st of each month
  workflow_dispatch:       # allows manual trigger

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests

      - name: Run update script
        run: python air/update_air_data.py

      - name: Commit CSV changes
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: "Automated update: air_routes.csv on $(date -u +'%Y-%m-%d')"
          file_pattern: "air/air_routes.csv"
          github_token: ${{ secrets.GITHUB_TOKEN }}

