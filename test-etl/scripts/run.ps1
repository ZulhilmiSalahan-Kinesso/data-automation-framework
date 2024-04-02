docker run -i --rm `
  -v ${pwd}:/miq-test `
  -w="/miq-test" `
  python:3.11.4-slim /bin/sh -c "apt-get update && apt-get install -y --no-install-recommends curl gnupg unixodbc-dev && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && apt-get update && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql17 mssql-tools unixodbc-dev && apt-get purge curl gnupg -y && apt-get autoremove -yqq --purge && apt-get clean && rm -rf /var/lib/apt/lists/* && python -m pip install --upgrade pip && pip install -r requirements.txt && pytest -n 4 --alluredir=allure-results 'tests/mssql_test.py'"
  