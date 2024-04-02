FROM python:3.11-slim

# install the Microsoft ODBC driver for SQL Server & MSSQL Tools
# ref: https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl gnupg unixodbc-dev g++ libgssapi-krb5-2 \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql17 mssql-tools unixodbc-dev \
    && apt-get purge curl gnupg -y \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add mssql tools to path for easier use
ENV PATH="/opt/mssql-tools/bin:${PATH}"
