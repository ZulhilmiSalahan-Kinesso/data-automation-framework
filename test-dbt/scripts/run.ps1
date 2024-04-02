param ($site)

write-host $site

$source = "dbt_projects\" + $site +"\dbt_project.yml"
$destination = ""

Copy-Item -Path $source -Destination $destination -Recurse

dbt deps

dbt run

dbt docs generate

dbt-coverage compute doc --cov-report coverage-doc.json --cov-format markdown

dbt-coverage compute test --cov-report coverage-test.json --cov-format markdown

python -m dbt_allure test

cd ./target

allure serve
