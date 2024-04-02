# Prepare the base image
docker build -t base-tools ./test-etl/

docker run -i --rm \
  --user $(id -u):$(id -g) \
  -v "$(pwd)":/miq-test \
  -w="/miq-test" \
  base-tools /bin/sh -c \
  "cd test-dbt \
   && python -m venv --system-site-packages --copies --clear build-env \
   && . build-env/bin/activate \
   && python -m pip install --upgrade pip \
   && pip install -r requirements.txt \
   && dbt deps && python -m dbt_allure test \
   && rm -rf build-env"