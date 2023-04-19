run:
	docker build -t youtube-object-detection .
	docker rm -f app-youtube-object-detection
	docker run -d --name app-youtube-object-detection -p 8080:8080 youtube-object-detection

stop:
	docker stop app-youtube-object-detection

remove:
	docker rm -f app-youtube-object-detection

run-local:
	export PYTHONPATH=. ; \
	python app/main.py
