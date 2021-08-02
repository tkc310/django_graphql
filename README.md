# Django + GraphQL

Django で GraphQL サーバを立てるサンプル

@see https://qiita.com/hharu/items/ebe29501c0ab5f832911

## Usage

```
# migration
$ python3 manage.py migrate

# start server
$ python3 manage.py runserver

# open graphql console
$ open http://localhost:8000/graphql

# output schema.graphql
$ python3 manage.py graphql_schema --schema django_graphql.schema.schema --out schema.graphql

# add admin user & open admin
$ python3 manage.py createsuperuser
$ open http://localhost:8000/admin
```

## GraphQL Usage

- query

```
query {
  items {
    id,
    name,
    count,
  }
}
```

- mutation

```
mutation {
  createItem(name:"apple", count:10) {
    item {
      name
      count
    }
  }
}
```

## Memo

```
# add maigration file
$ python3 manage.py makemigrations
```
