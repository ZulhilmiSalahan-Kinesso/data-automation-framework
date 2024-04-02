# Prepare the base image
docker build -t base-tools ./test-etl/

docker run -i --rm \
  --user $(id -u):$(id -g) \
  -v "$(pwd)":/miq-test \
  -w="/miq-test" \
  base-tools /bin/sh -c \
  "cd test-etl \
   && mkdir ./allure-results \
   && python -m venv --system-site-packages --copies --clear build-env \
   && . build-env/bin/activate \
   && python -m pip install --upgrade pip \
   && pip install -r requirements.txt \
   && pytest -n 4 --alluredir=allure-results 'tests/poc' \
   && rm -rf build-env"