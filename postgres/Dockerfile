# Use an official PostgreSQL as the base image
FROM postgres:latest

# Set the environment variables for the PostgreSQL database
ENV POSTGRES_USER myuser
ENV POSTGRES_PASSWORD mypassword
ENV POSTGRES_DB mydatabase

# # Copy custom initialization scripts to the docker-entrypoint-initdb.d directory
# # This will be executed when the container starts for the first time
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the default PostgreSQL port
# EXPOSE 5432

# RUN \q