test-acceptance:
	./test/acceptance/mongodb_setup.py
	mocha --reporter spec \
	 test/acceptance/*.js

.PHONY: test
