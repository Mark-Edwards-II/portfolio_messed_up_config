
run-dev:
# Made it available on my home network by binding it to all interfaces with 0.0.0.0
	uvicorn main:app --host 0.0.0.0 --reload