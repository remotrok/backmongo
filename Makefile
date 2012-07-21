test-acceptance:
	@./test/acceptance/backmongo_server_setup.py
	@./test/acceptance/mongodb_setup.py
	@mocha --reporter spec \
	 test/acceptance/*.js
	@kill `cat /tmp/backmongo-test-server.pid`
	@rm /tmp/backmongo-test-server.pid

start-test-server:
	./test/acceptance/backmongo_server_setup.py

stop-test-server:
	kill `cat /tmp/backmongo-test-server.pid`
	rm /tmp/backmongo-test-server.pid

.PHONY: test
