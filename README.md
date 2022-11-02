# Leadplusnews

A test project for Leadplus. Django app for consuming and serving articles from Newsapi.com

** please read FAQ section below for known bugs **

## Requirements

- **Python:** >3.10

## Environment Variables

To run this project, you will need to add the following environment variables to your <project folder>/leadplusnews/.env file

`NEWSAPI_KEY`

#### 1) Get Api Key from Newsapi.com

[Visit Newsapi.com/register](https://newsapi.org/register)

#### 2) Clone .env.example to .env

```bash
  cp leadplusnews/.env.example leadplusnews/.env
```

#### 3) Update .env with apikey from Newsapi.com

## Run Locally

Clone the project

```bash
  git clone https://github.com/rafazafar/leadplusnews
```

Go to the project directory

```bash
  cd leadplusnews
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Apply DB Migrations

```bash
  python manage.py migrate
```

Create Superser

```bash
  python manage.py createsuperuser
```

Start server

```bash
  python manage.py runserver
```

Visit site at [http://localhost:8000](http://localhost:8000)

or

Visit admin at [http://localhost:8000/admin](http://localhost:8000/admin)

## API Reference

#### Get all available APIs

```http
  GET /api
```

#### Get latest 100 Articles in JSON

```http
  GET /api/articles?format=json
```

## Seeding Database

Run seeding command from project root folder.
This will take a while.

```bash
  python manage.py seed
```

## Delete All Articles

Use with caution

```bash
  python manage.py delete_all_articles
```

## FAQ

#### Why do Articles not have PublishedAt data ?

Using older v1 /article endpoint as per test instructions. The endpoint is depricated and has some issue. One being that the datetime data is always null.

## License

Django: [BSD](https://choosealicense.com/licenses/bsd/)
