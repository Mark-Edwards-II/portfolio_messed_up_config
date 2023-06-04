# portfolio
This is entended to be a light weight web app to display personal development projects and a project in itself that is Perpetually in development.

---

## TODOs
- [] Finish basic styling / minimum viable product
- [] build out IAC to easily make changes to deployed instance.
- [] deploy to AWS
- [x] set up pipenv
- [] add a reusable project template so projects can be viewed with more details.
- [] isolate web app to just 
- [x] add a database locally.
    - [] create project model for database very simple to start. 
    - [] set up alembic
    - [] connect local app to database

---

### first level dependencies
- fastapi
- uvicorn
- jinja2
- pydantic
- sqlalchemy
- alembic


psql -h localhost -p <Port> -d <Name> -U <User> -W

postgresql://myuser:mypassword@localhost:5432/mydatabase