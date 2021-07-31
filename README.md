# Django + GraphQL

Django で GraphQL サーバを立てるサンプル

@see https://qiita.com/hharu/items/ebe29501c0ab5f832911

## Usage

```
# migration
$ python3 manage.py migrate

# start server
$ python3 manage.py runserver

# open
open http://localhost:8000/graphql
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
