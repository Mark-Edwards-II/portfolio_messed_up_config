
# Made it available on my home network by binding it to all interfaces with 0.0.0.0
run:
	uvicorn main:app --host 0.0.0.0 --reload

run_db:
	docker build . -t postgres -f postgres_folder/Dockerfile
	docker run -it -d --name postgres -p 5432:5432 postgres